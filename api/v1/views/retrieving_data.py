#!/usr/bin/python3
"""loading items"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User
from recommendation.recommendation import get_recommendations

@app_views.route("/load", methods=['Get'], strict_slashes=False)
def load_items():
    """load items"""
    token = request.headers.get('Authorization')
    user = storage.getuser_bytoken(token)
    if not user:
        abort(400,description="not a valid user")

    recomended_items = get_recommendations(user.id)
    most_recent_items = storage.get_most_recent_items()
    return make_response(jsonify(recomended_items + most_recent_items), 200)
