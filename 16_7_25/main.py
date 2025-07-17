from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from web_scraper_worker import web_scraper_function
from calculator_agent import calculator_function
from summarizer import summarizer_function
from translator_worker import translator_function
from define_worker import define_function

from langchain_core.runnables import RunnableSequence
import re

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# LLM setup
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

# Prompt for routing
routing_prompt = PromptTemplate.from_template(
    """You are a task routing supervisor. Given a user's query, determine the exact sequence of required steps.

Available actions: ["scrape", "summarize", "translate", "calculate", "define"]

Instructions:
- Use "calculate" only if there's math or numeric intent (e.g., 'What is 15% of 200?').
- Use "scrape" only if you need to extract fresh info from the web.
- Use "summarize" for condensing content.
- Use "translate" for language conversion.
- Use "define" for explanations or definitions.

Return a Python list of actions (e.g., ["scrape", "summarize", "define"]) — nothing more.

Query: {query}
"""
)



# Modern replacement for deprecated LLMChain
router_chain = routing_prompt | llm

# Supervisor agent
def supervisor_agent(query):
    # Get plan
    plan_msg = router_chain.invoke({"query": query})
    plan_text = plan_msg.content if hasattr(plan_msg, "content") else str(plan_msg)

    print("🧠 Supervisor plan:\n", plan_text)

    # Extract list like ["scrape", "summarize"]
    match = re.search(r"\[(.*?)\]", plan_text)
    if not match:
        return f"❌ Couldn't parse the supervisor's plan: {plan_text}"
    
    try:
        plan = eval("[" + match.group(1) + "]")
    except Exception as e:
        return f"❌ Failed to evaluate plan list: {e}"

    print("\n📋 Executing plan:", plan)

    data = query
    for step in plan:
        print(f"\n🔧 Executing step: {step}")
        if step == "scrape":
            data = web_scraper_function(topic=data)
        elif step == "summarize":
            data = summarizer_function(data)
        elif step == "translate":
            data = translator_function(data)
        elif step == "calculate":
            # Prevent sending large text blocks like scraped data
            if len(data) > 500 or not any(char.isdigit() for char in data):
                print("🔢 Skipping calculator — not a math query.")
                continue
            data = calculator_function(data)
        elif step == "define":
            data = define_function(data)
        else:
            return f"❌ Unknown action: {step}"
    
    return f"\n🧾 Final Output:\n{data}"


# ==== Entry Point ====
if __name__ == "__main__":
    query = input("Enter your question: ")
    output = supervisor_agent(query)
    print(output)
