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



# Replace with the actual record ID of the teacher you want to update
record_id = '996692000000458001'  # example ID

# Zoho CRM API endpoint for updating a record
url = f'https://www.zohoapis.in/crm/v2/Teachers/{record_id}'

# Data to update
data = {
    "data": [
        {
            "Name": "Aryan Singh (Updated)",
            "Salary": 3000,
            "Status": "Completed"
        }
    ]
}

# PUT request to update the record
response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())