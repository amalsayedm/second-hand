#!/usr/bin/python3
""" objects that handle all default RestFul locations apis"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.locations import Location


@app_views.route('/locations', methods=['GET'], strict_slashes=False)
def get_locations():
    """get all locations"""
    all_locations = storage.all(Location)
    return make_response(jsonify(all_locations), 200)
