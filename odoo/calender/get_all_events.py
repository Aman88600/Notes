from dotenv import load_dotenv
import os
import xmlrpc.client

# Load environment variables
load_dotenv()
env_email = os.getenv("email")
env_api = os.getenv("API")

# Odoo connection details
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

print(f"Authenticated as UID: {uid}")

# Connect to object endpoint
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# Fetch all calendar events (use search_read with no domain to get all)
events = models.execute_kw(
    db, uid, password,
    'calendar.event', 'search_read',
    [[]],  # empty domain = all records
    {'fields': ['id', 'name', 'start', 'stop', 'partner_ids', 'location', 'description'], 'limit': 100}
)

print(f"Found {len(events)} events:")
for event in events:
    print(f"ID: {event['id']}, Name: {event['name']}, Start: {event['start']}, Stop: {event['stop']}, Location: {event.get('location')}")
