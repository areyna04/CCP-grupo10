from flask import Flask
from flask_restful import Api, Resource
from celery import Celery

# Definicion Ambiente Microservicio
app = Flask(__name__)

api = Api(app)
# Recurso HTTP: /planventa/cliente
class PlanVenta(Resource):
    def get(self):
        pass
 
#Urls Servicio
api.add_resource(PlanVenta, '/planes/')

#Microservicio 2 PlanVentaProcessor  port = 5003
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)   