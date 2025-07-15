from dotenv import load_dotenv
import os
from groq_llm import GroqLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
groq_llm = GroqLLM(api_key=api_key)

# Definig the prompt
prompt = PromptTemplate(
    input_variables = ["sentence"],
    template = "Rephrase the following sentense : {sentence}"
)

user_input = input("Enter any sentense : ")

final_prompt = prompt.format(sentence=user_input)

output = groq_llm.invoke(final_prompt)

print(output)