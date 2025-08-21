from dotenv import load_dotenv
import os
import xmlrpc.client

# Load environment variables
load_dotenv()
env_email = os.getenv("email")
env_api = os.getenv("API")

# Odoo connection info
url = "https://dion.odoo.com"
db = "dion"
username = env_email
password = env_api

# Authenticate
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
if not uid:
    print("Authentication failed. Check credentials.")
    exit()
print(f"Authenticated with UID: {uid}")

# Connect to the object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

models_list = models.execute_kw(db, uid, password, 'ir.model', 'search_read', 
    [[['model', 'ilike', 'mail']]], 
    {'fields': ['model', 'name']}
)

print("\nAvailable 'mail' models:")
for m in models_list:
    print(f"{m['model']} - {m['name']}")