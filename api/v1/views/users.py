#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import uuid
from models import storage
from models.user import User
from models.categories import Category
from models.favorites import Favorite
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from models.base_model import BaseModel
from flask import send_from_directory
from helpers import save_image

dir = os.path.expanduser("/home/second2hand/mysite/images/users")


@app_views.route('/user', methods=['POST'], strict_slashes=False)
def add_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        return jsonify({'message': 'Missing user email'}), 400
    if 'name' not in request.get_json():
        return jsonify({'message': 'Missing user name'}), 400
    if 'password' not in request.get_json():
        return jsonify({'message': 'Missing user password'}), 400
    if 'phone_number' not in request.get_json():
        return jsonify({'message': 'Missing user whatsapp number'}), 400

    user = storage.finduser_byemail(request.json.get('email'))
    if user:
        return jsonify({'message': 'User already exists'}), 400

    """ Generate a unique salt for each user"""
    salt = secrets.token_hex(16)
    encrypted_password = request.json.get('password')

    password_hash = generate_password_hash(encrypted_password + salt)
    random_uuid = uuid.uuid4()
    random_token = str(random_uuid)
    data = request.get_json()
    data['password'] = password_hash
    data['salt'] = salt
    data['token'] = random_token

    if 'picture' in request.get_json():
        data['picture'] = save_image(data, dir)

    instance = User(**data)
    instance.save()

    return make_response(
        jsonify({
            'data': instance.to_dict(),
            'message': 'user created sucessfuly'
            }),
        201)


@app_views.route('/user', methods=['GET'], strict_slashes=False)
def get_user():
    """get a user"""
    token = request.headers.get('Authorization')
    print("Received token:", token)
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400, description="not avalid user")
    return jsonify({
        'data': user.to_dict(),
        'message': 'user retrieved sucessfuly'
        }), 200


@app_views.route('/user.login', methods=['Post'], strict_slashes=False)
def user_login():
    """login a user"""
    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        abort(400, description="Missing user email")
    if not password:
        abort(400, description="Missing password")
    user = storage.finduser_byemail(email)
    if not user:
        return jsonify({'message': 'User not found'}), 401
    if check_password_hash(user.password, password + user.salt):
        return jsonify({
            'data': user.to_dict(),
            'message': 'Login sucessfuly'
            }), 200
    else:
        return jsonify({'message': 'Incorrect password'}), 401


@app_views.route('/user', methods=['PUT'], strict_slashes=False)
def put_user():
    """
    Updates a user
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400, description="not a valid user")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'token']
    data = request.get_json()
    encrypted_password = request.json.get('password')
    if (encrypted_password):
        print(encrypted_password)
        salt = secrets.token_hex(16)
        password_hash = generate_password_hash(encrypted_password + salt)
        data = request.get_json()
        data['password'] = password_hash
        data['salt'] = salt

    for key, value in data.items():
        if key not in ignore:
            if key == 'picture':
                value = save_image(data, dir)
                setattr(user, key, value)
            else:
                setattr(user, key, value)
    storage.save()
    return make_response(
        jsonify({
            'data': user.to_dict(),
            'message': 'updated sucessfuly'
            }), 200)


@app_views.route('/favorites', methods=['GET'], strict_slashes=False)
def get_userfavorites():
    """user favorites"""
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(404, description="not avalid user")
    favourites = storage.getuserfavorites(user.id)
    return jsonify(favourites)


@app_views.route('/favorites', methods=['POST'], strict_slashes=False)
def add_userfavorites():
    """add user favorites"""
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(404, description="not avalid user")
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user id")
    if 'item_id' not in request.get_json():
        abort(400, description="Missing item_id")
    id = request.json.get("user_id")
    if(id != user.id):
        abort(400, description="not valid user id")

    data = request.get_json()
    instance = Favorite(**data)
    if(instance.save()):
        return jsonify(instance.to_dict(), 200)
    else:
        return jsonify({"error": "somthing wrong"}), 400


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
    user_id = request.json.get("user_id")
    if(user_id != user.id):
        abort(400, description="not valid user id")
    itemid = request.json.get("item_id")

    status = storage.delete_favourite(item_id=itemid, user_id=user.id)
    if status and status is False:
        return make_response(jsonify({"Item not deleted"})), 400

    return make_response(jsonify({}), 200)


@app_views.route(
    '/users_photos/<path:filename>',
    methods=['GET'],
    strict_slashes=False)
def get_user_photo(filename):
    """access photo of user"""
    return send_from_directory(dir, filename)
