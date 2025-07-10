# agent_runner.py
import os
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from groq_llm import GroqLLM

# Load API key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Define calculator tool
def calculator_tool(input: str) -> str:
    try:
        return str(eval(input))
    except Exception as e:
        return f"Error: {e}"

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for answering math questions like '47 * 91'."
    )
]

# ReAct-style prompt with example
prompt_template = PromptTemplate.from_template("""
You are an AI assistant that answers questions using tools.

You must strictly follow this format:

Question: the question to answer
Thought: what to do
Action: the tool to use (must be one of [Calculator])
Action Input: input for the tool

When you get the result:

Observation: the result from the tool
Thought: what you learned from the result
Final Answer: the final answer

Example:

Question: What is 2 * 5?
Thought: I need to multiply two numbers.
Action: Calculator
Action Input: 2 * 5

Observation: 10
Thought: I now know the final answer.
Final Answer: 10

Begin!

Question: {input}
""")

# Initialize LLM and chain
llm = GroqLLM(api_key=api_key)
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    llm_chain=llm_chain,
    verbose=True,
    handle_parsing_errors=True
)

# Run it
if __name__ == "__main__":
    question = "What is 47 * 91?"
    response = agent.run(question)
    print("\n✅ Final Answer:", response)
