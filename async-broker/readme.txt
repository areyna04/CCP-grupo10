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
