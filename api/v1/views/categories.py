#!/usr/bin/python3
""" objects that handle all default RestFul categories API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():

    all_categories = storage.all(Category).values()
    list_r = []
    return jsonify(all_categories)

@app_views.route('/items/<cat_id>', methods=['GET'], strict_slashes=False)
def get_catitems(cat_id):

    all_items = storage.getItemsbycat(cat_id).values()
    return jsonify(all_items)

@app_views.route('/items/<user_id>', methods=['GET'], strict_slashes=False)
def get_useritems(user_id):

    all_items = storage.getrecipesbytype(user_id).values()
    list_r = []
    for item in all_items:
        list_r.append(item.to_dict())
    return jsonify(list_r)

@app_views.route('/items/<user_id>', methods=['POST'], strict_slashes=False)
def Post_item(user_id):
    """ add item to table"""

@app_views.route('/items', methods=['GET'], strict_slashes=False)
def get_items():
    """get recommended items"""
    all_recipes = storage.all(Recipe).values()
    list_r = []
    for recipe in all_recipes:
        list_r.append(recipe.to_dict())
    return jsonify(list_r)
