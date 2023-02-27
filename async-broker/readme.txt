Ejecucion de Test:

Preparación en Ambiente PC: Windows10.

1. instale server-redis en windows 10 localmente:
   para windows 10 debe ir a esta ruta :
   https://github.com/microsoftarchive/redis/releases , descargue la version 3.0.504 Latest: Redis-x64-3.0.504.msi
    - importante: agregue al path la ruta de instalación

2. instale celery: en lo posible realice una instalación sin ambiente venv: pip install celery
   Nota:
   celery 4.0+ no es soportado por windows todavia , si tiene problemas instale la version 3.1.24
   pip uninstall celery
   pip install celery==3.1.24
   

Ejecucion en Windows de los Test Asincrono:

1. Abra un cmd: ejecute el server redis
   redis-server --port 6380 --slaveof 127.0.0.1 6379

2. Ejecutar microservicio python PlanVentaProcessor.py para iniciar el API que recibe la solicitud de cliente Postman:

    \PlanVentaQuery\python PlanVentaQuery.py  ---En windows no olvidar ubicarse en la ruta.

2. ejecute en otro CMD el worker Celery:
    para version 4.0+: 
      -instale eventlet: pip install eventlet
      -ejecute el worker desde la ruta \PlanVentaQuery\:
           celery -A tareas worker -l  info -P eventlet 
       
    para version 3.1.24: 
       -ejecute el worker desde la ruta \PlanVentaQuery\:
           celery -A tareas worker -l  info  
   
Nota :
Ejemplo:
path completo celery:

-C:\Temp\Andes\arquitecturaAgil2\CCP-grupo10\async-broker\planVentaQuery>C:\Users\MARIO\AppData\Roaming\Python\Python39\Scripts\celery -A tareas worker -l  info -P eventlet
path  completo redis

-C:\Users\MARIO>redis-server --port 6380 --slaveof 127.0.0.1 6379


3. Relice las solicitudes Postman:

Para los Test de:

1. Comunicacion Asyncrona--ver documento evidencias:

https://uniandes-my.sharepoint.com/:w:/g/personal/mr_gomezc1_uniandes_edu_co/EST6Pz4znOVMul81pu9MXpEBMJL_do6W07vzkUs-Bjjv7A?e=o0uhEy

2. Deteccion falla componente Monitor--ver documento evidencias:

https://uniandes-my.sharepoint.com/:w:/g/personal/mr_gomezc1_uniandes_edu_co/EWAD9kpGbb5EnphSHVA4EpoBz9J4Lpm3gG1Da-60gd2YoA?e=wKa3wf











#Microservicio1---> Microservicio2
#use Celery redis

implementing:

1. install Celery
2. install redis
3. install psycopg2--or sqlite3
4. correr worker
  #iniciar worker: celery -A tareas worker -l  info -Q logs
5. iniciar server redis: redis-server
   redis-server --port 6380 --slaveof 127.0.0.1 6379
# config Postgresql

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://user_dbname:pass@localhost:5432/tabla'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
