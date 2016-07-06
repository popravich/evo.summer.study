from flask import render_template, request

from sample02.db import User


def index():
    return render_template('base.html')


def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)
