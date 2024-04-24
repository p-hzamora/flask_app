import sys
from pathlib import Path
from flask import Flask

sys.path.append([str(x) for x in Path(__file__).parents if x.name == "flask_app"].pop())

from config import Config  # noqa: E402


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize Flask extension here

    # Register blueprints here
    from app.components.main import bp as main_bp
    from app.components.posts import bp as posts_bp
    from app.components.questions import bp as questions_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix="/posts")
    app.register_blueprint(questions_bp, url_prefix="/questions")

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app


# set/export FLASK_APP=app
# set/export FLASK_ENV=development
# flask run
# open http://127.0.0.1:5000/test/

app = create_app()
app.run(port=5003)
