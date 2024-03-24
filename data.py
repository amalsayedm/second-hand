#!/usr/bin/env python3


'''entering data to the database'''

from models import storage
from models.user import User
#from PIL import Image
from models.base_model  import BaseModel
from models.categories import Category
from models.items import Item
from models.favorites import Favorite
from models.search import Search
from models.locations import Location
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

image = "yaay.jpg"
with open(image, "rb") as image_file:
    file_encoded = base64.b64encode(image_file.read()).decode('utf-8')

'''inserting data to the categories table'''
category1 = Category(name='Electronics',picture=file_encoded)
category2 = Category(name='Clothes',picture=file_encoded)
category3 = Category(name='Books',picture=file_encoded)
# category4 = Category(name='Furniture',picture=file_encoded)
# category7 = Category(name='Accessories',picture=file_encoded)
# category8 = Category(name='Toys',picture=file_encoded)
# category9 = Category(name='Others',picture=file_encoded)
# category10 = Category(name='Mobile and Tablets',picture=file_encoded)
# category11 = Category(name='Computers & Accessories',picture=file_encoded)


# BaseModel.save_all([category1, category2,category3])

# categories = storage.all(Category)
# print(categories)

'''testing the items class'''
image = "yaay.jpg"
with open(image, "rb") as image_file:
     file_encoded = base64.b64encode(image_file.read()).decode('utf-8')
item = Item(name='Samsung tv', description='LG 11', price=11000, picture=file_encoded, user_id=1, category_id=1,location_id=1)
item2 = Item(name='blue dress', description='blue long woman dress', price=550, picture=file_encoded, user_id=1, category_id=2,location_id=2)
item3 = Item(name='solasyt 3"rnata', description='best seller book', price=50, picture=file_encoded, user_id=2, category_id=3,location_id=3)
item4 = Item(name='black coat', description='black defacto coat used twice', price=900, picture=file_encoded, user_id=2, category_id=2,location_id=5)

# BaseModel.save_all([item,item2,item3,item4])

# all_items = storage.all(Item)
# print(all_items)

# tv_items = storage.search_items('tv')
# print(tv_items)

'''testing favourites'''
# user1 = User(name='Alice', email='alice@example.com', password='password1', phone_number='1234567890')
# user2 = User(name='Bob', email='bob@example.com', password='password2', phone_number='0987654321')
# BaseModel.save_all([user1, user2, category10, category11])

item1 = Item(name='Phone', description='Smartphone', price=500, picture=file_encoded, size=5, user_id=2, category_id=10, location_id=1)
item2 = Item(name='Laptop', description='Notebook computer', price=1000, picture=file_encoded, size=15, user_id=1, category_id=11,location_id=4.)

# BaseModel.save_all([item1, item2])

favorite1 = Favorite(user_id=1, item_id=3)
favorite2 = Favorite(user_id=2, item_id=4)
favorite3 = Favorite(user_id=1, item_id=9)

# BaseModel.save_all([favorite1, favorite2, favorite3])
# BaseModel.save(favorite3)

# get_user_10= storage.get(User, 14)
# print(get_user_10.to_dict())

# get_user_10_favorites = storage.getuserfavorites(14)
# print(get_user_10_favorites)


# favorite3 = Favorite(user_id=15, item_id=1)
# BaseModel.save(favorite3)

# favorite4 = Favorite(user_id=10, item_id=1)
# BaseModel.save(favorite4)

'''testing followers'''

user1 = User(name='hamza', email='hamza@example.com', password='password5', phone_number='1234567890', picture=file_encoded, token='2356', salt='1234')
user2 = User(name='roka', email='roka@example.com', password='password4', phone_number='0987654321', picture=file_encoded, token='1245', salt='1234')

# BaseModel.save_all([user1, user2])
hamza = storage.get(User, 1)
roka = storage.get(User, 2)


# hamza.following.append(roka)
# storage.save()

# hamza = storage.get(User, 14)
# # print(hamza.get_user_following())
# print(hamza.get_user_followers())
# roka = storage.get(User, 15)
# print(roka.get_user_following())
# print(roka.get_user_followers())
# suzan = storage.get(User, 12)
# print('============hamza===================')
# print(hamza.to_dict())
# print('============roka===================')
# print(roka.to_dict())
# print('============suzan===================')
# print(suzan.to_dict())

# get_followers = storage.get_user_followers(15)
# print([follower.get('name') for follower in get_followers])

# get_following = storage.get_user_following(14)
# print(get_following)

# print(suzan.to_dict())

# 
# print(hamza.to_dict())


'''testing  Location'''

location1 = Location(name='Cairo')
location2 = Location(name='Giza')
location3 = Location(name='Alexandria')
location4 = Location(name='Aswan')
location5 = Location(name='Luxor')
location6 = Location(name='Hurghada')
location7 = Location(name='Sharm El Sheikh')
location8 = Location(name='Dahab')
location9 = Location(name='Suez')
location10 = Location(name='Port Said')
location11 = Location(name='Ismailia')
location12 = Location(name='Mansoura')
location13 = Location(name='Tanta')

# BaseModel.save_all([location1, location2, location3, location4, location5, location6, location7, location8, location9, location10, location11, location12, location13])
# print(storage.all(Location))

# item1 = Item(name='Phone', description='Smartphone', price=500, picture=file_encoded, size=5, user_id=10, category_id=19, location_id=1)
# item2 = Item(name='Laptop', description='Notebook computer', price=1000, picture=file_encoded, size=15, user_id=11, category_id=20, location_id=2)
# item3 = Item(name='Tablet', description='Tablet computer', price=300, picture=file_encoded, size=10, user_id=12, category_id=19, location_id=3)
# item4 = Item(name='Desktop', description='Desktop computer', price=800, picture=file_encoded, size=20, user_id=13, category_id=20, location_id=4)

# BaseModel.save_all([item1, item2, item3, item4])

# get_location_1 = storage.get(Location, 1)
# # print(get_location_1.to_dict())

# get_item1 = storage.get(Item, 1)
# # print(get_item1.to_dict())

# cairo_items = storage.search_items_by_location('cairo')
# # print(cairo_items)

# Mobile_and_Tablets_items = storage.search_items_by_category('Mobile')
# print(Mobile_and_Tablets_items)

'''testing search'''
search1 = Search(user_id=1, name='phone')
search2 = Search(user_id=2, name='dress')
search3 = Search(user_id=2, name='book')

# BaseModel.save_all([search1, search2, search3])

get_search_by_user_id_2 = storage.get_searches_by_user(2)

print(get_search_by_user_id_2)

