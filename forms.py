from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField
from wtforms import validators


class UsersForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese nombre valido')
    ])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese apellido valido')
    ])
    amaterno=StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese apellido valido')
    ])

    edad=IntegerField('edad',[        
        validators.number_range(min=1, max=20,message='ingrese edad valida')
    ])
    correo=StringField('correo',[
        validators.DataRequired(message='el campo es requerido'),
    ])

    # nombre=StringField('nombre')
    # apaterno=StringField('apaterno')
    # amaterno=StringField('amaterno')
    # edad=IntegerField('edad')
    # correo=EmailField('correo')

class EmpleadosForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese nombre valido')
    ])
    correo=StringField('correo',[
        validators.DataRequired(message='ingresar un correo valido'),
    ])
    telefono=StringField('telefono')
    direccion=StringField('direccion')
    sueldo=StringField('sueldo')
    

class PizzeriaForm(Form):
    id = IntegerField('id')
    nombre= StringField('nombre',[
        validators.DataRequired(message='el campo es requerido')
    ])
    direccion= StringField('direccion',[
        validators.DataRequired(message='el campo es requerido')
    ])
    telefono= StringField('telefono',[
        validators.DataRequired(message='el campo es requerido')
    ])
    numPizzas= IntegerField('Número Pizzas',[
        validators.DataRequired(message='el campo es requerido')
    ])
    
    tamaPizza = RadioField('Tamaño Pizza', 
       choices=[
            ('40','Chica $40'),
            ('80','Mediana $80'),
            ('120','Grande $120')
            ], 
        validators=[validators.InputRequired()])
    ingredientesPizza = RadioField('Ingredientes Pizza', 
       choices=[
            ('10','Jamon $10'),
            ('10','Piña $10'),
            ('10','Champiñones $120')
            ], 
        validators=[validators.InputRequired()])
    subtotal= StringField('Subtotal')
    total= StringField('Total')
