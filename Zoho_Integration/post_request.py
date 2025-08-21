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

data = {
    "data": [
        {
            "Name": "Aryan Singh",
            "Phone_Number": "9876543210",
            "Salary": 2500,
            "User_1": {
                "id": "996692000000410001",  # Same user (Aman Basoya)
            },
            "Owner": {
                "id": "996692000000410001"
            },
            "Checkbox_1": True,
            "Decimal_1": 456.78,
            "Status": "Started",
            "Long_Integer_1": "9998887776",
            "Percent_1": 75,
            "Joining_Date": "2025-08-15",
            "Pick_List_1": "Option 1",
            "Number_1": 4321987,
            "Email_1": "riya.verma@example.com",
            "Date_Time_1": "2025-08-18T10:30:00+05:30",
            "Multi_Select_1": ["Option 1", "Option 2"],
            "URL_1": "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "Lookup_1": {
                "id": "996692000000429001"  # Assuming same lookup ID as example (Tyler Durden)
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
