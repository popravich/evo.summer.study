import flask
from flask_debugtoolbar import DebugToolbarExtension

from sample02.config import configure
from sample02.views import setup_routes
from sample02.db import db


def main():
    app = flask.Flask(__name__)

    configure(app)
    setup_routes(app)

    db.init_app(app)
    DebugToolbarExtension(app)
    app.run()
