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
supervisor_prompt = PromptTemplate.from_template(
    """You are a task routing supervisor. Based on the user's query, choose the right tools to use.

Available actions: ["scrape", "summarize", "translate", "calculate", "define"]

Rules:
- Use "scrape" if fresh data, company info, or stock data is needed.
- Use "summarize" to condense content.
- Use "translate" for language conversion. If translation is required, also extract the target language if it's mentioned.
- Use "calculate" for math or numeric tasks.
- Use "define" to explain concepts or terms.

Return a Python dictionary like:
{{ 
  "actions": ["scrape", "translate"], 
  "translate_to": "German" 
}}

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