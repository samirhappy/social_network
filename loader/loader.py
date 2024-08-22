from flask import render_template, request, Blueprint
from functions import load_from_json, upload_f
import logging

load_blueprint = Blueprint('load_blueprint', __name__, url_prefix='/post', static_folder='static',
                           template_folder='templates')
logging.basicConfig(encoding='utf-8', level=logging.INFO)


@load_blueprint.route('/form/')
def form():
    return render_template('post_form.html')


@load_blueprint.route('/uploaded/', methods=['POST'])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_from_json()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        upload_f(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split('.'[-1]) not in ['png', 'jpeg', 'jpg']:
            logging.info('Файл не изображение')
    except FileNotFoundError:
        return "<h1> Файл не найден </h1>"
        logging.error('Ошибка при загрузке файла')
    else:
        return render_template('post_uploaded.html', pic=f"/uploads/images/{filename}", content=content)
