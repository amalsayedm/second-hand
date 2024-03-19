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
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' or 'description' not in request.get_json():
        abort(400, description="Missing name or description")
    if 'price' not in request.get_json():
        abort(400, description="Missing price")
    if 'picture' not in request.get_json():
        abort(400, description="Missing item picture")
    if 'user_id' or 'category_id' in request.get_json():
        abort(400, description="Missing category or user ids")
   
    data = request.get_json()
    instance = Item(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
