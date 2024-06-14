from flask import Blueprint
from flask import render_template

bp = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/main/static",
)

@bp.route("/")
def index():
    return render_template("index.html")