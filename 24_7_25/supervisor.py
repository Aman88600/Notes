# Getting the API key
from dotenv import load_dotenv
import os
# Setting up groq llm
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key = api_key,
    model_name="llama3-8b-8192"
)

# Making a prompt template for the supervisor model
from langchain.prompts import PromptTemplate

supervisor_prompt = PromptTemplate.from_template(
    """You are a task routing supervisor. Based on the user's query, choose the appropriate actions.

Available actions: ["scrape", "summarize", "translate", "calculate", "define"]

Rules:
- Use "scrape" if the query asks for current data, company info, news, or stock information.
- Use "summarize" to shorten or condense long content.
- Use "translate" only if the user explicitly requests translation **to a specific language** (e.g., "Translate to German").
- ❗️If the query includes the word "translate" but does **not specify a target language**, DO NOT include "translate" or "translate_to". Never assume or guess a language.
- Use "calculate" if the user asks for a computation, arithmetic, or math.
- Use "define" if the user wants a definition or explanation of a term.

Output format:
- Always return a Python dictionary with an "actions" list.
- Only include "translate_to" if "translate" is in the actions AND the target language is explicitly stated.

Examples:
Query: "Tell me about Tesla and translate to German"
→ {{
  "actions": ["scrape", "translate"],
  "translate_to": "German"
}}

Query: "Tell me about Apple and translate to"
→ {{
  "actions": ["scrape"]
}}

Query: "Summarize this and define it"
→ {{
  "actions": ["summarize", "define"]
}}

Query: "What's 5 * 5?"
→ {{
  "actions": ["calculate"]
}}

Query: "Translate this"
→ {{
  "actions": []
}}

Now process this query and return ONLY the dictionary — no explanation, no comments, and no text outside the dictionary.
Query: {query}
"""
)


supervisor_model = supervisor_prompt | llm

def get_actions(user_input) -> dict:
    """
    This function Does not take any inputs
    It gives the output of the required dictionary
    """
    # Getting user input
    
    plan_msg = supervisor_model.invoke({"query" : user_input})

    # Refinig the output to get the dictionary out of it
    content = plan_msg.content
    do_print = False
    required_dict = ""
    for i in content:
        if i == "{":
            do_print = True
        if do_print:
            required_dict += i
        if i == "}":
            do_print = False
    required_dict = eval(required_dict)

    # checking thw required_dict
    return required_dict

# For individual testing
if __name__ == "__main__":
    user_input = input("Enter Your Query : ")
    print(get_actions(user_input))