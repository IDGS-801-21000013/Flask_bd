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

class UserForm2(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre=StringField("Nombre", [validators.DataRequired(message="El nombre es requerido"), validators.length(min=4,max=20, message="Ingresa un nombre de entre 4 a 20 letras")])
    apaterno=StringField("Apellido Paterno", [validators.DataRequired(message="El campo es requerido"), validators.length(min=4,max=10, message="Ingresa un apellido de entre 4 y 10 letras")])
    amaterno=StringField("Apellido Materno", [validators.DataRequired(message="El campo es requerido"), validators.length(min=4,max=10, message="Ingresa un apellido de entre 4 y 10 letras")])
    email=EmailField("Email", [validators.DataRequired(message=("El campo es requerido")), validators.Email('Ingrese un correo valido') ])


