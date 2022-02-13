import json
import pprint

def get_posts_all():
    """
    Получить все посты из жсона
    :return: посты или пустой список, если постов в файле нет
    """
    with open("data/data.json", "r", encoding="utf-8") as file_posts:
        posts = json.load(file_posts)

        if posts:
            return posts
        return []



def get_posts_by_user(user_name):
    """
    Получить все посты, сделанные одним юзером
    :param user_name: имя пользователя
    :return: посты, сделанные пользователем с указанным юзером
    """
    posts = get_posts_all()

    posts_by_user = []

    for post in posts:
        if user_name == post["poster_name"]:
            posts_by_user.append(post)

    return posts_by_user


def search_for_posts(query):
    """
    Получить все посты, которые содержат искомый текст
    :param query: искомый текст
    :return: все посты, которые содержат искомый текст
    """
    posts = get_posts_all()
    posts_matching = []

    for post in posts:
        if query in post["content"]:
            posts_matching.append(post)

    return posts_matching



def get_post_by_pk(pk):
    """
    Получить один пост по его айди
    :param pk: айди поста
    :return: пост
    """
    posts = get_posts_all()

    for post in posts:
        if pk == post["pk"]:
            return post



def get_comments_all():
    """
    Получить все комментарии из жсон файла
    :return: комментарии
    """
    with open("data/comments.json", "r", encoding="utf-8") as f:
        comments = json.load(f)
        return comments



def get_comments_by_post_id(post_id):
    """
    Получить комментарии к определенному посту по его айди
    :param post_id: айди поста
    :return: комментарии
    """
    comments = get_comments_all()

    matching_comments = []
    for comment in comments:
        if comment["post_id"] == post_id:
            matching_comments.append(comment)

    return matching_comments


def get_posts_by_tag(tag_name):
    """
    Получить посты, которые содержат указанный тег
    :param tag_name: тег
    :return: все подходящие посты
    """

    posts = get_posts_all()
    posts_matching = []
    search_for = f"#{tag_name}"

    for post in posts:
        if search_for in post.get("content"):
            posts_matching.append(post)
    return posts_matching



