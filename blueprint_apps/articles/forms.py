from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import InputRequired

# creer les forms d'articles
class AddForm(FlaskForm):
    titre       = wtforms.StringField("titre",validators=[InputRequired()])
    contenu     = wtforms.TextAreaField("contenu" ,validators=[InputRequired()])
    submit      = wtforms.SubmitField("Publier")