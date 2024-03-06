from flask import Flask,render_template,request,Response
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import g
from config import DevelopmentConfig
from flask import flash
import forms

from models import db
from models import Empleados
from models import PedidosPizza

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'),404


@app.route("/index",methods=["GET","POST"])
def index():    
    emp_form=forms.EmpleadosForm(request.form)
    if request.method=='POST':
        emp=Empleados(nombre=emp_form.nombre.data,
                      correo=emp_form.correo.data,
                      telefono=emp_form.telefono.data,
                      direccion=emp_form.direccion.data,
                      sueldo=emp_form.sueldo.data)
        db.session.add(emp)
        db.session.commit()
    return render_template("index.html",form=emp_form)

@app.route('/modificar', methods=["GET","POST"])
def modificar():
    emp_form=forms.EmpleadosForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        emp1=db.session.query(Empleados).filter(Empleados.id==id).first()
        emp_form.id.data=request.args.get('id')
        emp_form.nombre.data=emp1.nombre
        emp_form.correo.data=emp1.correo
        emp_form.telefono.data=emp1.telefono
        emp_form.direccion.data=emp1.direccion
        emp_form.sueldo.data=emp1.sueldo
    if request.method=='POST':
        id=emp_form.id.data
        emp1=db.session.query(Empleados).filter(Empleados.id==id).first()
        emp1.nombre=emp_form.nombre.data
        emp1.nombre=emp_form.nombre.data
        emp1.correo=emp_form.correo.data
        emp1.telefono=emp_form.telefono.data
        emp1.telefono=emp_form.telefono.data
        emp1.direccion=emp_form.direccion.data
        emp1.sueldo=emp_form.sueldo.data
        db.session.add(emp1)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template("modificar.html", form=emp_form)

@app.route('/eliminar', methods=["GET","POST"])
def eliminar():
    emp_form=forms.EmpleadosForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        emp1=db.session.query(Empleados).filter(Empleados.id==id).first()
        emp_form.id.data=request.args.get('id')
        emp_form.nombre.data=emp1.nombre
        emp_form.correo.data=emp1.correo
        emp_form.telefono.data=emp1.telefono
        emp_form.direccion.data=emp1.direccion
        emp_form.sueldo.data=emp1.sueldo
        
    if request.method=='POST':
        id=emp_form.id.data
        alum=Empleados.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template("eliminar.html", form=emp_form)
        

@app.route("/ABC_Completo",methods=["GET","POST"])
def ABC_Completo():
    
    empleado=Empleados.query.all()
    return render_template("ABC_Completo.html", empleados=empleado)

@app.route("/pizzeria",methods=["GET","POST"])
def pizzeria():
    pizzeria_form=forms.PizzeriaForm(request.form)
    pedidosPiza = PedidosPizza.query.all()
    if request.method == 'POST' and pizzeria_form.validate():
        costoPizza = int(pizzeria_form.tamaPizza.data)
        ingrePizza = int(pizzeria_form.ingredientesPizza.data)
        totalPizza = int(pizzeria_form.numPizzas.data)
        subtotalPizza = str( (costoPizza+ingrePizza)*totalPizza )
        totalPizza = "0"
        pedidosPiza = PedidosPizza(
                    nombre=pizzeria_form.nombre.data,
                    direccion =pizzeria_form.direccion.data,
                    telefono = pizzeria_form.telefono.data,
                    tamaPizza = pizzeria_form.tamaPizza.data,
                    ingredientesPizza = pizzeria_form.ingredientesPizza.data,
                    numPizza = pizzeria_form.numPizzas.data,
                    subtotal = subtotalPizza,
                    total = totalPizza)
        db.session.add(pedidosPiza)
        db.session.commit()

    return render_template("pizzeria.html",pedidos=pedidosPiza,form=pizzeria_form)

# @app.route("/alumnos",methods=["GET","POST"])
# def alum():
#     nom=""
#     apa=""
#     ama=""
#     mensaje = ""
#     alum_form=forms.UsersForm(request.form)
#     if request.method=='POST' and alum_form.validate():
#         nom=alum_form.nombre.data
#         apa=alum_form.apaterno.data
#         ama=alum_form.amaterno.data

#         mensaje = 'Bienvenido {}'.format(nom)
#         flash(mensaje)

#         print("NOMBRE: {}".format(nom))
#         print("APATERNO: {}".format(apa))
#         print("AMATERNO: {}".format(ama))

#     return render_template("alumnos.html", form=alum_form, nom=nom, apa=apa, ama=ama)

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()