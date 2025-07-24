from dotenv import load_dotenv
load_dotenv()

from workers.summarizer import summarize
from workers.translator import translate
from workers.calculator import calculate

from langsmith.run_helpers import traceable

@traceable(name="Supervisor")
def supervisor(query: str):
    if "summarize" in query.lower():
        content = query.split("summarize", 1)[-1].strip()
        return summarize(content)
    elif "translate" in query.lower():
        content = query.split("translate", 1)[-1].strip()
        return translate(content)
    elif "calculate" in query.lower():
        content = query.split("calculate", 1)[-1].strip()
        return calculate(content)
    else:
        return "Sorry, I don't know how to handle this request."

if __name__ == "__main__":
    while True:
        user_input = input("\n👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("🤖", supervisor(user_input))
