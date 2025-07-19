# This is the Documentation of Multi Agent Model

## 1 Objective

- The Objective is to make a supervisor and worker model using LangChain, In which the supervisor can use multiple worker e.g. scraper, summarizer, or transator, according to the user needs.

## 2 Achievement
- The model that is built so far, can scrape data about companies subjects and other topics as well as data about company stocks
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Stocks_output.PNG?raw=true)

## 3 What did not work

### 1 Making a RAG model in order to reterive data
- In initial plan was to make a vecotor data base where the workers like summarizer and definer can reterive data from, but since it was taking too long to make the vector data base using the hugging face embeddings and chroma db, there for it was not used


### 2 Trying to use list or dictionary for traslation
- With the translation worker I ran into a problem which was the language it should translate to (By default it translates to french), but, I tried giving, it as a list in list or dictionay in list and tried to tell the language with the translation, but it did not worked, because the supervisor does the jobs step by step

## 4 What Worked

### 1 Using a simple text file
- Using a text file to store the output from the web scraper and then using that text file to give data to the summarizer and the definer is what worker it was fast

### 2 Asking the user the language before transation
- Now the translator asks the user before execution, which language it should, convert the text to.
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/translator_in_action.PNG?raw=true)

## 5 Final Outputs

- Final output for some prompts

- Prompt : Tell me about the Apple comapany

![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Stocks_output.PNG?raw=true)

- Prompt : Tell me about Apple Stocks
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Getting_apple_stocks.PNG?raw=true)

- Prompt : Scrape and define philosphy
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/scrape_and_define.PNG?raw=true)