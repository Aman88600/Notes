# This is the Documentation of Multi Agent Model

## 1 Objective

- The Objective is to make a supervisor and worker model using LangGraph, In which the supervisor can use multiple worker e.g. scraper, summarizer, or transator, according to the user needs.

## 2 Achievement
- The model that is built so far, can scrape data about companies subjects and other topics as well as data about company stocks
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Stocks_output.PNG?raw=true)

- The Langgraph's graph
![alt text](https://github.com/Aman88600/Notes/blob/main/24_7_25/supervisor_graph.png?raw=true)

## 3 What did not work

### 1 Making a RAG model in order to reterive data
- In initial plan was to make a vecotor data base where the workers like summarizer and definer can reterive data from, but since it was taking too long to make the vector data base using the hugging face embeddings and chroma db, there for it was not used


### 2 Trying to use list or dictionary for traslation
- With the translation worker I ran into a problem which was the language it should translate to (By default it translates to french), but, I tried giving, it as a list in list or dictionay in list and tried to tell the language with the translation, but it did not worked, because the supervisor does the jobs step by step

### 3 Asking the user the language before transation
- Now the translator asks the user before execution, which language it should, convert the text to.
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/translator_in_action.PNG?raw=true)


### 4 Using simple encoding without error handling
- with open("web_scraper_output.txt", "w") as file:
-       file.write(str(result['scraped']['content']))
- This causes errors somtimes like the following:
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/encoding_error.PNG?raw=true)

### 5 Using previous prompt that was giving wrong instructions
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


## 4 What Worked

### 1 Using a simple text file
- Using a text file to store the output from the web scraper and then using that text file to give data to the summarizer and the definer is what worker it was fast

### 2 Using a better prompt and better techniques

- 1. First the prompt used for LLM was made
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

- 2. We get a big output of string that includes the dictionay we need, so we extract the dictionary using this
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

- 3. The we get the actions list from the dictionary as before but there is also the key 'translate_to' and the value is the language that we put in the translator
language = required_dict['translate_to']
print("Translating....")
data = translator_function(data, language)

### 3 Using a better encoding method + error handling

- We used the following technique to stop the error from happening and catch it and give a replace character if the character is unknown

![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/better_encoding.PNG?raw=true)

### 4 Using Newer better prompt
- This prompt does not give us the translate step if not specified
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

## 5 Final Outputs

- Final output for some prompts

- Prompt : Tell me about the Apple comapany

![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Stocks_output.PNG?raw=true)

- Prompt : Tell me about Apple Stocks
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Getting_apple_stocks.PNG?raw=true)

- Prompt : Scrape and define philosphy
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/scrape_and_define.PNG?raw=true)