from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_status():
    return "Hola Estoy Funcionando"

@app.route('/login')
def get_user_and_password():
    
    auth_header   = request.authorization
    user = auth_header.username 
    password = auth_header.password
    
    
    
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
    #token = request.args.get('token')
    token = request.headers['authorization']
    user  = request.headers['user']
    
    #print(auth_header)
    #user = request.args.get('user')
    params = {'id': id}
    headers = {'authorization': token,  'user': user}
    url = 'http://127.0.0.1:8002/planDeVenta'
    response = requests.get(url,  params=params,  headers= headers)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return jsonify({'error': 'Acceso Denegado'}), 403

if __name__ == '__main__':
    app.run(port=8000)