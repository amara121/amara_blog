from blueprint_apps import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from blueprint_apps.articles import models

# verifie si un utilisateur est connectée
@login_manager.user_loader
def load_user(user_id):
    return Utilisateurs.query.get(user_id)

# creer la table utilisateur dans la base de donnée
class Utilisateurs(db.Model, UserMixin):
    # __tablename__ = 'users'
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(64), unique=True, index=True)
    email           = db.Column(db.String(64), unique=True, index=True)
    password_hashed = db.Column(db.String(128))
    articles        = db.relationship("Articles",uselist=True, backref="Utilisateurs", cascade="all, delete")
    articles_like   = db.relationship("Articles",uselist=True)
    # liked = db.relationship(
    #     'PostLike',
    #     foreign_keys='PostLike.user_id',
    #     backref='utlisateurs', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hashed = generate_password_hash(password)
    def __repr__(self):
        return str(self.username)

    def check_password(self, password):
        return check_password_hash(self.password_hashed, password)

    @classmethod
    def check_email(cls, email):
        return cls.query.filter_by(email=email).count() > 0


    def like_post(self, articles):
        if not self.has_liked_post(articles):
            like = PostLike(user_id=self.id, post_id=articles.id)
            db.session.add(like)

    def unlike_post(self, articles):
        if self.has_liked_post(articles):
            PostLike.query.filter_by(
                user_id=self.id,
                post_id=articles.id).delete()

    def has_liked_post(self, articles):
        return PostLike.query.filter(
            PostLike.user_id == self.id,
            PostLike.post_id == articles.id).count() > 0


# class PostLike(db.Model):
#     __tablename__ = 'post_like'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'))
#     post_id = db.Column(db.Integer, db.ForeignKey('articles.id'))