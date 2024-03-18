#!/usr/bin/env python3
<<<<<<< HEAD
import requests
import json
from PIL import Image
import base64



url = "http://0.0.0.0:5000/api/v1/user/"

image = "yaay.jpg"
with open(image, "rb") as image_file:
    file_encoded = base64.b64encode(image_file.read()).decode('utf-8')


payload = {
    "email": "amal@gmail.com",
    "name": "amal sayed",
    "phone_number": "0123456789",
    "picture": file_encoded,
    "password": "56789",
    "token": "amal5678"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

# url = "http://0.0.0.0:5000/api/v1/categories"
# response = requests.get(url)

print(response.status_code)
print(response.text)
=======
'''entering data to the database'''

from models import storage
from models.user import User
#from PIL import Image
from models.base_model  import BaseModel
from models.categories import Category
from models.items import Item
from models.favorites import Favorite
import base64

'''testing the user class'''
# image = Image.open('./yaay.jpg')
# resized_image = image.resize((100, 100))
# resized_image.save('yaay.jpg')
# image = Image.open('yaay.jpg')

# user = User(name='Alaa', email='alaa251996@gmail.com', password='123456', phone_number='1234567890', picture=image.tobytes(), token='123456')
# BaseModel.save(user)

# # users = storage.all(User)
# # print(users)
# # # print(users['User.1'].name)
# # # print(users['User.1'].email)
# # alaa = storage.get(User, 1)
# # print(alaa.to_dict())
# # BaseModel.delete(alaa)
# # print('deleted ==========')
# users = storage.all(User)
# print(users)

# update = storage.update(User, 1,email='afsgeh')
# ala = storage.get(User, 1)
# print(ala['email'])


'''inserting data to the categories table'''
category1 = Category(name='Electronics')
category2 = Category(name='Clothes')
category3 = Category(name='Books')
category4 = Category(name='Furniture')
category5 = Category(name='Cars')
category6 = Category(name='Bikes')
category7 = Category(name='Accessories')
category8 = Category(name='Toys')
category9 = Category(name='Others')
category10 = Category(name='Mobile and Tablets')
category11 = Category(name='Computers & Accessories')


# BaseModel.save_all([category1, category2,category3,category4])

# categories = storage.all(Category)
# print(categories)

'''testing the items class'''
# image = "yaay.jpg"
# with open(image, "rb") as image_file:
#      file_encoded = base64.b64encode(image_file.read()).decode('utf-8')
# item = Item(name='iphone 12', description='iphone 12 used for 10 month', price=11000, picture=file_encoded, user_id=3, category_id=1)
# BaseModel.save(item)

# all_items = storage.all(Item)
# print(all_items)

# # tv_items = storage.search_items('tv')
# # print(tv_items)

# '''testing favourites'''
# # user1 = User(name='Alice', email='alice@example.com', password='password1', phone_number='1234567890')
# # user2 = User(name='Bob', email='bob@example.com', password='password2', phone_number='0987654321')
# # BaseModel.save_all([user1, user2, category10, category11])

# item1 = Item(name='Phone', description='Smartphone', price=500, picture=file_encoded, size=5, user_id=10, category_id=19)
# item2 = Item(name='Laptop', description='Notebook computer', price=1000, picture=file_encoded, size=15, user_id=11, category_id=20)

# # BaseModel.save_all([item1, item2])

# favorite1 = Favorite(user_id=1, item_id=1)
# favorite2 = Favorite(user_id=2, item_id=2)
# favorite3 = Favorite(user_id=3, item_id=1)
# favorite4 = Favorite(user_id=3, item_id=3)

# BaseModel.save_all([favorite1, favorite2])
# BaseModel.save(favorite3)

# print(storage.all(Favorite))
# # get_user_10= storage.get(User, 10)
# # print(get_user_10.to_dict())

# # get_user_10_favorites = storage.get_favorites(10)
# # print(get_user_10_favorites)

print(storage.getuserfavorites(3))

# print(storage.getuserfavorites(1))
# print(storage.getuserfavorites(2))



# user1 = User(name='hamza', email='hamza@example.com', password='password5', phone_number='1234567890', picture=file_encoded, token='2356')
# user2 = User(name='roka', email='roka@example.com', password='password4', phone_number='0987654321', picture=file_encoded, token='1245')

# # BaseModel.save_all([user1, user2])
# hamza = storage.get(User, 14)
# roka = storage.get(User, 15)
# suzan = storage.get(User, 12)

# # hamza.following.append(roka)
# # hamza.following.append(suzan)
# # suzan.following.append(roka)
# # storage.save()

# hamza = storage.get(User, 14)
# roka = storage.get(User, 15)
# suzan = storage.get(User, 12)
# # print('============hamza===================')
# # print(hamza.to_dict())
# # print('============roka===================')
# # print(roka.to_dict())
# # print('============suzan===================')
# # print(suzan.to_dict())

# get_followers = storage.get_user_followers(15)
# print([follower.get('name') for follower in get_followers])

# # get_following = storage.get_user_following(14)
# # print(get_following)

# # print(suzan.to_dict())

# # 
# # print(hamza.to_dict())
>>>>>>> database
