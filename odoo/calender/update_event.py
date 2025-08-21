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

event_id = 2  # Replace with your event's ID

updated_values = {
    'name': 'Updated Team Sync',
    'description': 'Updated agenda for the meeting.',
    # You can update other fields similarly, e.g. location, start, stop, etc.
}

models.execute_kw(
    db, uid, password,
    'calendar.event', 'write',
    [[event_id], updated_values]
)

print(f"Event with ID {event_id} has been updated.")
