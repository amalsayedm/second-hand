#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage
from models.user import User
from models.categories import Category
from models.favorites import Favorite
from models.items import Item


@app_views.route('/items', methods=['POST'], strict_slashes=False)
def add_user():
    """
    Creates an item
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(404,description="not avalid user")

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' or 'description' not in request.get_json():
        abort(400, description="Missing name or description")
    if 'price' not in request.get_json():
        abort(400, description="Missing price")
    if 'picture' not in request.get_json():
        abort(400, description="Missing item picture")
    if 'category_id' not in request.get_json():
        abort(400, description="Missing category id")
    if 'location_id' not in request.get_json():
        abort(400, description="Missing Location")
   
    data = request.get_json()
    data['user_id'] = user.id
    instance = Item(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/search-items', methods=['GET'], strict_slashes=False)
def get_item():
    """
    Creates an item
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
   
    data = request.get_json()
    location_id = data.get('location_id')
    category_id = data.get('category_id')
    search_text = data.get('name')
    result = storage.search_item_with_filters(location_id=location_id,cat_id=category_id,search_text=search_text)
    return jsonify(result)

@app_views.route('/items', methods=['PUT'], strict_slashes=False)
def put_item():
    """
    Updates a user
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(404,description="not avalid user")

    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'id' not in request.get_json():
        abort(400, description="Missing item id")

    ignore = ['id']

    data = request.get_json()
    id = data.get('id')
    item =storage.update(cls=Item,id=id,kwargs=data,ignore_items=ignore)
    return make_response(jsonify(item.to_dict()), 200)

@app_views.route('/items', methods=['DELETE'],
                 strict_slashes=False)
def delete_item():
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

    data = request.get_json()
    id = data.get('item_id')
    item = storage.get(Item, id)

    if not item:
        abort(404, description="not a valid item")

    storage.delete(item)
    storage.save()

    return make_response(jsonify({}), 200)
