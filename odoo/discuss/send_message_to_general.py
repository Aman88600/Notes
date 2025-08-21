from dotenv import load_dotenv
import os
import xmlrpc.client

# Load .env credentials
load_dotenv()
username = os.getenv("email")
password = os.getenv("API")

url = "https://dion.odoo.com"
db = "dion"

# Authenticate
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
if not uid:
    print("Authentication failed")
    exit()

print("Authenticated with UID:", uid)

# Connect to models
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# Known Discuss channel ID (you said you're using discuss.channel_1)
channel_id = 1  # Update this if your real channel ID is different

# Post message
message_id = models.execute_kw(
    db, uid, password,
    'mail.message', 'create',
    [{
        'model': 'mail.channel',
        'res_id': channel_id,
        'body': '✅ Hello! This message was sent via the API.',
        'message_type': 'comment',
        'channel_ids': [(4, channel_id)]
    }]
)

print(f"Message posted with ID: {message_id}")
