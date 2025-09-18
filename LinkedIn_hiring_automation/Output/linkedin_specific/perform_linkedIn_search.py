import requests
from dotenv import load_dotenv
load_dotenv()
import os
url=f"https://{os.getenv("sub_domain")}.unipile.com:{os.getenv("port")}/api/v1/linkedin/search?account_id={os.getenv("account_id")}"

payload = {
    "api": "classic",
    "category": "people"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": os.getenv("x_api_key")
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)