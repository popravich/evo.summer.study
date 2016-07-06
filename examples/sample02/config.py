

def configure(app):
    """Here we can configure some parts of Flask Application"""
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:db.sqlite'
    app.config['SQLALCHEMY_ECHO'] = True

    app.config['SECRET_KEY'] = 'not-really-a-secret'
