# tools/web_tool.py
from langchain.tools import Tool
from tools.web_scraper import scrape_website

web_scrape_tool = Tool(
    name="WebScraper",
    func=scrape_website,
    description="Use this to scrape content from a website given a URL."
)
