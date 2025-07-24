# Setting Up the state
from typing import TypedDict

class State(TypedDict):
    # We give the list of actions right here
    actions : list
    # If we get a language to translate to
    translate_to : str
    # To iterate thought the list of actions
    current_action : int
    # Did we reach the end of the list (can use different logic here)
    end_of_actions : bool


# Here we are making some nodes

# First we go to the super visor node function, so we need that
from supervisor import get_actions
def supervisor_function(state : State) -> State:
    # Getting the actions
    actions = get_actions()
    # Adding the variables to the state
    state['actions'] = actions['actions']
    state['translate_to'] = actions['translate_to']
    state['current_action'] = 0
    state['end_of_actions'] = False
    print(state)
    return state


# Importing classes required to set up the Graph
from langgraph.graph import StateGraph, START, END
# Setting up the builder
builder = StateGraph(State)

# Make node
builder.add_node("supervisor_node", supervisor_function)

# Make edges
builder.add_edge(START, "supervisor_node")
builder.add_edge("supervisor_node", END)


# Compiling the graph
graph = builder.compile()

# # making the graph image
# from IPython.display import display, Image
# image = (graph.get_graph().draw_mermaid_png())

# # save the graph image
# with open("supervisor_graph.png", "wb") as file:
#     file.write(image)


# Running the graph, finally
graph.invoke({})