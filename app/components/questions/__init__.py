from flask import Blueprint

bp = Blueprint("questions", __name__, template_folder="templates")

from . import routes  # noqa: E402, F401