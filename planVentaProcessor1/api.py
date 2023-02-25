from flask import Flask
from flask_restful import Api, Resource
from faker import Faker

# Definicion Ambiente Microservicio
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/productos.db'


api = Api(app)
data_fk = Faker()

# DB Data Inicial Plan venta Usuarios todos microservicios
plan_venta = []
for rows in range(1,6):
    plan_user = {
                  "id" : rows,
                  "usuario" : "Juan Valdez",
                  "producto" : data_fk.name(),
                  "cantidad": data_fk.random_number(digits=2),
                  "valor": data_fk.random_number(digits=4),
                  "stock": data_fk.random_number(digits=2 )
                }
    plan_venta.append(plan_user)

# recurso GET http:/planes  todos los Clientes
class PlanVentaListResource(Resource):
    def get(self):
        return plan_venta


# recurso GET http:/plan/int:<id_usuario> un Cliente
class PlanVentaResource(Resource):
    def get(self, id_usuario):
        #return plan_venta_schema.dump(plan)
        return plan_venta[id_usuario-1]
# HealthCheck:

class MonitorCheck(Resource):
    def get(self,):
        return "Bienvenido"


#Urls Servicio
api.add_resource(PlanVentaListResource, '/planes')
api.add_resource(PlanVentaResource, '/planes/<int:id_usuario>')
api.add_resource(MonitorCheck, '/')

#Microservicio 1 PlanVentaProcessor  port = 8000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

