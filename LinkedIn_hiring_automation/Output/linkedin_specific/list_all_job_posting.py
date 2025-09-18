import requests
from dotenv import load_dotenv
load_dotenv()
import os
url=f"https://{os.getenv("sub_domain")}.unipile.com:{os.getenv("port")}/api/v1/linkedin/jobs?account_id={os.getenv("account_id")}"

headers = {
    "accept": "application/json",
    "X-API-KEY": os.getenv("x_api_key")
}

response = requests.get(url, headers=headers)

print(response.text)