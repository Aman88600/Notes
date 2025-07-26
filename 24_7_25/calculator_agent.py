from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.schema import AgentFinish

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",
)

# --- Safe Calculator ---
def safe_calculator(expression: str) -> str:
    """Safely evaluate basic math expressions."""
    try:
        # Use eval with restricted globals and locals
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"❌ Error evaluating expression: {e}"

# --- Define Calculator Tool ---
calculator_tool = Tool(
    name="Calculator",
    func=safe_calculator,
    description="Useful for solving math problems like '12 * 4' or '100 / (5 + 5)'.",
)

# --- Initialize Agent ---
calculator_agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

# --- Agent Wrapper Function ---
def calculator_worker_function(text: str) -> str:
    """Use the calculator agent if input looks like a math expression."""
    math_keywords = ["+", "-", "*", "/", "calculate", "of", "percent", "=", "sum", "product"]
    is_mathy = any(kw in text.lower() for kw in math_keywords) and any(c.isdigit() for c in text)

    if not is_mathy:
        return "🛑 Skipping calculator — no math-like expression detected."

    try:
        result = calculator_agent.invoke({"input": text})

        # Handle both return types
        if isinstance(result, AgentFinish):
            return result.return_values.get("output", "✅ Done, but no output.")
        elif isinstance(result, dict):
            return result.get("output", "✅ Agent completed, but output was empty.")
        else:
            return str(result)

    except Exception as e:
        return f"❌ Agent error: {e}"
