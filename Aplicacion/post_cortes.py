from flask import Flask, render_template, request, redirect, g, session, url_for, Blueprint, flash

from .models import User, Post_Cortes

from Aplicacion import db

from Aplicacion.auth import necesita_iniciar_sesion


bp = Blueprint("postcortes", __name__, url_prefix="/post-cortes")


#* Obtener fotos
from werkzeug.utils import secure_filename


@bp.route("/post-cortes", methods=["GET", "POST"])
@necesita_iniciar_sesion
def create():

    if request.method == "POST":
        title = request.form.get("title")
        url = request.form.get('url')
        url = url.replace(' ', '-')
        desc = request.form.get('ckeditor')

        postcortes = Post_Cortes(g.user.id, title, url, desc)

        error = None

        #* Comprobar si la url existe
        post_url = Post_Cortes.query.filter_by(url=url).first()
        if post_url == None:
            db.session.add(postcortes)
            db.session.commit()
            flash(f"El POST {postcortes.title} se registro correctamente")
            return redirect(url_for('post.post'))
        
        else:
            error = f"Esa URL {url} ya esta registrada"

    return render_template("post_cortes/create.html")