from dotenv import load_dotenv
import os
import re
import requests
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Set up the LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

# Prompt template to get URLs
prompt = PromptTemplate.from_template(
    "Give me valid URLs (Wikipedia or other reputable sites) that I can web scrape for the topic:\n\n{topic}"
)
worker = prompt | llm

# Function to extract URLs from LLM output
def extract_urls(text):
    return re.findall(r"https?://[^\s)>\]]+", text)

# Function to scrape text from a URL
def scrape_url(url, max_paragraphs=5):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            return f"❌ Failed to fetch {url} — Status code: {res.status_code}"

        soup = BeautifulSoup(res.text, "html.parser")

        # Try to get main content
        paragraphs = soup.find_all("p")
        text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        return text[:2000]  # Truncate for readability

    except Exception as e:
        return f"❌ Error scraping {url}: {e}"

def main_function(topic):
    # Get topic from user
    topic = topic

    # Invoke the LLM to get URLs
    llm_output = worker.invoke({"topic": topic})
    # print("\n🧠 LLM Output:\n", llm_output.content)

    # Extract URLs from the output
    urls = extract_urls(llm_output.content)
    # print("\n🌐 Extracted URLs:")
    # for i, url in enumerate(urls, 1):
    #     print(f"{i}. {url}")

    # Ask user if they want to scrape the URLs
    content = ""
    if urls:
        # print("\n🔍 Scraping top 1-2 URLs...\n")
        for url in urls[:2]:  # You can change how many you want to scrape
            # print(f"\n📄 Content from: {url}\n")
            # print(scrape_url(url))
            content += scrape_url(url)
            # print("\n" + "-"*80 + "\n")
    else:
        print("❌ No valid URLs found.")

    # Prompt template to get URLs
    prompt = PromptTemplate.from_template(
        "Given the following content I want you to present this beautifully :\n\n{content}"
    )
    cleaner = prompt | llm
    response = cleaner.invoke({"content" : content})
    return response.content