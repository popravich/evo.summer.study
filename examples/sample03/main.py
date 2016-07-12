import argparse
import pathlib
import flask

from sample03.config import load_config, config_trafaret, configure
from sample03.views import setup_routes
from sample03.db import db


def get_parser():
    PROJ_DIR = pathlib.Path(__file__).parent

    ap = argparse.ArgumentParser("Sample app parser")

    ap.add_argument('-p', '--port', default=5000,
                    help="Port to bind to, default: %(default)s")
    ap.add_argument('-c', '--config', dest='config_file',
                    default=PROJ_DIR / 'config' / 'sample.yaml',
                    type=pathlib.Path,
                    help="Configuration file path, default `%(default)s`")
    return ap


def main(argv=None):
    ap = get_parser()
    options = ap.parse_args(argv)
    config = load_config(options.config_file, config_trafaret)

    app = flask.Flask(__name__)

    configure(app, config)
    setup_routes(app)

    db.init_app(app)
    app.run(port=options.port)
