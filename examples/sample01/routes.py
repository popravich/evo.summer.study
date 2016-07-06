from . import views


def setup_routes(app):
    """Here we map routes to handlers."""

    app.add_url_rule('/', view_func=views.index)
    app.add_url_rule('/template', view_func=views.show_template)
    app.add_url_rule('/user/<name>', view_func=views.request_args)
    app.add_url_rule('/args', view_func=views.request_args)
