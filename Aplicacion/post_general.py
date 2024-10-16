from flask import Flask, render_template, request, redirect, Blueprint

from .models import User, Post_Cortes,Post_Moda,Post_Temporadas

from Aplicacion.auth import necesita_iniciar_sesion


bp = Blueprint("post", __name__, url_prefix="/post")



@bp.route("/post")
@necesita_iniciar_sesion
def post():

    postModa = Post_Moda.query.all()
    posCortes = Post_Cortes.query.all()
    posTemporadas = Post_Temporadas.query.all()

    return render_template('auth/home.html')