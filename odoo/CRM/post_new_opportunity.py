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

new_lead_id = models.execute_kw(
    db, uid, password,
    'crm.lead', 'create',
    [{
        'name': 'Big Deal Opportunity',
        'partner_id': 5,  # optional: link to a contact
        'expected_revenue': 5000,
        'stage_id': 1,  # e.g., "New"
    }]
)