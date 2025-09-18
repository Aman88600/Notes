import requests
from dotenv import load_dotenv
load_dotenv()
import os
url = f"https://{os.getenv("sub_domain")}.unipile.com:{os.getenv("port")}/api/v1/accounts"
headers = {
    "X-API-KEY": os.getenv("x_api_key"),
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Request failed with status code {response.status_code}")