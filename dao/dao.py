import json
from dao.post import Post


class PostsDao:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    """
    загружает посты
    """
    def load_posts(self):
        with open(self.posts_path, "r", encoding="utf-8") as file:
            new_posts = []
            posts_data = json.load(file)
            for post in posts_data:
                new_posts.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]))
        return new_posts

    """
    загружает посты из json
    """
    def load_posts_json(self):
        with open(self.posts_path, "r", encoding="utf-8") as file:
            posts_data = json.load(file)

        return posts_data

    def load_comments(self):
        with open(self.comments_path, "r", encoding="utf-8") as file:
            comments = json.load(file)
        return comments

    """
    возвращает посты
    """
    def get_all_posts(self):
        return self.load_posts()

    """
    возвращает посты определенного пользователя
    """
    def get_posts_by_username(self, username):
        posts = self.load_posts()
        user_posts = []
        try:
            for post in posts:
                if post.poster_name.lower() == username.lower():
                    user_posts.append(post)
        except ValueError:
            return 'такого пользователя нет'

        return user_posts

    """
    возвращает комментарии определенного поста
    """
    def get_comments_by_post_id(self, post_id):
        comments = self.load_comments()
        post_comments = []
        try:
            for comment in comments:
                if comment['post_id'] == post_id:
                    post_comments.append(comment)
        except ValueError:
            return 'Такого поста нет'

        return post_comments

    """
    возвращает список постов по ключевому слову
    """
    def search_posts(self, substr):
        posts = self.load_posts()
        new_posts = []

        for post in posts:
            if substr.lower() in post.content.lower():
                new_posts.append(post)
        return new_posts

    """
    возвращает один пост по его идентификатору
    """
    def get_post_by_pk(self, pk):
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post
        return

    def get_post_by_pk_json(self, pk):
        posts = self.load_posts_json()
        for post in posts:
            if post['pk'] == pk:
                return post
        return
