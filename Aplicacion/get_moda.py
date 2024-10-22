from flask import Flask, render_template, request, redirect, Blueprint

from .models import Post_Moda

from Aplicacion.auth import necesita_iniciar_sesion


bp = Blueprint("getpostmoda", __name__, url_prefix="/post-get-moda")



#* POST MODA
@bp.route('/post-moda')
def postModa():
    postModa = Post_Moda.query.all()
    return render_template('post_moda/index.html', postModa=postModa)


@bp.route('/ver-post/<url>', methods=["GET", "POST"])
def getmoda(url):
    postget = Post_Moda.query.filter_by(url=url).first()
    return render_template('post_moda/verpostModa.html', getmoda=postget)
