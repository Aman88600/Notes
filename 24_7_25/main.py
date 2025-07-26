# Setting Up the state
from typing import TypedDict
# Getting the workers
from web_scraper import hybrid_scraper_worker
from summarizer_worker import summarizer_function
from define_worker import define_function
from translation_worker import translator_worker_function
from calculator_agent import calculator_worker_function

class State(TypedDict):
    # We give the list of actions right here
    actions : list
    # If we get a language to translate to
    translate_to : str
    # To iterate thought the list of actions
    current_action : int
    # Did we reach the end of the list (can use different logic here)
    end_of_actions : bool
    # Getting the result
    result : str


# Here we are making some nodes

# First we go to the super visor node function, so we need that
from supervisor import get_actions
def supervisor_function(state : State) -> State:
    # Getting the actions
    user_input = input("Enter Your Query : ")
    actions = get_actions(user_input)
    # Adding the variables to the state
    state['actions'] = actions['actions']
    try:
        state['translate_to'] = actions['translate_to']
    except KeyError:
        state['translate_to'] = 'French'
    state['current_action'] = 0
    state['end_of_actions'] = False
    state['result'] = user_input
    print(state)
    return state

# Making the worker function(Dummys for now)
def scrapper(state: State) -> State:
    print("Scraping......")
    state_index = state['current_action']
    # Increment the state to go to the next state
    state_index += 1
    state['current_action'] = state_index
    query = state['result']
    state['result'] = hybrid_scraper_worker(query)
    return state

def translator_function(state: State) -> State:
    print("Translating......")
    state_index = state['current_action']
    # Increment the state to go to the next state
    state_index += 1
    state['current_action'] = state_index
    state['result'] = translator_worker_function(state['result'], state['translate_to'])
    return state

def sumarizzer_function(state: State) -> State:
    print("Sumarizzing......")
    state_index = state['current_action']
    # Increment the state to go to the next state
    state_index += 1
    state['current_action'] = state_index
    summary = summarizer_function(state['result'])
    state['result'] = summary
    return state

def definer_function(state: State) -> State:
    print("Defining......")
    state_index = state['current_action']
    # Increment the state to go to the next state
    state_index += 1
    state['current_action'] = state_index
    defined_text = define_function(state['result'])
    state['result'] = defined_text
    return state

def calculator_function(state: State) -> State:
    print("Calculating......")
    state_index = state['current_action']
    # Increment the state to go to the next state
    state_index += 1
    state['current_action'] = state_index
    state['result'] = calculator_worker_function(state['result'])
    return state


# We need a checker to see if we have reached the end of actions
def check_end_of_actions(state: State) -> State:
    # Checking if we have reached the end of the list
    list_length = len(state['actions'])
    index_of_action = state['current_action']
    if index_of_action == list_length:
        state['end_of_actions'] = True
    print(state['result'])
    return state

# Getting the action
def get_action_function(state: State) -> str:
    actions = state['actions']
    index = state['current_action']
    # Cheking if we have reached the end
    check_end_of_actions(state)
    if state['end_of_actions']:
        return 'end'
    return actions[index]

# Importing classes required to set up the Graph
from langgraph.graph import StateGraph, START, END
# Setting up the builder
builder = StateGraph(State)

# Make node
builder.add_node("supervisor_node", supervisor_function)
builder.add_node("scrapper_node", scrapper)
builder.add_node("sumarizzer_node", sumarizzer_function)
builder.add_node("translator_node",translator_function)
builder.add_node("definer_node", definer_function)
builder.add_node("calculator_node", calculator_function)

# Make edges
builder.add_edge(START, "supervisor_node")
builder.add_conditional_edges(
    "supervisor_node",
    get_action_function,
    {
        "scrape" : "scrapper_node",
        "summarize" : "sumarizzer_node",
        "translate" : "translator_node",
        "define" : "definer_node",
        "calculate" : "calculator_node",
        'end' : END
    }

)

builder.add_conditional_edges(
    "scrapper_node",
    get_action_function,
    {
        "summarize" : "sumarizzer_node",
        "translate" : "translator_node",
        "define" : "definer_node",
        "calculate" : "calculator_node",
        'end' : END
    }
)

builder.add_conditional_edges(
    "sumarizzer_node",
    get_action_function,
    {
        "scrape" : "scrapper_node",
        "translate" : "translator_node",
        "define" : "definer_node",
        "calculate" : "calculator_node",
        'end' : END
    }
)

builder.add_conditional_edges(
    "translator_node",
    get_action_function,
    {
        "scrape" : "scrapper_node",
        "summarize" : "sumarizzer_node",
        "define" : "definer_node",
        "calculate" : "calculator_node",
        'end' : END
    }
)

builder.add_conditional_edges(
    "definer_node",
    get_action_function,
    {
        "scrape" : "scrapper_node",
        "summarize" : "sumarizzer_node",
        "translate" : "translator_node",
        "calculate" : "calculator_node",
        'end' : END
    }
)

builder.add_conditional_edges(
    "calculator_node",
    get_action_function,
    {
        "scrape" : "scrapper_node",
        "summarize" : "sumarizzer_node",
        "translate" : "translator_node",
        "define" : "definer_node",
        'end' : END
    }
)
# builder.add_edge("supervisor_node", END)


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
