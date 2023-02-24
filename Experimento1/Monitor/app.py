from flask import Flask, jsonify, render_template
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    
    servicios = {
        'Almacenamiento': 'http://localhost:8000',
        'Cola de Mensajes': 'http://localhost:8001',
        'API Gateway': 'http://localhost:8002'
    }
    
    resultados = {}

    def check_service(url):
        try:
            response = requests.get(url)
            return 'Activo'
        except:
            return 'Inactivo'

    while True:

        for servicio, url in servicios.items():
            resultados[servicio] = check_service(url)

        return render_template('index.html', servicios=servicios, resultados=resultados)

