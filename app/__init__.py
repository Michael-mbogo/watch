from flask import Flask
# from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstarp = Bootstrap()

def create_app(config_name):
    #initializing app
    app = Flask(__name__,instance_relative_config = True)

    #creating app configuration
    app.config.from_object(config_options[config_name])


    #initializing flask ext
    bootstrap.init_app(app)

    #registering a blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # #setting up configuration
    from .request import configure_request
    configure_request(app)


    #will ad views and forms

    return app
