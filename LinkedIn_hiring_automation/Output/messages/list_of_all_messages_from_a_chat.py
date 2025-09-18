import requests
from dotenv import load_dotenv
load_dotenv()
import os
chat_id="gotwQGsgUEyomDo0MpfciQ"
url = f"https://{os.getenv("sub_domain")}.unipile.com:{os.getenv("port")}/api/v1/chats/{chat_id}/messages"

headers = {
    "X-API-KEY": os.getenv("x_api_key"),
    "accept": "application/json"
}


response = requests.get(url,  headers=headers)
print(response.status_code)
print(response.json()) 