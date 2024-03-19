#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage
from models.user import User
from models.categories import Category
from models.favorites import Favorite

@app_views.route('/user', methods=['POST'], strict_slashes=False)
def add_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' or 'name' not in request.get_json():
        abort(400, description="Missing user email or name")
    if 'password' not in request.get_json():
        abort(400, description="Missing user password")
    if 'phone_number' not in request.get_json():
        abort(400, description="Missing user whatsapp number")
   
    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/user', methods=['GET'], strict_slashes=False)
def get_user():
    token = request.headers.get('Authorization')
    print("Received token:", token)
    user = storage.getuser_bytoken(token)
    if not user:
        abort(404,description="not avalid user")
    return jsonify(user.to_dict())

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():

    all_categories = storage.all(Category)
    return make_response(jsonify(all_categories), 200)

@app_views.route('/user', methods=['PUT'], strict_slashes=False)
def put_user():
    """
    Updates a user
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(404,description="not avalid user")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'token']

    data = request.get_json()
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
    data = request.get_json()
    instance = Favorite(**data)
    instance.save()
    return jsonify(instance.to_dict())

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
    if 'id' not in request.get_json():
        abort(400, description="Missing item id")

    data =request.get_json()
    id = data.get('id')


    status =storage.delete_favourite(item_id=id,user_id=user.id)
    if status and status == False:
        return make_response(jsonify({"Item not deleted"}), 400)

    return make_response(jsonify({}), 200)
