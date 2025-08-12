from typing import TypeDict
from langgraph.graph import StateGraph, START, END

class State(TypeDict):
    greeting : str

def say_hello(state:State) -> State:
    state['greeting'] = "Hello"
    return state

builder = StateGraph(State)

builder.add_node("say_hello", say_hello)

builder.add_edge(START, "say_hello")
builder.add_edge("say_hello", END)

graph = builder.compile()

# making the graph image
from IPython.display import display, Image
image = (graph.get_graph().draw_mermaid_png())

# save the graph image
with open("supervisor_graph.png", "wb") as file:
    file.write(image)

