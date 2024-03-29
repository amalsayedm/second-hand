#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage
from models.user import User
from models.categories import Category
from models.favorites import Favorite
from models.base_model import BaseModel
import secrets
from werkzeug.security import generate_password_hash, check_password_hash



@app_views.route('/user', methods=['POST'], strict_slashes=False)
def add_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing user email")
    if 'name'  not in request.get_json():
        abort(400, description="Missing user name")
    if 'password' not in request.get_json():
        abort(400, description="Missing user password")
    if 'phone_number' not in request.get_json():
        abort(400, description="Missing user whatsapp number")
    
    user = storage.finduser_byemail(request.json.get('email'))
    if user:
        return jsonify({'error': 'User already exists'}), 400
    
    """ Generate a unique salt for each user"""
    salt = secrets.token_hex(16)
    encrypted_password = request.json.get('password')

    password_hash = generate_password_hash( encrypted_password+ salt)

    data = request.get_json()
    data['password'] = password_hash
    data['salt'] = salt

    instance = User(**data)
    # instance.save()
    BaseModel.save(instance)
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/user', methods=['GET'], strict_slashes=False)
def get_user():
    token = request.headers.get('Authorization')
    print("Received token:", token)
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not avalid user")
    return jsonify(user.to_dict())

@app_views.route('/user.login', methods=['GET'], strict_slashes=False)
def user_login():

    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        abort(400, description="Missing user email")
    if not password:
        abort(400, description="Missing password")
    user = storage.finduser_byemail(email)
    if not user:
        return jsonify({'error': 'User not found'}), 400
    if check_password_hash(user.password, password + user.salt):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Incorrect password'}), 401


@app_views.route('/user', methods=['PUT'], strict_slashes=False)
def put_user():
    """
    Updates a user
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'token']
    data = request.get_json()
    encrypted_password = request.json.get('password')
    if (encrypted_password):
        print(encrypted_password)
        salt = secrets.token_hex(16)
        password_hash = generate_password_hash( encrypted_password+ salt)
        data = request.get_json()
        data['password'] = password_hash
        data['salt'] = salt

    for key, value in data.items():
        if key not in ignore:
            if key == 'picture':
                    encoded_data = value.encode('utf-8')
                    setattr(user, key, encoded_data)
            else:
                setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)

@app_views.route('/favorites', methods=['GET'], strict_slashes=False)
def get_userfavorites():

    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(404,description="not avalid user")
    favourites = storage.getuserfavorites(user.id)
    return jsonify(favourites)

@app_views.route('/favorites', methods=['POST'], strict_slashes=False)
def add_userfavorites():

    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(404,description="not avalid user")
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user id")
    if 'item_id' not in request.get_json():
        abort(400, description="Missing item_id")
    id =request.json.get("user_id")
    if(id != user.id):
        abort(400,description="not valid user id")  

    data = request.get_json()
    instance = Favorite(**data)
    if(instance.save()):
        return jsonify(instance.to_dict(),200)
    else:
        return jsonify({"error":"somthing wrong"}),400


@app_views.route('/favorites', methods=['DELETE'],
                 strict_slashes=False)
def delete_favorite():
    """
    Deletes an Object
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(404, description="not a valid user")
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'item_id' not in request.get_json():
        abort(400, description="Missing item id")
    user_id =request.json.get("user_id")
    if(user_id != user.id):
        abort(400,description="not valid user id") 
    itemid= request.json.get("item_id")

    status =storage.delete_favourite(item_id=itemid,user_id=user.id)
    if status and status == False:
        return make_response(jsonify({"Item not deleted"})), 400

    return make_response(jsonify({}), 200)
