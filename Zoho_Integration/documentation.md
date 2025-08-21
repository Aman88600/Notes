Step 1. Make a zoho account(I made free tier)
At https://www.zoho.com/

Step 2. Make a zoho api
go to https://api-console.zoho.in/
Click Add client
Select Server-based Applications

Fill 
Client Name
Homepage URL
Authorized Redirect URIs

Step 3 : setting up the API
After making the API you will get client_id and client_secret, store them like this in the .env file
client_id=1000.CAUCDPOUWX8HKH6KAJW8SSB7XPFI9D
client_secret=671b7cde8bf0400c61c8845c27e6d6b280393baeba

specify REDIRECT_URI = 'http://localhost:8000/oauth/callback', in refresh_token.py
then, You can run the refresh_token.py, to refresh the token

Step 4 : Using the API
Now, you can make your own folder and modules by going to zoho crm, or use the pre-existing ones.

To GET DATA
With get_module.py you can get all the entries in the specified module
e.g. url = 'https://www.zohoapis.in/crm/v2/Teachers', here I am getting the data of Teachers module


TO POST DATA
With post_request.py you can make a new entry in the specified module the data we are passing should match the fields.
a good example is in post_request


TO UPDATE DATA
use put_request to update specific fields of a specific entry

TO DELETE DATA
Use delete_request.py all you need is the id of the record you want to delete