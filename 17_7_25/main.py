import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

from advanced_web_scrapper import hybrid_scraper_worker
from summarizer import summarizer_function
from translator_worker import translator_function
from calculator_agent import calculator_function
from define_worker import define_function

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Setup Groq LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

# Routing Prompt (with 5 workers)
routing_prompt = PromptTemplate.from_template(
    """You are a task routing supervisor. Based on the user's query, choose the right tools to use.

Available actions: ["scrape", "summarize", "translate", "calculate", "define"]

Rules:
- Use "scrape" if fresh data, company info, or stock data is needed.
- Use "summarize" to condense content.
- Use "translate" for language conversion.
- Use "calculate" for math or numeric tasks.
- Use "define" to explain concepts or terms.

Return only a Python list like: ["scrape", "summarize"]

Query: {query}
"""
)

# Chain setup
router_chain = routing_prompt | llm

def supervisor_agent(query: str) -> str:
    print(f"\n🤖 User query: {query}\n")

    # Ask LLM what to do
    plan_msg = router_chain.invoke({"query": query})
    plan_text = plan_msg.content.strip()

    print("🧠 Supervisor plan:\n", plan_text)

    # Extract action list
    match = re.search(r"\[(.*?)\]", plan_text)
    if not match:
        return f"❌ Couldn't parse supervisor plan: {plan_text}"

    try:
        plan = eval("[" + match.group(1) + "]")
    except Exception as e:
        return f"❌ Failed to evaluate plan list: {e}"

    print("\n📋 Executing plan:", plan)

    # Initial data to pass
    data = query
    for step in plan:
        print(f"\n🔧 Executing step: {step}")
        if step == "scrape":
            data = hybrid_scraper_worker(data)
        elif step == "summarize":
            data = summarizer_function(data)
        elif step == "translate":
            data = translator_function(data)
        elif step == "calculate":
            if len(data) > 500 or not any(c.isdigit() for c in data):
                print("⚠️ Skipping calculator — not a math query.")
                continue
            data = calculator_function(data)
        elif step == "define":
            data = define_function(data)
        else:
            return f"❌ Unknown step: {step}"

    return f"\n✅ Final Output:\n{data}"

# Entry point
if __name__ == "__main__":
    query = input("Enter your query: ")
    result = supervisor_agent(query)

    print("\n\n====== 🧾 FINAL STRUCTURED OUTPUT ======\n")

    if isinstance(result, dict):
        # Pretty printing the dictionary result
        if "topic" in result:
            print(f"🔍 Topic: {result['topic'].title()}")
        if "type" in result:
            print(f"📌 Type: {result['type'].capitalize()}")

        if "info" in result:
            print("\n💼 Basic Stock Info:")
            info = result["info"]
            print(f"• Market Cap      : ${info.get('market_cap'):,}")
            print(f"• P/E Ratio       : {info.get('pe_ratio')}")
            print(f"• Dividend Yield  : {info.get('dividend_yield') * 100:.2f}%")
            print(f"• CSV File Saved  : {info.get('csv_file')}")

        if "analysis" in result:
            print("\n📊 Stock Analysis Summary:")
            print(result["analysis"])

        if "scraped" in result:
            print("\n🌐 Scraped Info (from web):")
            print(result["scraped"].get("content", ""))

        if "summary" in result:
            print("\n📝 Summary:")
            print(result["summary"])

    else:
        print(result)

