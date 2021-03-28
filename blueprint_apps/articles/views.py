from flask import Blueprint, render_template, redirect, url_for
from blueprint_apps import db
from .models import Articles
from .forms import AddForm
from flask_login import login_required, current_user

from datetime import datetime

# pour synchroniser la view et le model
articles_app = Blueprint('articles', __name__, template_folder='templates')

# la view de l'article
@articles_app.route("/liste")
def articles():
    articles = Articles.query.all()
    titre = 'Blogar | articles'
    return render_template('articles/articles.html', titre = titre, articles = articles)

# la view pour ajouter un article
@articles_app.route('/ajouter', methods=['GET', 'POST'])
@login_required
def ajouter_article():
    form = AddForm()
    if form.validate_on_submit():
        titre = form.titre.data
        contenu = form.contenu.data
        article = Articles(titre, contenu, datetime.now(), current_user.id)
        db.session.add(article)
        db.session.commit()
        form.titre.data = ""
        form.contenu.data = ""
        return redirect(url_for('articles.articles'))
    titre = 'Blogar | ajouter'
    return render_template('articles/ajouter_article.html', titre = titre, form = form)

# la view pour supprimer un article
@articles_app.route('/supprimer/<int:id>')
def supprimer(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('index'))

# la view pour la modification des articles
@articles_app.route('/modification/<int:id>', methods=['GET', 'POST'])
def modification(id):
    form = AddForm()
    article = Articles.query.get(id)
    form.titre.data=article.titre
    form.contenu.data=article.contenu
    if form.validate_on_submit():
        form = AddForm()
        article.titre = form.titre.data
        article.contenu = form.contenu.data
        db.session.add(article)
        db.session.commit()
        form.titre.data, form.contenu.data = ("","")
        return redirect(url_for('index'))
    return render_template("articles/ajouter_article.html", form=form)


# la view pour lire la suite d'un article
@articles_app.route('/article_detail/<int:id>')
def article_detail(id):
    article = Articles.query.get(id)
    return render_template('articles/article_detail.html', article = article)


# @articles_app.route('/like/<int:post_id>/<action>')
# @login_required
# def like_action(post_id, action):
#     post = Post.query.filter_by(id=post_id).first_or_404()
#     if action == 'like':
#         current_user.like_post(post)
#         db.session.commit()
#     if action == 'unlike':
#         current_user.unlike_post(post)
#         db.session.commit()
#     return redirect(request.referrer)