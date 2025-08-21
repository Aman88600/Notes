from dotenv import load_dotenv
import os
import requests
import json
# Load .env variables
load_dotenv()

# Safely fetch environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")  # typo fixed here


from flask import Flask, redirect, request
import requests
import os

app = Flask(__name__)

CLIENT_ID = client_id
CLIENT_SECRET = client_secret
REDIRECT_URI = 'http://localhost:8000/oauth/callback'
AUTH_URL = 'https://accounts.zoho.in/oauth/v2/auth'
TOKEN_URL = 'https://accounts.zoho.in/oauth/v2/token'

@app.route('/')
def home():
    # Redirect user to Zoho OAuth authorization page
    params = {
        'scope': 'ZohoCRM.modules.ALL',
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'access_type': 'offline',
        'redirect_uri': REDIRECT_URI
    }
    url = requests.Request('GET', AUTH_URL, params=params).prepare().url
    return redirect(url)

@app.route('/oauth/callback')
def oauth_callback():
    code = request.args.get('code')
    if not code:
        return 'Authorization code not found in request.', 400
    
    # Exchange authorization code for access and refresh tokens
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code
    }
    token_response = requests.post(TOKEN_URL, data=data)
    tokens = token_response.json()
    # Save tokens to JSON file (overwrite)
    with open("zoho.json", 'w') as f:
        json.dump(tokens, f, indent=4)
    # Save tokens for later use (here we just print)
    print("Access Token:", tokens.get('access_token'))
    print("Refresh Token:", tokens.get('refresh_token'))
    
    # You can save tokens to a file or database here
    
    return 'Authorization successful! Tokens received. You can close this page.'

if __name__ == '__main__':
    app.run(port=8000)
