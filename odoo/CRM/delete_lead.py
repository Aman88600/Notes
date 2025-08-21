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

# Lead ID to delete
lead_id = 8  # Replace with actual lead ID

# Delete the lead
success = models.execute_kw(
    db, uid, password,
    'crm.lead', 'unlink',
    [[lead_id]]
)

if success:
    print(f"Lead with ID {lead_id} deleted successfully!")
else:
    print("Failed to delete lead.")