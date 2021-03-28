from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Email, EqualTo
from .models import Utilisateurs


# la form de l'inscription
class InscriptionForm(FlaskForm):
    username             = wtforms.StringField("Votre nom", validators=[DataRequired()])
    email                = wtforms.StringField("Votre Email", validators=[DataRequired(), Email()])
    password             = wtforms.PasswordField("Creer mot de passe", validators=[DataRequired(), EqualTo("password_confirm")])
    password_confirm     = wtforms.PasswordField("Confirmer le mot de passe", validators=[DataRequired()])
    submit               = wtforms.SubmitField("S'inscrire")
    
    def check_email(self, field):
        if Utilisateurs.query.filter_by(email=field.data).first():
            raise wtforms.ValidationError('Cette adresse mail existe déja!!!')
    def check_username(self, field):
        if Utilisateurs.query.filter_by(username=field.data).first():
            raise wtforms.ValidationError('Cet utilisateur existe déja!!!')


# la form de la connexion
class ConnexionForm(FlaskForm):
    username     = wtforms.StringField("Nom utilisateur", validators=[DataRequired()])
    password     = wtforms.PasswordField("Mot de passe", validators=[DataRequired()])
    submit       = wtforms.SubmitField("Se connecter")
