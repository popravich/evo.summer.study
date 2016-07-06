from flask import render_template, request


def index():
    return "Index"


def show_template():
    return render_template('sample.html')


def request_args(name=None):
    print(request.args)
    return render_template('request_args.html',
                           name=name, args=request.args)
