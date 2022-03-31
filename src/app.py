
from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/cur'
app.config['SQALCHEMY_TRACK_MODIFACTIONS']= False

app.secret_key = 'cur2022'

db = SQLAlchemy(app)
ma = Marshmallow(app)

#crear las tablas de la base de datos

class Articulos(db.Model):
    __tablename__ = "Articulos"
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(70))
    Precio = db.Column(db.Float())

    def __init__(self, Nombre, Precio):
       self.Nombre = Nombre
       self.Precio = Precio
db.create_all()

class ArticulosSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre','Precio')

articulo_schema = ArticulosSchema()
articulos_schema =ArticulosSchema(many=True)

@app.route('/articulos',methods=['GET','POST'])
def articulos():
    all_articulos = Articulos.query.all()
    resultadoArticulos = articulos_schema.dump(all_articulos)
    print (resultadoArticulos)
    return "estos son los datos "

@app.route('/addarticulos',methods=['POST'])
def addarticulos():
    if request.method == 'POST':
        #aquí obtengo los datos del formulario
        id = request.form['Id']
        articuloexit = Articulos.query.get(id)
        if articuloexit :
            return "no se puede almacernar los datos, el articulo ya existe"
        else:
            Nombre = request.form['Nombre']
            Precio = request.form['Precio']
            newarticulo = Articulos(Nombre, Precio)
            #agregamos la data en la tabla
            db.session.add(newarticulo)
            db.session.commit()
            return "guardado con exito"


        
@app.route('/')
def index():
    return "Hola mundo!!"

if __name__ == "__main__":
    app.run(debug = True)