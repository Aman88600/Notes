import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

# Replace with the actual person ID you want to delete
person_id = 12

# Build the URL for deletion
url = f"{base_url}/persons/{person_id}"

# Send DELETE request
response = requests.delete(
    url,
    params={'api_token': api_token}
)

# Print result
data = response.json()
if data.get('success'):
    print(f"Person {person_id} deleted successfully.")
else:
    print("Failed to delete person:", data)
