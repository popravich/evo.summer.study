"""
Module shows example how configuration can be loaded and validated.


"""
import pathlib
import yaml
import trafaret as t


def load_config(filename, trafaret=None):
    """Loads config file."""
    if not isinstance(filename, pathlib.Path):
        filename = pathlib.Path(filename)
    with filename.open('rt') as f:
        config = yaml.load(f)
    if trafaret is not None:
        return trafaret(config)
    return config


# Configuration trafaret
# Describes expected config structure and validators

config_trafaret = t.Dict({
    t.Key('flask'): t.Dict({
        t.Key('DEBUG', default=False): t.Bool,
        t.Key('SERVER_NAME'): t.String,
        }),
    t.Key('sqlalchemy', default=dict): t.Dict({
        t.Key('echo', default=False): t.Bool,
        t.Key('database_uri', default='sqlite:db.sqlite'): t.String,
        }),
    # Some Application-specific configs
    t.Key('app', default=dict): t.Dict({
        t.Key('login_attempts', default=10): t.Int[0:] | t.Null,
        }),
    })


def configure(app, config):
    """Here we can configure some parts of Flask Application"""

    # Setup config options from 'flask' section
    for key, value in config['flask'].items():
        app.config[key] = value

    # Setup config options from other sections, sqlalchemy for instance
    for key, value in config['sqlalchemy'].items():
        flask_key = 'SQLALCHEMY_{}'.format(key.upper())
        app.config[flask_key] = value
