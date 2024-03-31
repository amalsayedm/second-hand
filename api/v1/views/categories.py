#!/usr/bin/python3
""" objects that handle all default RestFul categories API actions"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.categories import Category
from models.base_model import BaseModel
from models import storage
from flask import send_from_directory
from helpers import save_image

dir = os.path.expanduser("/home/second2hand/mysite/images/categories")


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """get all categories"""
    all_categories = storage.all(Category)
    return make_response(jsonify(all_categories), 200)


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def add_category():
    """
    Creates a category
    """
    auth = request.headers.get('Authorization')
    if auth != "admin":
        abort(400, description="Admin access required")

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing category name")
    if 'picture' not in request.get_json():
        abort(400, description="Missing category picture")

    data = request.get_json()
    name = save_image(data, dir)

    instance = Category(name=data['name'], picture=name)
    BaseModel.save(instance)

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route(
    '/categories_photos/<path:filename>',
    methods=['GET'], strict_slashes=False)
def get_photo(filename):
    """access photo of category"""
    return send_from_directory(dir, filename)
