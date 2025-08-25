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
url = 'https://www.zohoapis.in/crm/v2/JSONInvoices'

headers = {
    'Authorization': f'Zoho-oauthtoken {access_token}',
    'Content-Type': 'application/json'
}

data = {
    "data": 
    [
        {
            "Name": "API Invoice",
            "JSONInvoice Owner": {"id": "996692000000410001"},
            "Status": "Started",
            "Invoice Category" : "Text",
            "Sender Email Address" : "aman@gamil.com",
            "Invoice Details" : "Hello"
        }
    ]
}
    


response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
