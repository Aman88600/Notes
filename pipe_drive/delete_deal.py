import requests
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("api_key")
api_token = api_key
base_url = 'https://dion2.pipedrive.com/api/v1'

# ID of the deal you want to delete
deal_id = 11  # Replace with the actual deal ID

# Send DELETE request
url = f"{base_url}/deals/{deal_id}"
response = requests.delete(url, params={'api_token': api_token})

# Print the response
print(response.json())
