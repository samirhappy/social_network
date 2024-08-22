import json

POST_PATH = "posts.json"


def load_from_json():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def upload_f(posts1):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts1, file, indent=4)
