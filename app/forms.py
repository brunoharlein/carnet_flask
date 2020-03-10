"""Module to hold the different forms for the application"""
"""Module pour contenir les différents formulaires de candidature"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp

from .models import User

# Note that each form corresponds to an entities from the model
# Notez que chaque formulaire correspond à une entité du modèle
# Form fields are defiened by class attributs holding object of the correspnding type field
# Les champs de formulaire sont définis par des attributs de classe contenant un objet du champ de type correspondant

class NewThoughtForm(FlaskForm):
    """Class to generate a form to add a thought to the database"""
    """Classe pour générer un formulaire pour ajouter une pensée à la base de données"""
    content = StringField('Citation', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')
