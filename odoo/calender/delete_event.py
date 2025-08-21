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

event_id = 2  # Replace with the actual event ID you want to delete

result = models.execute_kw(
    db, uid, password,
    'calendar.event', 'unlink',
    [[event_id]]
)

if result:
    print(f"Event with ID {event_id} was successfully deleted.")
else:
    print(f"Failed to delete event with ID {event_id}.")
