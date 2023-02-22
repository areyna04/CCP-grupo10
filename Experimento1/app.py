from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

# Funciones para comprobar el estado de los microservicios
def check_service(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

# Llenar con ips de los microservicios
def check_all_services():
    services = {
        'servicio1': 'http://localhost:8000',
        'servicio2': 'http://localhost:8001',
        'servicio3': 'http://localhost:8002'
    }

    results = {}
    for service_name, service_url in services.items():
        results[service_name] = check_service(service_url)

    return results

# Configuración del intervalo de tiempo para comprobar el estado de los microservicios
@app.before_first_request
def activate_job():
    def check_services():
        app.config['services'] = check_all_services()
    check_services()
    while True:
        time.sleep(60)
        check_services()

# Vista para mostrar el estado de los microservicios
@app.route('/services')
def services():
    return render_template('services.html', services=app.config['services'])

if __name__ == '__main__':
    app.run(debug=True)