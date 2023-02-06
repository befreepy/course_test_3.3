from flask import Blueprint, render_template, request
from dao.dao import PostsDao

"""
создаем блюпринт main
"""
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')
posts = PostsDao('./data/posts.json', './data/comments.json')


"""
вывод формы на главной странице при обращении к /
"""


@main_blueprint.route('/')
def index_page():
    all_posts = posts.get_all_posts()
    return render_template('index.html', posts=all_posts)


"""
представление для одного поста 
"""


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    found_post = posts.get_post_by_pk(postid)
    comments = posts.get_comments_by_post_id(postid)
    return render_template('post.html', post=found_post, comments=comments)


"""
поиск и вывод постов при обращении на /search
"""


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    query = request.args.get('s')
    found_posts = posts.search_posts(query)
    return render_template('search.html', posts=found_posts)


"""
представление с выводом постов конкретного пользователя GET /users/<username>
"""


@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    user_post = posts.get_posts_by_username(username)
    return render_template('user-feed.html', posts=user_post, username=username)
