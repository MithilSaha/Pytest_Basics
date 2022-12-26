import requests

endpoint = "https://simple-grocery-store-api.glitch.me/status"
response = requests.get(endpoint)
print(response)

data = response.json()
print(type(data))

status_code = response.status_code
print(type(status_code))

headers  = response.headers
print(dir(headers))