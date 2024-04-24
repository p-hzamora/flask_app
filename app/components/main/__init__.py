from flask import Blueprint

bp = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/main/static",
)

from app.components.main import routes  # noqa: E402, F401