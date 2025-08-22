import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

# Replace with the actual activity ID you want to update
activity_id = 10

# Updated data for the activity
update_data = {
    'subject': 'Updated follow-up call with Apple',
    'due_date': '2025-09-03',
    'due_time': '15:00',
    'duration': '00:45',
    'note': 'Discuss updated Q4 strategy and budget',
}

# Construct the full URL with the activity ID
url = f"{base_url}/activities/{activity_id}"

# Make the PUT request to update the activity
response = requests.put(url, params={'api_token': api_token}, json=update_data)
data = response.json()

# Check for success
if data.get('success'):
    print("Activity updated:", data['data']['id'])
else:
    print("Failed to update activity:", data)
