from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()


def run_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATA_BASE')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import post_general
    app.register_blueprint(post_general.bp)


    @app.route("/")
    def index():
        return render_template("index.html")
    

    with app.app_context():
        db.create_all()

    return app