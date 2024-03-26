#!/usr/bin/env python3
'''get recommendations for a user using a content-based filtering approach'''

from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
from models import storage
from models.user import User
from models.items import Item


def get_recommendations(user_id):
    '''get user recommendations based on his search history and favorites'''
    user = storage.get(User, user_id)
    if not user:
        return []

    search_history = [[search.name, ''] for search in user.searches]
    favorite = [[favorite.item.name, favorite.item.description]
                for favorite in user.favorites]
    data = search_history + favorite
    all_items = [[item['name'], item['description']]
                 for item in storage.all(Item)]

    encoder = OneHotEncoder()
    items_encoded = encoder.fit_transform(all_items)

    recommender = NearestNeighbors(metric='cosine')
    recommender.fit(items_encoded)
    recommended_items = []
    for item in data:
        try:
            item_encoded = encoder.transform([item])
            _, indicis = recommender.kneighbors(item_encoded, 5)
            recommendations = [all_items[i][0] + ':' + all_items[i][1]
                               for i in indicis[0]]
            recommended_items += recommendations
        except Exception:
            continue

    items_ids = []
    for item in recommended_items:
        name, description = item.split(':')
        item_id = storage.get_item_id(name, description)
        items_ids.append(item_id)
    return items_ids
