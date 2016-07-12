from flask import render_template

from sample02.db import User


def setup_routes(app):
    """Here we map routes to handlers."""

    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/users', view_func=list_users)


def index():
    return render_template('base.html')


def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)
