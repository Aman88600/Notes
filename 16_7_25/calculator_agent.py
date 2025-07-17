from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# LLM setup
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",
)

# Safe custom calculator
def safe_calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"❌ Error: {e}"

# Define calculator tool
calculator_tool = Tool(
    name="Calculator",
    func=safe_calculator,
    description="Useful for solving math problems like '12 * 4' or '100 / (5 + 5)'"
)

# Set up agent
calculator_agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

from langchain.schema import AgentFinish

def calculator_function(text: str) -> str:
    """Evaluate math if text looks like a math expression."""
    math_keywords = ["calculate", "+", "-", "*", "/", "=", "of", "percent", "sum", "product"]
    
    if not any(kw in text.lower() for kw in math_keywords) and not any(c.isdigit() for c in text):
        return "🛑 Skipping calculator — no math expression detected."

    try:
        # Run with intermediate steps to monitor loop
        result = calculator_agent.invoke({"input": text})

        # If the final output is an AgentFinish, extract it
        if isinstance(result, AgentFinish):
            return result.return_values.get("output", "✅ Done, but no output.")
        
        return result.get("output", "✅ Agent completed, but output was empty.")
    
    except Exception as e:
        return f"❌ Agent error: {e}"
