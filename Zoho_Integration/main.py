import requests
import json

# Load access token from zoho_tokens.json or get it from your /tokens Flask endpoint
with open('zoho.json') as f:
    tokens = json.load(f)

access_token = tokens.get('access_token')

headers = {
    'Authorization': f'Zoho-oauthtoken {access_token}',
    'Content-Type': 'application/json'
}

# Zoho CRM API endpoint to insert a record into Contacts (you can replace with Students if custom module)
url = 'https://www.zohoapis.in/crm/v2/Teachers'

headers = {
    'Authorization': f'Zoho-oauthtoken {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
