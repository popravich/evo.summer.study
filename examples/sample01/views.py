from flask import render_template, request


def setup_routes(app):
    """Here we map routes to handlers."""

    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/template', view_func=show_template)
    app.add_url_rule('/user/<name>', view_func=request_args)
    app.add_url_rule('/args', view_func=request_args)


def index():
    return "Index"


def show_template():
    return render_template('sample.html')


def request_args(name=None):
    print(request.args)
    return render_template('request_args.html',
                           name=name, args=request.args)
