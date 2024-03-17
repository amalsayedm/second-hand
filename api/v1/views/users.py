#!/usr/bin/python3
""" objects that handle all default RestFul user API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/add-user', methods=['POST'], strict_slashes=False)
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
    if 'whatsapp' not in request.get_json():
        abort(400, description="Missing user whatsapp number")
   
    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/add-favorite', methods=['POST'], strict_slashes=False)
def post_favorite():
    """
    Creates a favorite
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user id")
    if 'item_id' not in request.get_json():
        abort(400, description="Missing item id")
   
    data = request.get_json()
    instance = Favorites(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/favorites/<id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_favorite(id):
    """
    Deletes an Object
    """

    """favorite = storage.get(Favorites, id)

    if not favorite:
        abort(404)

    storage.delete(favorite)
    storage.save()

    return make_response(jsonify({}), 200)"""

@app_views.route('/favorites/<user_id>', methods=['GET'], strict_slashes=False)
def get_userfavorites(user_id):

    all_fav = storage.getuserfavorites(user_id).values()
    return jsonify(all_fav)

@app_views.route('/follow-user', methods=['POST'], strict_slashes=False)
def post_favorite():
    """
    Creates a following recored
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user id")
    if 'follwing_id' not in request.get_json():
        abort(400, description="Missing following id")
   
    data = request.get_json()
    instance = followers(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/followers/<id>', methods=['GET'],
                 strict_slashes=False)
def get_followers(id):
    """
    get user followers
    """
    all_followers = storage.getuserfollowers(user_id).values()
    return jsonify(list_r)

@app_views.route('/followings/<id>', methods=['GET'],
                 strict_slashes=False)
def get_followings(id):
    """
    get user followers
    """
    all_followings = storage.getuserfollowers(user_id).values()
    list_r = []
    for f in followings:
        list_r.append(f.to_dict())
    return jsonify(list_r)

@app_views.route('/followings/<id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_favorite(id):
    """
    Deletes an Object
    """

    following = storage.get(Favorites, id)

    if not following:
        abort(404)

    storage.delete(following)
    storage.save()

    return make_response(jsonify({}), 200)
