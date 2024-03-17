#!/usr/bin/env python3
'''entering data to the database'''

from models import storage
from models.user import User
#from PIL import Image
from models.base_model  import BaseModel
from models.categories import Category

'''testing the user class'''
""""image = Image.open('./yaay.jpg')
resized_image = image.resize((100, 100))
resized_image.save('yaay.jpg')
image = Image.open('yaay.jpg')"""

user = User(name='khalid', email='khalid@gmail.com', password='123456', phone_number='1234567890', picture= None, token='123456')
BaseModel.save(user)

# users = storage.all(User)
# print(users)
# # print(users['User.1'].name)
# # print(users['User.1'].email)
# alaa = storage.get(User, 1)
# print(alaa.to_dict())
# BaseModel.delete(alaa)
# print('deleted ==========')
users = storage.all(User)
print(users)

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

# BaseModel.save_all([category1, category2, category3, category4, category5, category6, category7, category8, category9])

# categories = storage.all(Category)
# print(categories)
