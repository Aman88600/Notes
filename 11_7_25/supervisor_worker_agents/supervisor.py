# supervisor.py
import os
from dotenv import load_dotenv
from groq_llm import GroqLLM
from worker import worker_task

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
llm = GroqLLM(api_key=api_key)

def supervisor_task(main_question: str):
    planning_prompt = f"""You are a supervisor AI. Break down the task and explain what the worker should do.

Task: {main_question}

Give clear instructions in a single sentence.
"""
    instruction = llm._call(planning_prompt)

    print("\n👨‍💼 Supervisor says:", instruction)

    result = worker_task(instruction)
    print("\n👷 Worker response:", result)

if __name__ == "__main__":
    user_question = "Summarize the benefits of using solar energy."
    supervisor_task(user_question)
