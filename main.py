from flask import Flask, request, render_template

from utils import get_posts_all, get_posts_by_user, get_post_by_pk, search_for_posts, get_comments_by_post_id, get_posts_by_tag

app = Flask(__name__)


@app.route("/")
def page_index():

    posts = get_posts_all()
    return render_template("index.html", posts=posts)



@app.route("/posts/<int:post_id>")
def page_post(post_id):

    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_count = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)


@app.route("/search")
def page_search():
    query = request.args.get("s")
    if query == None or query == "":
        return "Параметры для поиска не заданы"

    posts = search_for_posts(query)
    posts_count = len(posts)

    return render_template("search.html", posts=posts, posts_count=posts_count, query=query)


@app.route("/users/<user_name>")
def page_posts_by_user(user_name):
    posts = get_posts_by_user(user_name)
    posts_count = len(posts)

    return render_template("user-feed.html", posts=posts, posts_count=posts_count, user_name=user_name)


@app.route("/tag")
def page_tag():
    tag_name = request.args.get("tag")
    posts = get_posts_by_tag(tag_name)
    return render_template("tag.html", posts=posts, tag_name=tag_name)


if __name__ == "__main__":
    app.run()