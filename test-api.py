#!/usr/bin/env python3
import requests
import json
from PIL import Image
import base64



url = "http://0.0.0.0:5000/api/v1/user"



image = "yaay.jpg"
with open(image, "rb") as image_file:
    file_encoded = base64.b64encode(image_file.read()).decode('utf-8')


payload_user = {
    "email": "mihre@gmail.com",
    "name": "mihre",
    "phone_number": "0123456789",
    "picture": file_encoded,
    "password": "56789",
    "token": "mihre56788"
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
token = 'mihre5678'

headers = {
    "Content-Type": "application/json",
    "Authorization": f'{token}',
}

response = requests.put(url,data=json.dumps(payload_user),headers=headers)
# response = requests.get(url)


# url = "http://0.0.0.0:5000/api/v1/categories"
# response = requests.get(url)

print(response.status_code)
print(response.text)
