import os

from config import Config, BASEDIR
from flask import Flask, url_for, redirect
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()


def create_app(configuration=Config):
    print(os.path.join(BASEDIR, 'templates'))
    app = Flask(__name__, template_folder=os.path.join(BASEDIR, 'templates'), static_folder=os.path.join(BASEDIR, 'static'))
    app.config.from_object(configuration)
    
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    from app.admin import bp as admin_bp
    from app.main import bp as main_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    @app.route("/")
    def index():
        return redirect(url_for("main.index"))

    return app