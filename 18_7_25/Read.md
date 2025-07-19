# This is the Documentation of Multi Agent Model

## 1 Objective

- The Objective is to make a supervisor and worker model using LangChain, In which the supervisor can use multiple worker e.g. scraper, summarizer, or transator, according to the user needs.

## 2 Achievement
- The model that is built so far, can scrape data about companies subjects and other topics as well as data about company stocks
![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Stocks_output.PNG?raw=true)

## 3 What did not work

### 1 Making a RAG model in order to reterive data
- In initial plan was to make a vecotor data base where the workers like summarizer and definer can reterive data from, but since it was taking too long to make the vector data base using the hugging face embeddings and chroma db, there for it was not used

## 4 What Worked

### 1 Using a simple text file
- Using a text file to store the output from the web scraper and then using that text file to give data to the summarizer and the definer is what worker it was fast

## 5 Final Outptu

- Final output for some prompts

- Prompt : Tell me about the Apple comapany

![alt text](https://github.com/Aman88600/Notes/blob/main/18_7_25/Images/Stocks_output.PNG?raw=true)
