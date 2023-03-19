from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_status():
    return "Hola Estoy Funcionando"

@app.route('/login')
def get_user_and_password():
    #user = request.args.get('user')
    #password = request.args.get('password')
    auth_header   = request.authorization
    user = auth_header.username 
    password = auth_header.password
    
    ##params = {'user': user, 'password': password}
    
    
    
    url = 'http://127.0.0.1:8001/login'
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(user,password))
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return jsonify({'error': 'Acceso Denegado'}), 403

@app.route('/planDeVenta')
def get_plan_de_venta():
    id = request.args.get('id')
    token = request.args.get('token')
    user = request.args.get('user')
    params = {'id': id, 'token': token, 'user': user}
    url = 'http://127.0.0.1:8002/planDeVenta'
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return jsonify({'error': 'Acceso Denegado'}), 403

if __name__ == '__main__':
    app.run(port=8000)