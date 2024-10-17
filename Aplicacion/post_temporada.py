from flask import Flask, render_template, request, redirect, g, session, url_for, Blueprint, flash

from .models import User, Post_Temporadas

from Aplicacion import db

from Aplicacion.auth import necesita_iniciar_sesion


bp = Blueprint("posttemporada", __name__, url_prefix="/post-temporada")


@bp.route("/post-temporada", methods=["GET", "POST"])
@necesita_iniciar_sesion
def create():

    if request.method == "POST":
        title = request.form.get("title")
        url = request.form.get('url')
        url = url.replace(' ', '-')
        desc = request.form.get('ckeditor')

        postcortes = Post_Temporadas(g.user.id, title, url, desc)

        error = None

        #* Comprobar si la url existe
        post_url = Post_Temporadas.query.filter_by(url=url).first()
        if post_url == None:
            db.session.add(postcortes)
            db.session.commit()
            flash(f"El POST {postcortes.title} se registro correctamente")
            return redirect(url_for('post.post'))
        
        else:
            error = f"Esa URL {url} ya esta registrada"

    return render_template("post_moda/create.html")


#* Obtener id del POST
def tener_id(id):
    post_temporadas = Post_Temporadas.query.get_or_404(id)
    return post_temporadas


#* Eliminar POST
@bp.route("/delete/<int:id>")
def delete(id):
    
    post_temporadas = tener_id(id)

    db.session.delete(post_temporadas)
    db.session.commit()
    return redirect(url_for('post.post'))


#* Editar POST
@bp.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):

    post_temporadas = tener_id(id)

    if request.method == "POST":
        post_temporadas.title = request.form.get("title")
        post_temporadas.url = request.form.get('url')
        post_temporadas.url = post_temporadas.url.replace(' ', '-')
        post_temporadas.desc = request.form.get('ckeditor')

        db.session.commit()
        return redirect(url_for('post.post'))
    
    return render_template('post_temporadas/update.html', post_temporadas=post_temporadas)