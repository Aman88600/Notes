# We need TypeDict class to make the state
from typing import TypedDict
# We need StateGraph, START and END classes
from langgraph.graph import StateGraph, START, END

# This is the state variable
class PortfolioState(TypedDict):
    amount_usd : float
    total_usd : float
    total_inr : float

# These function are nodes
def clac_total(state: PortfolioState) -> PortfolioState:
    state['total_usd'] = state['amount_usd'] * 1.08
    return state

def convert_to_inr(state: PortfolioState) -> PortfolioState:
    state['total_inr'] = state['total_usd'] * 80
    return state


# Here we make the graph builder with ProtfolioState
builder = StateGraph(PortfolioState)

# Making nodes, we take functions and convert them to nodes
builder.add_node("calc_total_node", clac_total)
builder.add_node("convert_to_inr_node", convert_to_inr)

# Making Edges We connect the nodes to make edges
builder.add_edge(START, "calc_total_node")
builder.add_edge("calc_total_node", "convert_to_inr_node")
builder.add_edge("convert_to_inr_node", END)

# Compiling the graph
graph = builder.compile()

# Running the graph
response = graph.invoke({"amount_usd" : 1000})
print(response)