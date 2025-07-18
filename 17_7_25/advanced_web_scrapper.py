import os
import re
import requests
import time
import yfinance as yf
import pandas as pd
from urllib.parse import quote
from bs4 import BeautifulSoup
from newspaper import Article
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from stock_analysis_worker import analyze_stock_csv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

# Helpers
def is_stock_topic(topic: str) -> bool:
    return any(word in topic.lower() for word in ['stock', 'stocks', 'share', 'share price', 'market'])

def extract_ticker_symbol(topic: str) -> str:
    known_tickers = {
        "apple": "AAPL", "google": "GOOG", "alphabet": "GOOG",
        "microsoft": "MSFT", "amazon": "AMZN",
        "tesla": "TSLA", "meta": "META", "facebook": "META"
    }
    for name, ticker in known_tickers.items():
        if name in topic.lower():
            return ticker
    return None

def get_stock_data(ticker_symbol: str):
    print(f"\n📈 Fetching stock data for: {ticker_symbol}")
    ticker = yf.Ticker(ticker_symbol)
    try:
        data = ticker.history(period="1y")
        filename = f"{ticker_symbol}_stock_history.csv"
        data.to_csv(filename)

        info = {
            "market_cap": ticker.info.get("marketCap", "N/A"),
            "pe_ratio": ticker.info.get("trailingPE", "N/A"),
            "dividend_yield": ticker.info.get("dividendYield", "N/A"),
            "csv_file": filename
        }

        print("\n🧾 Basic Financial Info:")
        for k, v in info.items():
            print(f"{k.replace('_', ' ').title()}: {v}")

        analysis = analyze_stock_csv(filename)
        print(f"\n📊 Data Analysis:\n{analysis}")
        return {"type": "stock", "info": info, "analysis": analysis}

    except Exception as e:
        return {"error": f"Failed to fetch stock data: {e}"}

def extract_urls(text):
    return re.findall(r"https?://[^\s)>\]]+", text)

def scrape_url(url, max_paragraphs=5):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            return f"❌ Failed to fetch {url} — Status code: {res.status_code}"
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        return text[:2000]
    except Exception as e:
        return f"❌ Error scraping {url}: {e}"

def llm_scrape_and_clean(topic):
    print("\n🧠 Using LLM to fetch useful URLs...")
    prompt = PromptTemplate.from_template("Give me 3 valid URLs (Wikipedia or other reputable sites) to scrape for the topic:\n\n{topic}")
    urls = extract_urls((prompt | llm).invoke({"topic": topic}).content)
    
    content = ""
    for url in urls[:2]:
        print(f"\n🌐 Scraping: {url}")
        content += scrape_url(url)
        time.sleep(1)

    if not content:
        return "❌ No content could be scraped."

    clean_prompt = PromptTemplate.from_template(
        "Given the following content I want you to present this beautifully:\n\n{content}"
    )
    final = (clean_prompt | llm).invoke({"content": content})
    return final.content

def fallback_scraper(topic, num_results=3):
    query = quote(topic)
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    urls = []
    for a in soup.find_all("a", href=True):
        match = re.search(r'/url\?q=(https?://[^&]+)&', a["href"])
        if match:
            url = match.group(1)
            if "google.com" not in url:
                urls.append(url)
        if len(urls) >= num_results:
            break

    summaries = []
    for url in urls:
        print(f"\n🌐 Scraping (fallback): {url}")
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            summaries.append(article.summary)
        except Exception as e:
            summaries.append(f"❌ Failed to scrape {url}: {e}")
    return summaries

# 👷 Main worker function
def hybrid_scraper_worker(topic: str) -> dict:
    result = {"topic": topic}

    if is_stock_topic(topic):
        ticker = extract_ticker_symbol(topic)
        if ticker:
            result.update(get_stock_data(ticker))
        else:
            result["error"] = "Could not infer stock ticker."

    print("\n🔧 Trying LLM-based scraping...")
    llm_result = llm_scrape_and_clean(topic)
    if llm_result.startswith("❌"):
        print("LLM scraping failed. Using fallback...")
        fallback = fallback_scraper(topic)
        result["scraped"] = {"mode": "fallback", "summaries": fallback}
    else:
        result["scraped"] = {"mode": "llm", "content": llm_result}

    return result
