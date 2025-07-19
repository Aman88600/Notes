# Imports for api key
from dotenv import load_dotenv
import os

# Imports for LLM setup and execution
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

# Import to get plan list
import re

# Getting workers
from web_scraper import hybrid_scraper_worker
from summarizer_worker import summarizer_function

# Getting the api key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# LLM setup
llm = ChatGroq(
    groq_api_key = api_key,
    model_name="llama3-8b-8192"
)

# Making a prompt template for the supervisor model
supervisor_prompt = PromptTemplate.from_template(
"""You are a task routing supervisor. Based on the user's query, choose the right tools to use.

Available actions: ["scrape", "summarize", "translate", "calculate", "define"]

Rules:
- Use "scrape" if fresh data, company info, or stock data is needed.
- Use "summarize" to condense content.
- Use "translate" for language conversion.
- Use "calculate" for math or numeric tasks.
- Use "define" to explain concepts or terms.

Return only a Python list like: ["scrape", "summarize"] anything else

Query: {query}
"""
)

supervisor_model = supervisor_prompt | llm

def supervisor_function(query):
    plan_msg = supervisor_model.invoke({"query" : query})

    # Getting the plan list
    plan_text = plan_msg.content.strip()
    match = re.search(r"\[(.*?)\]", plan_text)
    plan = eval("[" + match.group(1) + "]")

    print(plan)
    # Executing the plan step by step
    for step in plan:
        print(f"Exceuting {step}")
        if step == "scrape":
            print("Scrapping.....")
            data = hybrid_scraper_worker(query)
        elif step == "summarize":
            data = summarizer_function()
        elif step == "translate":
            print("Translating....")
        elif step == "define":
            print("Defining....")
    return f"\nFinal Output:\n{data}"
if __name__ == "__main__":
    # Taking User input
    query = input("Enter your Query : ")
    result = supervisor_function(query)
    if isinstance(result, dict):
        # Pretty printing the dictionary result
        if "topic" in result:
            print(f"Topic: {result['topic'].title()}")
        if "type" in result:
            print(f"Type: {result['type'].capitalize()}")

        if "info" in result:
            print("\n Basic Stock Info:")
            info = result["info"]
            print(f"• Market Cap      : ${info.get('market_cap'):,}")
            print(f"• P/E Ratio       : {info.get('pe_ratio')}")
            print(f"• Dividend Yield  : {info.get('dividend_yield') * 100:.2f}%")
            print(f"• CSV File Saved  : {info.get('csv_file')}")

        if "analysis" in result:
            print("\n Stock Analysis Summary:")
            print(result["analysis"])

        if "scraped" in result:
            print("\n Scraped Info (from web):")
            print(result["scraped"].get("content", ""))

        if "summary" in result:
            print("\n Summary:")
            print(result["summary"])

    else:
        print(result)