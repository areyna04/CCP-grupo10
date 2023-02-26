from flask import Flask
from flask_restful import Api, Resource
from celery import Celery

# Definicion Ambiente Microservicio
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/productos.db'
api = Api(app)

#se instancia para cuando colocar tareas en cola para workers
celery_app = Celery(__name__, broker='redis://localhost:6379/0')

# función para enviar a cola redis como parametro
@celery_app.task(name='plan_venta')
def get_plan_venta(*args):
    pass

# Recurso HTTP: /planventa/cliente
class PlanVenta(Resource):
    def post(self):
        cliente = request.json["cliente"]
        if cliente:
            args = (cliente,)
            #--Tarea Celery colocada en cola redis
            get_plan_venta.apply_async(args)
            return {'Tarea: iniciada'}, 200
        else:
            return {'no existe user'}, 404

#Urls Servicio
api.add_resource(PlanVenta, '/planes/<string:cliente>')

#Microservicio 2 PlanVentaProcessor  port = 8000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)   