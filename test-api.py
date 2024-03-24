#!/usr/bin/env python3
import requests
import json
from PIL import Image
import base64



url = "http://0.0.0.0:5000/api/v1/favorites"



image = "yaay.jpg"
with open(image, "rb") as image_file:
    file_encoded = base64.b64encode(image_file.read()).decode('utf-8')

    # "password": "56789",

payload_user = {
    "email": "mihre@gmail.com",
    "name": "mihre",
    "phone_number": "0123456789",
    "picture": file_encoded,
    "token": "amal123456",
    "password": "56789",

}
payload_user_login= {
    "email": "amal@gmail.com",
    "password":"123456"
}
payload_item = {
    "description": "a defacto black coat",
    "name": "black coat",
    "price": "1000",
    "picture": file_encoded,
    "category_id": 1,
    "location_id": 2
}
payload_item_search = {
    
    "id":3
}
payload_add_fav = {
    
    "user_id":1,
    "item_id":4
}
payload_item_update = {
    
    "description": "a defacto black coat",
    "size" : 42,
    "name": "black coat",
    "price": "1000",
    "picture": file_encoded,
    "category_id": 1,
    "location_id":3,
    "id": 3
}
token = 'mihre56788'
# token ='amal123456'
headers = {
    "Content-Type": "application/json",
    "Authorization": f'{token}',
}

# response = requests.delete(url,data=json.dumps(payload_add_fav),headers=headers)
response = requests.get(url,headers=headers)


# url = "http://0.0.0.0:5000/api/v1/categories"
# response = requests.get(url)

print(response.status_code)
print(response.text)
