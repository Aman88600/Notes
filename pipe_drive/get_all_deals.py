import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("api_key")

# Base API URL
base_url = 'https://dion2.pipedrive.com/api/v1'
endpoint = f'{base_url}/deals'

# Store all deals
all_deals = []

# Pagination
start = 0
limit = 100
more_items = True

while more_items:
    response = requests.get(endpoint, params={
        'api_token': api_key,
        'start': start,
        'limit': limit
    })

    if response.status_code != 200:
        print("Error fetching deals:", response.status_code, response.text)
        break

    data = response.json()

    if data.get('data') is None:
        print("No deals found or unexpected response structure.")
        break

    all_deals.extend(data['data'])

    # Safely access pagination data
    pagination = data.get('additional_data', {}).get('pagination', {})
    more_items = pagination.get('more_items_in_collection', False)
    start = pagination.get('next_start', None)

    # Exit if next_start is not provided
    if start is None:
        break

# Output
print(f"\nTotal deals retrieved: {len(all_deals)}\n")
for deal in all_deals:
    print(f"Deal ID: {deal['id']}, Title: {deal['title']}, Value: {deal['value']}, Status: {deal['status']}")
