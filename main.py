from flask import Flask, redirect, render_template, request, flash, g, url_for
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
    alumnos = UserForm2(request.form)

    if request.method == "POST":
        alumnoObj = Alumnos(
            id=alumnos.id.data,
            nombre=alumnos.nombre.data,
            apaterno=alumnos.apaterno.data,
            amaterno=alumnos.amaterno.data,
            email=alumnos.email.data
        )
        db.session.add(alumnoObj)
        db.session.commit()

    return render_template("index.html", form=alumnos)

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

@app.route("/ABC_Completo", methods=["GET","POST"])
def ABC_Completo():
    alumno_form= UserForm2(request.form)
    alumnoObj = Alumnos.query.all()
    return render_template("ABC_Completo.html", alumno=alumno_form, alumnos=alumnoObj)

@app.route("/eliminar", methods=["GET","POST"])
def eliminar():
    alumno_form= UserForm2(request.form)
    if request.method == "GET":

        id = request.args.get("id")
        alumnoObj = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumno_form.id.data = request.args.get("id")
        alumno_form.nombre.data = alumnoObj.nombre
        alumno_form.apaterno.data = alumnoObj.apaterno
        alumno_form.amaterno.data = alumnoObj.amaterno
        alumno_form.email.data = alumnoObj.email
    if request.method == "POST":
        id = request.form["id"]
        alum = Alumnos.query.filter_by(id=id).first()
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("ABC_Completo"))
    return render_template("eliminar.html", form=alumno_form)

@app.route("/editar", methods=["GET","POST"])
def editar():
    alumno_form= UserForm2(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alumnoObj = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumno_form.id.data = request.args.get("id")
        alumno_form.nombre.data = alumnoObj.nombre
        alumno_form.apaterno.data = alumnoObj.apaterno
        alumno_form.amaterno.data = alumnoObj.amaterno
        alumno_form.email.data = alumnoObj.email
    if request.method == "POST":
        try:
            id = alumno_form.id.data
            alumnoObj = Alumnos.query.filter_by(id=id).first()
            alumnoObj.nombre = alumno_form.nombre.data  
            alumnoObj.apaterno = alumno_form.apaterno.data
            alumnoObj.amaterno = alumno_form.amaterno.data
            alumnoObj.email = alumno_form.email.data
            db.session.commit()
        except Exception as e:
            print(f"Error en la actualizacion: {e}")
            db.session.rollback()
        return redirect(url_for("ABC_Completo"))
    
    return render_template("editar.html", form=alumno_form)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()    
    app.run()
