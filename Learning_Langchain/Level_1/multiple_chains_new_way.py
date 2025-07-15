from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

# Loading the .env file
load_dotenv()

# Getting the API key
api_key = os.getenv("GROQ_API_KEY")

# making an object(llm) using the ChatGroq class
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",  # or 70b if you want
)


# 1 Summary Chain

summary_template = "Summarize the follwing:\n\n{text}"
summary_prompt = PromptTemplate.from_template(summary_template)
# summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
summary_chain = summary_prompt | llm

# 2 Translation chain
# Making the prompt using the from_template() method
translate_template = "Translate this into French:\n\n{text}"
translate_prompt = PromptTemplate.from_template(translate_template)


# making the chain using the LLMChain class
# translate_chain = LLMChain(llm=llm, prompt=translate_prompt)
translate_chain = translate_prompt | llm


summary = summary_chain.invoke({"text": "A black hole is a massive, compact astronomical object so dense that its gravity prevents anything from escaping, even light. Albert Einstein's theory of general relativity predicts that a sufficiently compact mass will form a black hole.[4] The boundary of no escape is called the event horizon. A black hole has a great effect on the fate and circumstances of an object crossing it, but has no locally detectable features according to general relativity.[5] In many ways, a black hole acts like an ideal black body, as it reflects no light.[6][7] Quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional to its mass. This temperature is of the order of billionths of a kelvin for stellar black holes, making it essentially impossible to observe directly."})
print(summary.content)

translation = translate_chain.invoke({"text" : summary.content})
print(translation.content)
# Combining the two chains
# overall_chain = SimpleSequentialChain(chains=[summary_chain, translate_chain], verbose=True)
# overall_chain = summary_chain | translate_chain

# using the invoke() method to get the response
# response = overall_chain.invoke({"text":"LangChain lets you build LLM apps by linking prompts, memory, tools, and models together."})

# Prithind the response
# print(response)
