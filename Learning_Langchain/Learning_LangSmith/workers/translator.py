from langsmith.run_helpers import traceable
from langchain.schema import HumanMessage
from utils.model import get_llm

@traceable(name="Translation Worker")
def translate(text: str, language: str = "French") -> str:
    llm = get_llm()
    prompt = f"Translate this to {language}:\n\n{text}"
    return llm.invoke([HumanMessage(content=prompt)]).content
