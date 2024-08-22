from flask import render_template, request, Blueprint
from functions import load_from_json
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(encoding='utf-8', level=logging.INFO)


@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search():
    search_by = request.args['s']
    logging.info(f'Файл для поиска: {search_by}')
    posts = [x for x in load_from_json() if search_by.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by=search_by, posts=posts)
