from langsmith.run_helpers import traceable
from langchain.schema import HumanMessage
from utils.model import get_llm

@traceable(name="Calculator Worker")
def calculate(problem: str) -> str:
    llm = get_llm()
    prompt = f"Solve this math problem step-by-step:\n{problem}"
    return llm.invoke([HumanMessage(content=prompt)]).content
