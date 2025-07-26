# advanced_web_scraper.py
import re
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import yfinance as yf
import pandas as pd
from urllib.parse import quote
import time

def is_stock_topic(topic: str) -> bool:
    return any(word in topic.lower() for word in ['stock', 'stocks', 'share', 'share price', 'market'])

def extract_ticker_symbol(topic: str) -> str:
    known_tickers = {
        "apple": "AAPL",
        "google": "GOOG",
        "alphabet": "GOOG",
        "microsoft": "MSFT",
        "amazon": "AMZN",
        "tesla": "TSLA",
        "meta": "META",
        "facebook": "META",
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
        data.to_csv(f"{ticker_symbol}_stock_history.csv")

        print("\n🧾 Basic Financial Info:")
        print(f"Market Cap: {ticker.info.get('marketCap', 'N/A')}")
        print(f"Trailing P/E: {ticker.info.get('trailingPE', 'N/A')}")
        print(f"Dividend Yield: {ticker.info.get('dividendYield', 'N/A')}")

        print(f"\n✅ Historical data saved to: {ticker_symbol}_stock_history.csv")

    except Exception as e:
        print(f"❌ Failed to fetch stock data: {e}")

def google_search_urls(topic, num_results=3):
    print(f"\n🔍 Searching sources for: {topic}")
    query = quote(topic)
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        match = re.search(r'/url\?q=(https?://[^&]+)&', href)
        if match:
            url = match.group(1)
            if "webcache.googleusercontent.com" not in url and "google.com" not in url:
                urls.append(url)
        if len(urls) >= num_results:
            break
    return urls

def scrape_and_summarize(url):
    print(f"\n🌐 Scraping: {url}")
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        print(f"\n🔗 URL: {url}")
        print(f"\n📝 Content:\nHere is a clean and summarized version of the content:\n\n{article.summary}")
        return article.summary

    except Exception as e:
        print(f"❌ Failed to scrape: {url}\nReason: {e}")
        return None

def main():
    topic = input("Enter a topic: ").strip()

    if is_stock_topic(topic):
        ticker_symbol = extract_ticker_symbol(topic)
        if ticker_symbol:
            get_stock_data(ticker_symbol)
        else:
            print("⚠️ Could not infer stock ticker from topic. Try using the company name (e.g., 'Apple stock').")
    else:
        urls = google_search_urls(topic)
        for url in urls:
            scrape_and_summarize(url)
            time.sleep(1)

if __name__ == "__main__":
    main()
