# Making the state that will be carried thoughout the graph
from typing import TypedDict

# This is the state
class PortfolioState(TypedDict):
    amount_usd : float
    total_usd : float
    target_currency : str
    total : float


# Take the current usd, and convert it to the total usd
def calc_total_usd(state:PortfolioState) -> PortfolioState:
    state['total_usd'] = state['amount_usd'] * 1.08
    return state

# Convert total usd to inr
def convert_to_inr(state:PortfolioState) -> PortfolioState:
    state['total'] = state['total_usd'] * 80
    return state

# Convert total usd to euro
def convert_to_euro(state:PortfolioState) -> PortfolioState:
    state['total'] = state['total_usd'] * 0.85
    return state

# conditional edge funciton that will decide the target current and the next step of the graph
def choose_conversion(state: PortfolioState) -> str:
    return state["target_currency"]

# Making the graph
from langgraph.graph import StateGraph, START, END

builder = StateGraph(PortfolioState)

# Making nodels from funciton like add_node(node_name,function_name)

builder.add_node('calc_total_usd_node',calc_total_usd)
builder.add_node('convert_to_inr_node', convert_to_inr)
builder.add_node('convert_to_euro_node', convert_to_euro)


# Making the edges like this add_edge(starting_node, ending_node)
builder.add_edge(START, 'calc_total_usd_node')

# Here we have a condiotnal edge that works a bit diffrently, the first argument is the strting node, the second argument is the a function
builder.add_conditional_edges(
    "calc_total_usd_node", 
    choose_conversion,
    {
        "INR" : "convert_to_inr_node",
        "EUR" : "convert_to_euro_node"
    }
    )

builder.add_edge(["convert_to_inr_node", "convert_to_euro_node"], END)

# Compiling the graph
graph = builder.compile()

# making the graph image
from IPython.display import display, Image
image = (graph.get_graph().draw_mermaid_png())

# Saving it to decision_graph.png 
# with open("decison_graph.png", "wb") as file:
    # file.write(image)

# Running the graph
response = graph.invoke({"amount_usd" : 1000, "target_currency" : "EUR"})
print(response)
