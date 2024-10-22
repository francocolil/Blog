from flask import Flask, render_template, request, redirect, Blueprint

from .models import Post_Cortes,Post_Moda,Post_Temporadas

from Aplicacion.auth import necesita_iniciar_sesion


bp = Blueprint("post", __name__, url_prefix="/post")



@bp.route("/post")
@necesita_iniciar_sesion
def post():

    posCortes = Post_Cortes.query.all()
    postTemporadas = Post_Temporadas.query.all()
    postModa = Post_Moda.query.all()
    return render_template('auth/home.html', posCortes=posCortes, postTemporadas=postTemporadas, postModa=postModa)




#* CORTES
@bp.route("/post-cortes")
def postCortes():
    posCortes = Post_Cortes.query.all()
    return render_template('post_cortes/index.html', posCortes=posCortes)


@bp.route('/ver-post/<url>', methods=["GET", "POST"])
def getcortes(url):
    postget = Post_Cortes.query.filter_by(url=url).first()
    return render_template('post_cortes/verpost.html', getcortes=postget)
