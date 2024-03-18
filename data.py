#!/usr/bin/env python3
'''entering data to the database'''

from models import storage
from models.user import User
from PIL import Image
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


# '''inserting data to the categories table'''
# category1 = Category(name='Electronics')
# category2 = Category(name='Clothes')
# category3 = Category(name='Books')
# category4 = Category(name='Furniture')
# category5 = Category(name='Cars')
# category6 = Category(name='Bikes')
# category7 = Category(name='Accessories')
# category8 = Category(name='Toys')
# category9 = Category(name='Others')
# category10 = Category(name='Mobile and Tablets')
# category11 = Category(name='Computers & Accessories')


# BaseModel.save_all([category10, category11])

# categories = storage.all(Category)
# print(categories)

'''testing the items class'''
image = "yaay.jpg"
with open(image, "rb") as image_file:
     file_encoded = base64.b64encode(image_file.read()).decode('utf-8')
# item = Item(name='Samsung tv', description='LG 11', price=11000, picture=file_encoded, user_id=1, category_id=1)
# BaseModel.save(item)

# all_items = storage.all(Item)
# print(all_items)

# tv_items = storage.search_items('tv')
# print(tv_items)

'''testing favourites'''
# user1 = User(name='Alice', email='alice@example.com', password='password1', phone_number='1234567890')
# user2 = User(name='Bob', email='bob@example.com', password='password2', phone_number='0987654321')
# BaseModel.save_all([user1, user2, category10, category11])

item1 = Item(name='Phone', description='Smartphone', price=500, picture=file_encoded, size=5, user_id=10, category_id=19)
item2 = Item(name='Laptop', description='Notebook computer', price=1000, picture=file_encoded, size=15, user_id=11, category_id=20)

# BaseModel.save_all([item1, item2])

favorite1 = Favorite(user_id=10, item_id=1)
favorite2 = Favorite(user_id=11, item_id=2)
favorite3 = Favorite(user_id=10, item_id=2)

# BaseModel.save_all([favorite1, favorite2])
BaseModel.save(favorite3)

# get_user_10= storage.get(User, 10)
# print(get_user_10.to_dict())

get_user_10_favorites = storage.get_favorites(10)
print(get_user_10_favorites)
