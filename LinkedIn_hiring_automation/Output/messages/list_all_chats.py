import requests
from dotenv import load_dotenv
load_dotenv()
import os

url = f"https://{os.getenv("sub_domain")}.unipile.com:{os.getenv("port")}/api/v1/chats"

headers = {
    "X-API-KEY": os.getenv("x_api_key"),
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

print(response.text)