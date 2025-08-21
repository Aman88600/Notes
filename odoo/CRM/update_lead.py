from dotenv import load_dotenv
import os
import xmlrpc.client

# Load credentials from .env
load_dotenv()
username = os.getenv("email")
password = os.getenv("API")

# Odoo config
url = "https://dion.odoo.com"
db = "dion"

# Authenticate
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
if not uid:
    print("❌ Authentication failed")
    exit()
print(f"✅ Authenticated with UID: {uid}")

# Connect to the object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

lead_id_to_update = 8  # Replace with an existing ID from the above list

updated_values = {
    'name': 'Updated Lead Name via API',
    'stage_id': 2,
    'expected_revenue': 10000,
}

result = models.execute_kw(
    db, uid, password,
    'crm.lead', 'write',
    [[lead_id_to_update], updated_values]
)

if result:
    print(f"Lead ID {lead_id_to_update} updated successfully!")
else:
    print("Update failed.")