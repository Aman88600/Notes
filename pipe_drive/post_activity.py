import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

url = f"{base_url}/activities"


activity_data = {
    'subject': 'Follow up call with Google',
    'type': 'call',                   # 'call', 'meeting', 'task', etc.
    'due_date': '2025-09-01',
    'due_time': '14:30',              # Optional
    'duration': '00:30',              # Optional
    'deal_id': 10,                   # Optional
    'person_id': 11,                   # Optional
    'note': 'Discuss Q4 budget',
}

response = requests.post(url, params={'api_token': api_token}, json=activity_data)
data = response.json()

if data.get('success'):
    print("Activity created:", data['data']['id'])
else:
    print("Failed to create activity:", data)
