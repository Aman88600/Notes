from langsmith.run_helpers import traceable
from langchain.schema import HumanMessage
from utils.model import get_llm

@traceable(name="Summarization Worker")
def summarize(text: str) -> str:
    llm = get_llm()
    prompt = f"Summarize this text:\n\n{text}"
    return llm.invoke([HumanMessage(content=prompt)]).content
