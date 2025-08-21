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

success = models.execute_kw(
    db, uid, password,
    'res.partner', 'write',
    [[17], {'email': 'company4@example.com'}]
)
print("Update successful?", success)
