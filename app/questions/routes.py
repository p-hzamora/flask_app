from app.questions import bp
from app.extesions.database import db

from .models.user import ClientModel

from flask import render_template, request, jsonify, abort


@bp.route("/")
def index():
    return render_template("questions/index.html")


@bp.route("/submit-answer", methods=["POST"])
def submit_answer():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        user = (
            ClientModel(db)
            .filter_by(lambda x: x.name, username)
            .filter_by(lambda x: x.password, password)
            .get(flavour=dict)
        )

        if not user:
            return jsonify(
                {"status": False, "error_mssg": "usuario o contraseña incorrectos"}
            ), 404
        return jsonify(user)
    abort(405)


@bp.errorhandler(405)
def page_not_found(error):
    return f"<h1>Error {error}. Usuario no registrado</h1>", 405
