from flask import Flask
# from app.models import db
from myenv.app.controller.controller import bp as main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.confilg/Config')

    # db.init_app(app) # Init extensions

    app.register_blueprint(main_bp) # regis blueprints