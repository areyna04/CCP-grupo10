#iniciar worker: celery -A tareas worker -l  info -Q logs
from celery import Celery

# instancia celery
celery_app = Celery(__name__, broker='redis://localhost:6379/0')

# recibe funcion de la cola + parametros
@celery_app.task(name='plan_venta')
def get_plan_venta(cliente):
    with open('planVenta.txt', 'w') as flog:
        flog.write(f'{cliente},producto=cafe,Cantida=30,Stock=10')
