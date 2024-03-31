#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage
from models.user import User
from models.categories import Category
from models.favorites import Favorite
from models.items import Item
from models.search import Search
from models.base_model import BaseModel
from recommendation.recommendation import get_recommendations
from helpers import save_image
from flask import send_from_directory

dir = os.path.expanduser("~/alx/second-hand/images/items")

@app_views.route('/items', methods=['POST'], strict_slashes=False)
def add_item():
    """
    Creates an item
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(400,description="not a valid user")

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing item name")
    if 'description' not in request.get_json():
        abort(400, description="Missing item description")
    if 'price' not in request.get_json():
        abort(400, description="Missing item price")
    if 'picture' not in request.get_json():
        abort(400, description="Missing item picture")
    if 'category_id' not in request.get_json():
        abort(400, description="Missing item category id")
    if 'location_id' not in request.get_json():
        abort(400, description="Missing item Location")
   
    data = request.get_json()
    data['user_id'] = user.id
    data['picture'] = save_image(data, dir)
    
    instance = Item(**data)
    # instance.save()
    BaseModel.save(instance)
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/search-items', methods=['GET'], strict_slashes=False)
def search_item():
    """
    search an item
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token).to_dict()

    if not request.get_json():
        abort(400, description="Not a JSON")
    
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    data = request.get_json()
    location_id = data.get('location_id')
    category_id = data.get('category_id')
    search_text = data.get('name')
    result = storage.search_item_with_filters(location_id=location_id,cat_id=category_id,search_text=search_text, page=page, per_page=per_page)
    items = result['items']
    total_pages = result['total_pages']
    next_page = page + 1 if page < total_pages else None
    if search_text:
        if user:
            searched = Search(user_id=user['id'], name=search_text)
            BaseModel.save(searched)
    return make_response(jsonify({'items': items, 'next_page': next_page}), 200)

@app_views.route('/items', methods=['PUT'], strict_slashes=False)
def put_item():
    """
    Updates a item
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(400,description="not avalid user")

    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'id' not in request.get_json():
        abort(400, description="Missing item id")

    ignore = ['id']

    data = request.get_json()
    if 'picture' in data:
        data['picture'] = save_image(data, dir)
    id_value = data.get('id')
    item =storage.update(Item,id_value,ignore_items=ignore,**data)
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
        abort(400, description="not a valid user")
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'id' not in request.get_json():
        abort(400, description="Missing item id")

    data = request.get_json()
    item_id = data.get('id')
    item = storage.get(Item, item_id)

    if not item:
        abort(400, description="not a valid item")

    # storage.delete(item)
    # storage.save()
    BaseModel.delete(item)

    return make_response(jsonify({}), 200)

@app_views.route('/items.by.category/<cat_id>', methods=['GET'], strict_slashes=False)
def get_items_byCategory(cat_id):
    """items by category"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_pages = (storage.count_items_by_category(cat_id) + per_page - 1) // per_page
    next_page = page + 1 if page < total_pages else None
    items = storage.get_items_by_category(cat_id, page, per_page)
    return make_response(jsonify({'items':items, 'next_page': next_page}), 200)

@app_views.route('/items.by.location/<loc_id>', methods=['GET'], strict_slashes=False)
def get_items_byLocation(loc_id):
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_pages = (storage.count_items_by_location(loc_id) + per_page - 1) // per_page
    items = storage.get_items_by_location(loc_id, page, per_page)
    next_page = page + 1 if page < total_pages else None
    return make_response(jsonify({'items': items, 'next_page': next_page}), 200)

@app_views.route('/items', methods=['GET'], strict_slashes=False)
def get_items_byuser():
    """
    getitems
    
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)

    if not user:
        abort(400, description="not a valid user")
    
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_pages = (storage.count_items_by_user(user.id) + per_page - 1) // per_page
    result = storage.getItemsbyuser(user.id, page, per_page)
    next_page = page + 1 if page < total_pages else None
    return make_response(jsonify({'items':result, 'next_page': next_page}), 200)

@app_views.route("/load", methods=['Get'], strict_slashes=False)
def load_items():
    """load items"""
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")
        
    page = request.args.get('page', 1, type=int)
    per_page = 10

    recomended_items = get_recommendations(user.id)

    total_pages = ((len(recomended_items) + storage.count(Item)) + per_page - 1) // per_page
    flag = False

    if (page == 1 and len(recomended_items) > 0):
            flag = True
            return make_response(jsonify({'items':recomended_items, 'next_page':2}), 200)

    if (flag):
        page -= 1
        next_page = page + 2 if page < total_pages else None
    else:
        next_page = page + 1 if page < total_pages else None

    if (not flag and len(recomended_items) > 0):
            page -= 1

    most_recent_items = storage.get_most_recent_items(page, per_page)
    return make_response(jsonify({'items':most_recent_items, 'next_page':next_page}), 200)

@app_views.route('/items_photos/<path:filename>', methods=['GET'], strict_slashes=False)
def get_items_photo(filename):
    return send_from_directory(dir, filename)
