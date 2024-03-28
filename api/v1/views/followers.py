#!/usr/bin/python3
""" objects that handle all default RestFul followers API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User
from models.favorites import Favorite
from models.followers import Follower

@app_views.route('/follow', methods=['POST'], strict_slashes=False)
def add_follow_recored():
    """
    Creates a follow recored
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")
    
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_followed_id' not in request.get_json():
        abort(400, description="Missing id of the user to be followed")
    
    id=request.json.get('user_followed_id')
    user_to_be_followed=storage.get(User,id)
    user.following.append(user_to_be_followed)
    if(user.save()):
        return make_response(jsonify({'message':'followed sucessfully'}), 201)
    else:
        return make_response(jsonify({'error':'followed failed'})),400

@app_views.route('/unfollow', methods=['POST'], strict_slashes=False)
def remove_follow_recored():
    """
    Removes a follow recored
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")
    
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_followed_id' not in request.get_json():
        abort(400, description="Missing id of the user to be unfollowed")
    
    id=request.json.get('user_followed_id')
    user_to_be_unfollowed=storage.get(User,id)
    user.following.remove(user_to_be_unfollowed)
    if(user.save()):
        return make_response(jsonify({'message':'unfollowed sucessfully'}), 201)
    else:
        return make_response(jsonify({'error':'unfollowed failed'})),400

@app_views.route('/followers', methods=['GET'], strict_slashes=False)
def get_followers():
    """
    Get all followers
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")
    
    followers=user.get_user_followers()
    return make_response(jsonify(followers), 200)

@app_views.route('/following', methods=['GET'], strict_slashes=False)
def get_following():
    """
    Get all following
    """
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")
    
    following=user.get_user_following()
    return make_response(jsonify(following), 200)
