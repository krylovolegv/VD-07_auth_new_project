from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app

