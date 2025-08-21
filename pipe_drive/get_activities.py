import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("api_key")
base_url = 'https://dion2.pipedrive.com/api/v1'

url = f"{base_url}/activities"

params = {
    'api_token': api_token,
    'user_id': None,         # Optional: filter by user
    'done': 0,               # 0 = not done, 1 = done
    'start': 0,
    'limit': 100
}

response = requests.get(url, params=params)
data = response.json()

if data.get('success'):
    for activity in data['data']:
        print(f"{activity['id']}: {activity['subject']} - {activity['type']} on {activity['due_date']}")
else:
    print("Failed to fetch activities:", data)
