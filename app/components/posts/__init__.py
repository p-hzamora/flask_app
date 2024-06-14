from flask import Blueprint
from app.extesions.database import db

from .models import CityModel, City

from flask import render_template

bp = Blueprint(
    "posts",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/posts",
)


@bp.route("/")
def index():
    model: list[City] = CityModel(db).select()
    return render_template("posts/index.html", cities=model)


@bp.route("/categories")
def categories():
    return render_template("posts/categories.html")
