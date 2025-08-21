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

# Choose a specific pipeline stage (you can change this)
target_stage_id = 1

# Fetch CRM leads in this stage
leads = models.execute_kw(
    db, uid, password,
    'crm.lead', 'search_read',
    [[['stage_id', '=', target_stage_id]]],
    {'fields': ['name', 'stage_id', 'expected_revenue', 'user_id', 'probability']}
)

# Display results
if not leads:
    print(f"No leads found in stage ID {target_stage_id}")
else:
    print(f"\n📌 Leads in stage ID {target_stage_id}:\n")
    for lead in leads:
        print(f"ID: {lead['id']}")
        print(f"Name: {lead['name']}")
        print(f"Stage ID: {lead['stage_id']}")
        print(f"Expected Revenue: {lead['expected_revenue']}")
        print(f"Assigned To: {lead.get('user_id', [''])[1] if lead.get('user_id') else 'Unassigned'}")
        print(f"Probability: {lead.get('probability', 0)}%")
        print("-" * 40)
