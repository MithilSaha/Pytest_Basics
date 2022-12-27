import requests
import json

get_endpoint = "https://simple-grocery-store-api.glitch.me/status"
response = requests.get(get_endpoint)
'''
response is an object. It is an instance of requests.models.Response class.
'''
print(response)

'''
response_payload is a JSON object
'''
response_payload = response.json()
print(response_payload)
print(type(response_payload))

'''
header paranmeters of reponse payload
'''
response_headers = response.headers
print(response_headers)
print(response_headers["Content-Type"])

'''
status code of response
'''
response_status_code = response.status_code
print(response_status_code)

'''
response time
'''
response_time = response.elapsed.total_seconds()
print(f"{response_time} seconds")
response_time = int((response_time)*1000)
print(f"{response_time} ms")

post_endpoint = "https://simple-grocery-store-api.glitch.me/carts"
response = requests.post(post_endpoint)
print(response)

response_payload = response.json()
print(response_payload)

cartId = response_payload["cartId"]

get_endpoint = "https://simple-grocery-store-api.glitch.me/carts/" + cartId
response = requests.get(get_endpoint)
print(response)

response_payload = response.json()
print(response_payload)

post_endpoint = f"https://simple-grocery-store-api.glitch.me/carts/{cartId}/items"
post_request_payload = {
    "productId": 7395,
    "quantity": 9
}

'''
json parameter sends a json object to an url
'''
response  = requests.post(post_endpoint,json = post_request_payload)
print(response)

response_payload = response.json()
print(response_payload)

itemId = response_payload["itemId"]

get_endpoint = f"https://simple-grocery-store-api.glitch.me/carts/{cartId}"
response = requests.get(get_endpoint)
print(response)

response_payload = response.json()
print(response_payload)

patch_endpoint = f"https://simple-grocery-store-api.glitch.me/carts/{cartId}/items/{itemId}"
patch_request_body = {
    "quantity": 5
}
headers = {
  'Content-Type': 'application/json'
}

'''
json.dumps() function makes a python dictionary to a json string
'''
response = requests.patch(patch_endpoint,headers = headers,data = json.dumps(patch_request_body))
print(response)
print(response.headers)

get_endpoint = f"https://simple-grocery-store-api.glitch.me/carts/{cartId}"
response = requests.get(get_endpoint)
print(response)

response_payload = response.json()
print(response_payload)

put_endpoint = f"https://simple-grocery-store-api.glitch.me/carts/{cartId}/items/{itemId}"
request_payload = {
    "productId": 1709,
    "quantity" : 8
}
headers = {
  'Content-Type': 'application/json'
}
response = requests.put(put_endpoint,headers=headers,data=json.dumps(request_payload))
print(response)

get_endpoint = f"https://simple-grocery-store-api.glitch.me/carts/{cartId}"
response = requests.get(get_endpoint)
print(response)

response_payload = response.json()
print(response_payload)

post_endpoint = "https://simple-grocery-store-api.glitch.me/api-clients"
request_payload = {
    "clientName": "Mark Jonass",
    "clientEmail": "markjonass@example.com"
}
response = requests.post(post_endpoint,json = request_payload)
print(response)

response_payload = response.json()
print(response_payload)

access_token = response_payload["accessToken"]

post_endpoint = "https://simple-grocery-store-api.glitch.me/orders"
request_payload = {
    "cartId": cartId,
    "customerName": "Mark Jonass",
    "comment": "Happy Customer!"
}
headers = {
    "Authorization": f"{access_token}",
    'Content-Type': 'application/json'
}
response = requests.post(post_endpoint,headers=headers,json=request_payload)
print(response)

response_payload = response.json()
print(response_payload)

order_id = response_payload["orderId"]

get_endpoint = "https://simple-grocery-store-api.glitch.me/orders"
headers = {
    "Authorization": f"{access_token}"
}

response = requests.get(get_endpoint,headers = headers)
print(response)

response_payload = response.json()
print(response_payload)

delete_endpoint = f"https://simple-grocery-store-api.glitch.me/orders/{order_id}"
headers = {
    "Authorization": f"{access_token}"
}

response = requests.delete(delete_endpoint,headers=headers)
print(response)

get_endpoint = "https://simple-grocery-store-api.glitch.me/orders"
headers = {
    "Authorization": f"{access_token}"
}

response = requests.get(get_endpoint,headers = headers)
print(response)

response_payload = response.json()
print(response_payload)