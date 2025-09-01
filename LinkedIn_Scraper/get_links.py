from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pyautogui
import pyperclip
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import csv






opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8000")

service = Service(executable_path="C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe")
# Create a new Chrome browser instance using Service
driver = webdriver.Chrome(service=service, options=opt)

def get_all_data(link):
    name = link.split("/")[-1]
    # opening the ID
    link = link
    driver.get(link)

    # Give time for Chrome to open and the extension to load
    time.sleep(5)

    # positions
    # chrome (512, 738)
    # extention (1256, 69)
    # Click Chrome
    pyautogui.click(512, 738)
    time.sleep(2)
    # Click Extentions
    pyautogui.click(1244, 68)
    time.sleep(2)
    # Select easy scraper
    pyautogui.click(1023, 210)
    time.sleep(20)
    # Copy Data
    pyautogui.click(678, 278)
    time.sleep(2)
    # Close the extention window
    pyautogui.click(711, 34)
    time.sleep(2)
    # come back to vs code
    pyautogui.click(455, 762)

    # Get the current content of the clipboard
    clipboard_content = pyperclip.paste()
    print("Clipboard content:", clipboard_content)


    # load_dotenv()
    # api_key = os.getenv("groq_api")

    # llm = ChatGroq(
    #     groq_api_key=api_key,
    #     model_name="llama-3.1-8b-instant",
    # )

    # # Prompt for summarization
    # summarize_prompt = PromptTemplate.from_template(
    #     "Please arrang the following content in a concise and clear way in json format:\n\n{content}"
    # )

    # summarizer_chain = summarize_prompt | llm

    # def summarizer_function(content: str) -> str:
    #     """Summarizes the given content."""
    #     try:
    #         result = summarizer_chain.invoke({"content": content})
    #         return result.content.strip()
    #     except Exception as e:
    #         return f"❌ Error during summarization:{e}"
        

    text = clipboard_content
    # output = summarizer_function(text)
    # print(output)
    file=open(f"full_ids/{name}.txt", "w", encoding='utf-8')
    file.write(text)
    file.close()



# Open the CSV file
with open('Partial_ids/google.csv', mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Loop through the rows in the CSV
    scrape_lock = True
    for row in csv_reader:
        if "http" in row[0]:
            print(row[0])
            if "https://in.linkedin.com/in/karthikeyan-" in row[0]:
                scrape_lock = False
            if scrape_lock:
                pass
            else:
                get_all_data(row[0])