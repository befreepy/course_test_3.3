import datetime
import logging

from flask import jsonify, Blueprint

from dao.dao import PostsDao

"""
создаем блюпринт api
"""
api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsDao('./data/posts.json', './data/comments.json')

"""
логируем обращения к эндпоинтам API
"""
logging.basicConfig(filename='./logs/basic.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

"""
Создаем представление, которое обрабатывает запрос GET /api/posts и возвращает полный список постов в виде JSON-списка.
"""


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info('Запрос /api/posts/')
    res = posts.load_posts_json()
    return jsonify(res)


"""
Создаем представление, которое обрабатывает запрос GET /api/posts/<post_id> и возвращает один пост в виде JSON-словаря.
"""


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/{postid}')
    return jsonify(posts.get_post_by_pk_json(postid))
