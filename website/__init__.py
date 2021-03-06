from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import path
from flask_login import LoginManager

# database
db = SQLAlchemy()
DB_NAME = "database.db"


def app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "fsht8thbgnvgfthre!jT%#K::5^uij0$g@"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize db
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    create_database(app)

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = "website.auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("DB created")
