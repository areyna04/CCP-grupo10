from flask import Flask, request
from flask_restful import Api, Resource
from celery import Celery

# Definicion Ambiente Microservicio PlanVentaProcessor
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/productos.db'
api = Api(app)

#se instancia para cuando colocar tareas en cola para workers
celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

# función para enviar a cola redis como parametro
@celery_app.task(name='get_plan_venta')
def get_plan_venta(*args):
    pass

# Recurso HTTP: /planventa/cliente
class PlanVenta(Resource):
    def get(self, cliente):
        if cliente:
            #--Tarea Celery colocada en cola redis
            args=(cliente,)
            get_plan_venta.apply_async(args=args)
            return 'Tarea: iniciada', 200
        else:
            return 'no existe user', 404

class PlanesVenta(Resource):
    def get(self):
        get_plan_venta.apply_async()
        return 'Tarea: iniciada', 200

#Urls Servicio
api.add_resource(PlanVenta, '/plan/<string:cliente>')
api.add_resource(PlanesVenta, '/planes')

#Microservicio 2 PlanVentaProcessor  port = 8000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)   