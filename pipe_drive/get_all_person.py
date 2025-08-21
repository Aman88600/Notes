import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_token = os.getenv("api_key")

# Base URL for your Pipedrive instance
base_url = 'https://dion2.pipedrive.com/api/v1'

# Endpoint to get all persons
url = f"{base_url}/persons"

# Optional: Pagination (start = 0, limit = 100)
params = {
    'api_token': api_token,
    'start': 0,
    'limit': 100  # You can go up to 500 per request
}

all_persons = []

while True:
    response = requests.get(url, params=params)
    data = response.json()

    if not data.get('success'):
        print("Failed to fetch persons:", data)
        break

    persons = data['data']
    if not persons:
        break

    all_persons.extend(persons)

    # Pagination: check if there's more data
    pagination = data.get('additional_data', {}).get('pagination', {})
    if not pagination.get('more_items_in_collection'):
        break

    params['start'] = pagination['next_start']

# Print results
for person in all_persons:
    print(f"{person['id']}: {person['name']} - {person.get('email')}")

# Optional: total count
print(f"\nTotal persons fetched: {len(all_persons)}")
