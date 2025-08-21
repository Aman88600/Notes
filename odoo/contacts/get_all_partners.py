from dotenv import load_dotenv
import os
import xmlrpc.client

# Load environment variables
load_dotenv()
env_email = os.getenv("email")
env_api = os.getenv("API")

# Odoo server info
url = "https://dion.odoo.com"
db = "dion"
username = env_email
password = env_api

# Authenticate
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})

if not uid:
    print("Authentication failed. Check your credentials.")
    exit()

print("Authenticated as UID:", uid)

# Connect to the object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# Create a new partner (optional)
new_partner_id = models.execute_kw(
    db, uid, password,
    'res.partner', 'create',
    [{
        'name': 'Company 4',
        'email': 'company2test@example.com',
        'company_type': 'company'
    }]
)
print("New partner created with ID:", new_partner_id)

# Get list of all partners
partners = models.execute_kw(
    db, uid, password,
    'res.partner', 'search_read',
    [[]],  # Empty domain = all records
    {
        'fields': ['id', 'name', 'email', 'company_type'],  # Specify fields you want
        'limit': 100  # Optional: limit the number of records
    }
)

# Print the list of partners
for partner in partners:
    print(partner)
