from dotenv import load_dotenv
import os
import xmlrpc.client

# Load environment variables from .env file
load_dotenv()
env_email = os.getenv("email")
env_api = os.getenv("API")

# Odoo server info
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

# Example: get a partner ID to add as attendee
partners = models.execute_kw(
    db, uid, password,
    'res.partner', 'search_read',
    [[['email', '!=', False]]],  # Example filter: partners with an email
    {'fields': ['id', 'name'], 'limit': 1}
)

if not partners:
    print("No partners found to add as attendees.")
    partner_id = False
else:
    partner_id = partners[0]['id']
    print(f"Using partner ID {partner_id} as attendee.")

# Optional: create a reminder (example)
# You would typically know reminder IDs or create them beforehand
# For simplicity, assuming no reminders here
reminder_id = None  # Or an integer ID of a reminder if you have one

# Prepare partner_ids in the expected format (many2many)
partner_ids = [[6, 0, [partner_id]]] if partner_id else []

# Create calendar event
event_data = {
    'name': 'Knowledge Transfer',
    'start': '2025-08-21 09:00:00',
    'stop': '2025-08-21 10:00:00',
    'partner_ids': partner_ids,
    'description': 'Weekly team synchronization meeting.',
    'location': 'Conference Room B',
    'allday': False,
    'duration': 1.0,
    'privacy': 'public',
    # 'recurrence': 'weekly',  # REMOVE this line
}

# Add reminders if you have reminder_id
if reminder_id:
    event_data['reminder_ids'] = [(4, reminder_id)]

new_event_id = models.execute_kw(
    db, uid, password,
    'calendar.event', 'create',
    [event_data]
)

print(f"New calendar event created with ID: {new_event_id}")
