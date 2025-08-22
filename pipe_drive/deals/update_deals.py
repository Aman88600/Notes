import requests
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("api_key")
api_token = api_key
base_url = 'https://dion2.pipedrive.com/api/v1'

# Deal ID you want to update
deal_id = 12  # Replace with actual deal ID

# New values to update
update_payload = {
    'title': 'Updated Deal with Microsoft',
    'value': 2500000,
    'stage_id': 3,  # Move to a new stage
    'status': 'open'
}

# Send PUT request to update the deal
url = f"{base_url}/deals/{deal_id}"
response = requests.put(url, params={'api_token': api_token}, json=update_payload)

# Print the response
print(response.json())
