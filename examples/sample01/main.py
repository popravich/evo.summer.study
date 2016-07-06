import flask

from .config import configure
from .routes import setup_routes


def main():
    app = flask.Flask(__name__)

    configure(app)
    setup_routes(app)

    app.run()
