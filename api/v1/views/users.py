#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage
from models.user import User
from models.categories import Category

@app_views.route('/user', methods=['POST'], strict_slashes=False)
def add_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing user email")
    if 'password' not in request.get_json():
        abort(400, description="Missing user password")
    if 'phone_number' not in request.get_json():
        abort(400, description="Missing user whatsapp number")
   
    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/user/<token>', methods=['GET'], strict_slashes=False)
def get_user(token):

    user = storage.getuser_bytoken(token)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():

    all_categories = storage.all(Category)
    return jsonify(all_categories)

@app_views.route('/user/<token>', methods=['PUT'], strict_slashes=False)
def put_user(token):
    """
    Updates a user
    """
    user = storage.getuser_bytoken(token)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
