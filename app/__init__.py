from flask import Flask, app
from config import config_options
from flask_bootstrap import Bootstrap, bootstrap_find_resource
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    # Will add the views and forms

    return app

# # Initializing application
# app = Flask(__name__,instance_relative_config = True)

# # setting up configuration
# app.config.from_object(config_options[config_name])
# app.config.from_pyfile("config.py")

# # Initiliazing Flask Extensions
# bootstrap = Bootstrap(app)

# from . import views
# from . import error