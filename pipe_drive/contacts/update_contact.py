import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

# Replace with the actual person ID you want to update
person_id = 12

# Data you want to update
update_data = {
    'name': 'L Lawliet',  # Fix typo
    'email': 'l.lawliet@example.com',
    'phone': '9876543210'
}

# API URL for updating a person
url = f"{base_url}/persons/{person_id}"

# Send the PUT request
response = requests.put(
    url,
    params={'api_token': api_token},
    json=update_data
)

# Output the result
print(response.json())
