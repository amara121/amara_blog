from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from blueprint_apps import db
from flask_login import login_user, login_required, logout_user
from .forms import ConnexionForm, InscriptionForm
from blueprint_apps.utilisateurs.models import Utilisateurs



utilisateurs_app = Blueprint('utilisateurs', __name__, template_folder='templates/utilisateurs')


@utilisateurs_app.route("/connexion", methods=['GET', 'POST'])
def connexion():
    form =ConnexionForm()
    if form.validate_on_submit():
        utilisateur = Utilisateurs.query.filter_by(username = form.username.data).first()
        if utilisateur is not None:
            if utilisateur.check_password(form.password.data):
                login_user(utilisateur)
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('index')
                return redirect(next)
            else:
                flash("mot de passe incorrect !!!")
        else:
            flash("L'utilisateur n'existe pas")

    titre='Blogar|connexion'
    return render_template('connexion.html', titre=titre, form=form)

@utilisateurs_app.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    flash("Vous etes déconnecté")
    return redirect(url_for('index'))




@utilisateurs_app.route("/inscription", methods=['GET', 'POST'])
def inscription():
    form = InscriptionForm()
    if form.validate_on_submit():
        utilisateurs=Utilisateurs(email=form.email.data, username=form.username.data,
                                 password=form.password.data)
        if not Utilisateurs.check_email(form.email.data):
            db.session.add(utilisateurs)
            db.session.commit()
            flash("merci pour votre inscription")
            return redirect(url_for("utilisateurs.connexion"))
        else:
            flash("bbbhdfbhf")
    titre='Blogar|inscription'
    return render_template('inscription.html', titre=titre, form=form)

