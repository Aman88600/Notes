import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

person_data = {
    'name': 'L Lawlite',
    'email': 'john.doe@example.com',
    'phone': '1234567890',
    'org_id': 6  # Optional, if they're linked to an organization
}

response = requests.post(
    f"{base_url}/persons",
    params={'api_token': api_token},
    json=person_data
)

print(response.json())
