from flask import Flask, jsonify, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    #Microservicios a Monitorear:
    servicios = {
                 'PlanVentaProcessor1': 'http://localhost:8000',
                 'PlanVentaProcessor2': 'http://localhost:8001',
                 'PlanVentaProcessor3': 'http://localhost:8002'
                }
    
    resultados = {}
    date = datetime.now()
    
    #Revisar si Microservicio está activo o inactivo
    def check_service(url):
        try:
            response = requests.get(url)
            return 'Activo'
        except:
            return 'Inactivo'
        
    while True:
        # Recorre Estado de cada uno de microservicio
        for servicio, url in servicios.items():
            resultados[servicio] = check_service(url)
        # imprime Log de estado microservicios    
        with open("healthcheck.txt", "a") as flog:
            for serv in servicios:
                line_log = serv+","+resultados[serv]+","+str(date)+"\n"
                flog.write(line_log)

        return render_template('index.html', servicios=servicios, resultados=resultados, date=date)
    

if __name__ == '__main__':
    app.run(debug=True)