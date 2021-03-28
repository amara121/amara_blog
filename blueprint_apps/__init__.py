import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# instancié login manager a la variable login_manager grace (from flask_login import LoginManager)
# LoginManager permettre de geré la connexion du site soit verifié si un utilisateur est connecté ou pas
login_manager = LoginManager()

# creer le chemin de notre base de donnée grace (import os)
chemin = os.path.abspath(os.path.dirname(__file__))

# instancié la classe Flask a la variable app grace (from flask import Flask)
app = Flask(__name__)

# la configuration de la clée secrete de notre site
app.config['SECRET_KEY'] = 'secret!!!!!'

# la configuration pour indiquer la route pour connecter notre application a notre base de donnée sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(chemin, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# lier notre application a SQLALCHEMY pour pouvoir modifier les elements dans la base de donnée grace (from flask_sqlalchemy import SQLAlchemy)
db = SQLAlchemy(app)

# Migrate comme le nom le dit c' est pour la migration de l'application et le db (sqlalchemy), le faite de creer des tables dans notre base de donnée grace (from flask_migrate import Migrate)
Migrate(app, db)

# permettre de lier la connexion a notre site
login_manager.init_app(app)
login_manager.login_message="Veuillez vous connecter pour accéder à cette page"
login_manager.login_view = 'utilisateurs.connexion' # la chemin de caractere est une fonction, permet de obligé les utilisateur a se connecté avant d'avoir certain fonctionnaliter

# importer les views de article et utilisateur
from blueprint_apps.articles.views import articles_app
from blueprint_apps.utilisateurs.views import utilisateurs_app

#enregistrer les deux views importer et ajouter un prefixe sur le nom de la view
app.register_blueprint(articles_app, url_prefix='/articles')
app.register_blueprint(utilisateurs_app, url_prefix='/utilisateurs')
