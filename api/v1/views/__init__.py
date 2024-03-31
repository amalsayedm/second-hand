#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from api.v1.views.users import *
from api.v1.views.items import *
from api.v1.views.followers import *
from api.v1.views.categories import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
