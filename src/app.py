
from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'http://localhost:8000/phpMyAdmin/index.php?db=nutriesthetic.&table=clientes&target=sql.php'
app.config['SQALCHEMY_TRACK_MODIFACTIONS']= False

app.secret_key = 'Santos0823'

db = SQLAlchemy(app)
ma = Marshmallow(app)

#crear las tablas de la base de datos

class nutriesthetic(db.Model):
    __tablename__ = "cliente"
    nombre completo =  ID_Nombre_completo(VARCHAR, primary_key=True)
    numero de identificacion= numero_identificacion(VARCHAR(50))
    numero de telfono = numero_telefono(VARCHAR(50))

    def __init__(self,Nombre_completo,numero_identificacion,numero_telefono):
       self.ID_Nombre_completo = Nombre_completo
       self.numero_identificacion = numero_identificacion
       self.numero_telefono = numero_telefono
db.create_all()

class ArticulosSchema(ma.Schema):
    class Meta:
        fields = ('ID_Nombre_completo','numero_identificacion','numero_telefono')

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
            ID_Nombre_completo = request.form['ID_Nombre_completo']
            numero_identificacion = request.form['numero_identificacion']
            numero_telefono = request.fron['numero_telefono']
            newarticulo = Articulos(Nombre_completo,numero_identificacion,numero_telefono )
            #agregamos la data en la tabla
            db.session.add(newarticulo)
            db.session.commit()
            return "guardado con exito"


        
@app.route('/')
def index():
    return "Hola mundo!!"

if __name__ == "__main__":
    app.run(debug = True)