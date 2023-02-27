#iniciar worker: celery -A tareas worker -l  info -Q logs
from celery import Celery
from datetime import datetime

# instancia Worker-celery PlanProcessorQuery
celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

# recibe funcion de la cola redis + parametros
@celery_app.task(name='get_plan_venta')
def get_plan_venta(cliente):
    name_file = 'planVenta_'+cliente+'.txt'
    print('log-celery : PlanVentaQuery1')
    # write file system planVenta Cliente
    with open(name_file, 'w') as flog:
        flog.write(f'{cliente},producto=cafe,Cantida=30,Stock=10,{datetime.now()}')
