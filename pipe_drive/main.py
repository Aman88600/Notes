import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

api_token = api_key
base_url = 'https://dion2.pipedrive.com/api/v1'

url = f"{base_url}/deals"
payload = {
    'title': 'New Deal with SONY',
    'value': 2000000,
    'currency': 'INR',
    'user_id': 26022355,  # Your user ID
    'org_id': 6,          # Org ID (optional)
    'person_id': 9,       # Person ID (optional)
    'stage_id': 1,        # Qualified stage
    'expected_close_date': '2025-09-15',
    'status': 'open'
}
response = requests.post(url, params={'api_token': api_token}, json=payload)
print(response.json())
