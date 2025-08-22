import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

# Replace with the actual activity ID you want to delete
activity_id = 10

# Construct the URL for deleting the activity
url = f"{base_url}/activities/{activity_id}"

# Make the DELETE request
response = requests.delete(url, params={'api_token': api_token})
data = response.json()

# Check response
if data.get('success'):
    print(f"Activity {activity_id} deleted successfully.")
else:
    print("Failed to delete activity:", data)
