from blueprint_apps import app
from flask import render_template, Request
from blueprint_apps.articles.models import Articles




# la view de ma page principale (index)
@app.route('/')
def index():
    articles = Articles.query.all()[0:2]
    titre = 'Blogar | Accueil'
    return render_template('index.html', titre = titre, articles = articles)

# la view de la page, lorsqué utilisateur rechercher une page qui n'exise pas
@app.errorhandler(404)
def page_not_fonud(erro):
    return render_template('404.html'), 404



if __name__=='__main__':
    app.run(debug=True)
