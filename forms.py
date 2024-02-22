from wtforms import Form
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField
from wtforms import EmailField
# Aqui agregaremos los campos que sean obligatorios y el email
from wtforms.validators import DataRequired, Email, Length

class UserForm(Form):
    
    nombre=StringField("Nombre", [validators.DataRequired(message="El campo es requerido"), validators.length(min=4,max=10, message="Ingresa uun nombre valido")])
    a_paterno=StringField("Apellido Paterno", [validators.DataRequired(message="El campo es requerido"), validators.length(min=4,max=10, message="Ingresa un apellido valido")])
    a_materno=StringField("Apellido Materno", [validators.DataRequired(message="El campo es requerido"), validators.length(min=4,max=10, message="Ingresa un apellido valido")])
    email=EmailField("Email", [validators.DataRequired(message="El campo es requerido") ])
    edad=IntegerField("Edad", [validators.DataRequired(message="EL campo es requerido") ])




