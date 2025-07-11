from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
api_key = api_key 
# agent_runner.py
from tools.web_tool import web_scrape_tool
from groq_llm import GroqLLM  # Your existing Groq LLM wrapper
from langchain.agents import initialize_agent, AgentType

groq_llm = GroqLLM(api_key=api_key)

agent = initialize_agent(
    tools=[web_scrape_tool],
    llm=groq_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)

question = "Scrape the title and paragraph from https://en.wikipedia.org/wiki/Black_hole"
response = agent.run(question)
print("\n✅ Final Answer:\n", response)
