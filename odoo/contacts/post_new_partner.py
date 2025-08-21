from dotenv import load_dotenv
import os

load_dotenv()
env_email = os.getenv("email")    
env_api = os.getenv("API")

import xmlrpc.client

# Odoo server info
url = "https://dion.odoo.com"
db = "dion"
username = env_email  # Replace with your Odoo email
password = env_api      # Replace with your API key

# Authenticate
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})

if not uid:
    print("Authentication failed. Check your credentials.")
    exit()

print("Authenticated as UID:", uid)

# Connect to the object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

new_partner_id = models.execute_kw(
    db, uid, password,
    'res.partner', 'create',
    [{
        'name': 'Company 4',
        'email': 'company2test@example.com',
        'company_type': 'company'  # or 'person'
    }]
)
print("New partner created with ID:", new_partner_id)
