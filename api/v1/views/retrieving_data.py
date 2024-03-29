#!/usr/bin/python3
"""loading items"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User
from recommendation.recommendation import get_recommendations
from models.items import Item

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

    
    
        
        
    