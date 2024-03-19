#!/usr/bin/env python3
import requests
import json
from PIL import Image
import base64



url = "http://0.0.0.0:5000/api/v1/categories/"


# headers = {'Authorization': f'Bearer {token}'}

image = "yaay.jpg"
with open(image, "rb") as image_file:
    file_encoded = base64.b64encode(image_file.read()).decode('utf-8')


payload = {
    "email": "amal@gmail.com",
    "name": "mihrema",
    "phone_number": "0123456789",
    "picture": file_encoded,
    "password": "56789",
    "token": "mihre5678"
}
token = 'mihre5678'
headers = {
    "Content-Type": "application/json",
    "Authorization": f'{token}',
}

# response = requests.put(url, data=json.dumps(payload),headers=headers)
response = requests.get(url)


# url = "http://0.0.0.0:5000/api/v1/categories"
# response = requests.get(url)

print(response.status_code)
print(response.text)
