import requests
import json

#Check Grocery API Status
def test_getGroceryApiStatus():
    get_grocery_api_status_endpoint = "https://simple-grocery-store-api.glitch.me/status"
    get_grocery_api_status_response = requests.get(get_grocery_api_status_endpoint)
    assert get_grocery_api_status_response.status_code == 200, f"API Response Status Code is {get_grocery_api_status_response.status_code}"
    print(f"API Status Code is {get_grocery_api_status_response.status_code}")
    assert "application/json" in get_grocery_api_status_response.headers["Content-Type"]
    print("Response Header's Content-Type is application/json")

#Create Cart
def test_createCart():
    post_create_cart_endpoint = "https://simple-grocery-store-api.glitch.me/carts"
    post_create_cart_response = requests.post(post_create_cart_endpoint)
    assert post_create_cart_response.status_code == 201, f"API Response Status Code is {post_create_cart_response.status_code}"
    post_create_cart_response_json = post_create_cart_response.json()
    for key in post_create_cart_response_json:
        print(f"\n{key} = {post_create_cart_response_json[key]}")
        if key == "cartId":
            cartId = post_create_cart_response_json["cartId"]
    assert cartId is not None


