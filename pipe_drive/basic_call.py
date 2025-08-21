import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

api_token = api_key
base_url = 'https://dion2.pipedrive.com/api/v1'

response = requests.get(f'{base_url}/deals', params={'api_token': api_token})

print(response.json())
