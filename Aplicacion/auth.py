from flask import Flask, render_template, request, redirect, g, session, url_for, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User, Post_Cortes,Post_Moda,Post_Temporadas

from Aplicacion import db


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None

        user = User(username, generate_password_hash(password))

        user_name = User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f"El usuario {username} ya existe"

        flash(error)
        

    return render_template("auth/register.html")



@bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None

        user = User.query.filter_by(username=username).first()

        if user == None or not check_password_hash(user.password, password):
            error = "El usuario o contraseña son ERRONEAS"

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('post.post'))

    return render_template("auth/login.html")


@bp.before_app_request
def inicio_sesion():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


import functools

def necesita_iniciar_sesion(view):
    @functools.wraps(view)
    def paginas_que_puede_ver(**kwars):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwars)
    return paginas_que_puede_ver