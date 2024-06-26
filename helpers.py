#!/usr/bin/python3
'''helpers functions'''
import os
import base64
import imghdr
from werkzeug.utils import secure_filename


def save_image(data, dir):
    '''save image'''
    pic = data['picture']
    if pic.startswith("data:image/jpeg;base64,"):
        pic = pic[len("data:image/jpeg;base64,"):]
    pic_binary = base64.b64decode(pic)
    image_extension = imghdr.what(None, pic_binary)

    if 'email' in data:
        name = data['email'].replace("@", "_").replace(".", "_")
    elif 'price' in data:
        name = data['name'].replace(" ", "_")
        name += str(data['price']).replace(" ", "_")
        name += str(data['user_id']).replace(" ", "_")
    else:
        name = data['name'].replace(" ", "_")
    name = f"{name}.{image_extension}" if image_extension else f"{name}.jpg"
    os.makedirs(os.path.expanduser(dir), exist_ok=True)
    file_name = os.path.join(
        os.path.expanduser(dir), name)

    with open(file_name, "wb") as file:
        file.write(pic_binary)
    return str(name)


def save_file(data, file, dir):
    '''save items and users pictures'''
    image_extension = secure_filename(file.filename).split('.')[-1]
    if 'email' in data:
        name = data['email'].replace("@", "_").replace(".", "_")
    elif 'price' in data:
        name = data['name'].replace(" ", "_")
        name += str(data['price']).replace(" ", "_")
        name += str(data['user_id']).replace(" ", "_")
    file_name = f"{name}.{image_extension}"
    file_path = os.path.join(dir, file_name)
    file.save(file_path)
    return str(file_name)
