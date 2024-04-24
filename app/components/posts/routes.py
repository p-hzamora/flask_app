from app.extesions.database import db

from . import bp
from .models.post import PostModel

from flask import render_template


@bp.route("/")
def index():
    model = PostModel(db).all(dict)
    print(model)
    return render_template("posts/index.html", post=model)


@bp.route("/categories")
def categories():
    return render_template("posts/categories.html")