from flask import (
    Blueprint, 
    redirect,
    render_template,
    request,
    url_for,
    )

from board.database import get_db

bp = Blueprint("posts", __name__)

# @bp.route("/create", methods=("GET", "POST"))
# def create():
#     return render_template("posts/about")


# @bp.route("/posts")
# def posts():
#     posts = []
#     return render_template("posts/posts.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUEs (?, ?)",
                (author, message),
            )
            db.commit()
            return redirect(url_for("posts.posts"))
            
    return render_template("posts/create.html")


@bp.route("/posts")
def posts():
    posts = []
    return render_template("posts/posts.html", posts=posts)
