from urllib import response
import requests

query = {'lat':'45', 'lon':'180'}
response = requests.get("http://api.open-notify.org/iss-pass.json",query)
print(response.json())