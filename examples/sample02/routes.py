from . import views


def setup_routes(app):
    """Here we map routes to handlers."""

    app.add_url_rule('/', view_func=views.index)
    app.add_url_rule('/users', view_func=views.list_users)
