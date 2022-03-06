from urllib import response
import requests

response = requests.get("http://api.open-notify.org/astros.json")
# print(response) # response status
print(response.json()) #mengembalikan response berupa json

# How to Use Query Parameters 
