import flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from sample02.config import configure
from sample02.routes import setup_routes
from sample02.db import db


def main():
    app = flask.Flask(__name__)

    configure(app)
    setup_routes(app)

    db.init_app(app)
    toolbar = DebugToolbarExtension(app)
    app.run()
