import requests
from dotenv import load_dotenv
load_dotenv()
import os
chat_id="gotwQGsgUEyomDo0MpfciQ"
url=f"https://{os.getenv("sub_domain")}.unipile.com:{os.getenv("port")}/api/v1/chats/{chat_id}/messages"

headers = {
    "X-API-KEY": os.getenv("x_api_key"),
    "accept": "application/json"
}

# Body data from Postman
data = {
    'text' : "Hello, Friend Happy Birthday!"
}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Check the response
print(response.status_code)  # To see if the request was successful
print(response.json()) 