from blueprint_apps import db
from blueprint_apps.utilisateurs.models import Utilisateurs

# creer la table articles dans la base de donnée
class Articles(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    titre   = db.Column(db.Text)
    contenu = db.Column(db.Text)
    date    = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'))
    user    = db.relationship("Utilisateurs")
    # like    = db.relationship("Utilisateurs",uselist=True)
    # likes = db.relationship('PostLike', backref='articles', lazy='dynamic')

    # like      = db.Column(db.Integer, default = 0)


    def __init__(self, titre, contenu, date, user_id):
        self.titre   = titre
        self.contenu = contenu
        self.date    = date
        self.user_id = user_id

    def __repr__(self):
        return str(self.titre)


