from flask import Flask, render_template, request, flash, g
from forms import UserForm, UserForm2
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db   
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
        

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/index", methods=["GET", "POST"])
def index():
    alumno = UserForm2(request.form)

    if request.method == "POST":
        alumnoObj = Alumnos(
            id=alumno.id.data,
            nombre=alumno.nombre.data,
            apaterno=alumno.apaterno.data,
            amaterno=alumno.amaterno.data,
            email=alumno.email.data
        )
        db.session.add(alumnoObj)
        db.session.commit()

    return render_template("index.html", form=alumno)



@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    alumno_clase = UserForm(request.form)
    nombre = None
    a_paterno = None
    a_materno = None
    email = None
    edad = None
    
    if request.method == "POST" and alumno_clase.validate():
        nombre = alumno_clase.nombre.data
        a_paterno = alumno_clase.a_paterno.data
        a_materno = alumno_clase.a_materno.data
        email = alumno_clase.email.data
        edad = alumno_clase.edad.data
        
        print(f"Nombre: {nombre} {a_paterno} {a_materno} Email: {email} Edad: {edad}")


    return render_template("alumnos.html",form=alumno_clase,nombre=nombre,a_paterno=a_paterno,a_materno=a_materno,email=email,edad=edad)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()    
    app.run()
