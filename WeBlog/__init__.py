from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "prince_blog"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    from.views import views
    from.auth import auth

    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")

    from .models import User
    
    create_database(app)    

    return app


def create_database(app):
    if not path.exists("WeBlog/"+DB_NAME):
        with app.app_context():
            db.create_all()
        print("database created")

# iam creating this init file to convert this folder into a python package so when ever i need it i can just import it  
