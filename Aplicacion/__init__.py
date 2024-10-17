from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

db = SQLAlchemy()


def run_app():

    app = Flask(__name__)

    ckeditor = CKEditor(app)

    app.config.from_object('config.Config')

    db.init_app(app)


    #* RUTAS
    from . import auth
    app.register_blueprint(auth.bp)

    from . import post_general
    app.register_blueprint(post_general.bp)

    from . import post_cortes
    app.register_blueprint(post_cortes.bp)

    from . import post_moda
    app.register_blueprint(post_moda.bp)

    from . import post_temporada
    app.register_blueprint(post_temporada.bp)


    @app.route("/")
    def index():
        return render_template("index.html")
    

    with app.app_context():
        db.create_all()

    return app