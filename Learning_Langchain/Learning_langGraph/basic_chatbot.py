# Getting the api key
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("GROQ_API_KEY")

# making the groq LLM
from langchain_groq import ChatGroq

llm = ChatGroq(groq_api_key = api_key,
         model_name="llama3-8b-8192")

# response = llm.invoke("What is the speed of light?")
# text = response.content

# Making the state that the chatbot is going to use
from typing import TypedDict

class State(TypedDict):
    conversation: list
    exit_conversation : bool


# This funciton will act as the chat bot node
def chat_response(state: State) -> State:
    user_query = input("Enter Anyting : ")
    if user_query == 'exit':
        state["exit_conversation"] = True
    else:
        response = llm.invoke(user_query)
        text = response.content
        state['conversation'].append(text)
        state["exit_conversation"] = False
        print(f"list = {state['conversation']}")
        print(text)
    return state

# Checking to keep going or not
def keep_chatting(state: State) -> bool:
    return state["exit_conversation"]
    


# Makinf the graph
from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)

# Making the nodes
builder.add_node("chat_response_node",chat_response)

# Making the edges the important part
builder.add_edge(START, "chat_response_node")
builder.add_conditional_edges(
    "chat_response_node", 
    keep_chatting,
    {
        True : END,
        False : "chat_response_node"
    }
)

graph = builder.compile()

# making the graph image
# from IPython.display import display, Image
# image = (graph.get_graph().draw_mermaid_png())

# save the graph image
# with open("basic_chatbot_graph.png", "wb") as file:
    # file.write(image)

# running the bot/ graph
graph.invoke({"conversation" : [], "exit_conversation" : False})

