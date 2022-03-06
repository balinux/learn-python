from urllib import response
from urllib.request import HTTPBasicAuthHandler
import requests

response = requests.get("https://api.github.com/user", auth=HTTPBasicAuthHandler())