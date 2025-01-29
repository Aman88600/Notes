# Since this module is not pre-installed in the python standard library therefore we have to install it using the, pip install requests commnad
import requests
text = requests.get("https://github.com/Aman88600/")
print(text)