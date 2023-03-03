from dao.dao import PostsDao
from app import app

posts = PostsDao('./data/posts.json', './data/comments.json')

keys_should_be = {
    'poster_name',
    'poster_avatar',
    'pic',
    'content',
    'views_count',
    'likes_count',
    'pk'
}

"""
тестируем эндпоинт GET /api/posts
"""


def test_api_all_posts():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys_should_be


"""
тестируем эндпоинт GET /api/posts/<post_id>
"""


def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response.keys()) == keys_should_be
