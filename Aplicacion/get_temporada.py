from flask import Flask, render_template, request, redirect, Blueprint

from .models import Post_Temporadas

from Aplicacion.auth import necesita_iniciar_sesion


bp = Blueprint("getposttemporada", __name__, url_prefix="/post-get-temporada")



@bp.route('/post-temporada')
def postTemporada():
    postTemporada = Post_Temporadas.query.all()
    return render_template('post_temporadas/index.html', postTemporada=postTemporada)

@bp.route('/ver-post/<url>')
def gettemporada(url):
    postget = Post_Temporadas.query.filter_by(url=url).first()
    return render_template('post_temporadas/verposttemporada.html', gettemporada=postget)