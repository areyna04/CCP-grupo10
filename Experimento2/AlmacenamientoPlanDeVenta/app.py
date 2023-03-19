from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import requests
import sqlite3

conn = sqlite3.connect('plans.db', check_same_thread=False)

app = Flask(__name__)
c = conn.cursor()

@app.route('/planDeVenta')
def planDeVenta():
    id = request.args.get('id')
    token = request.headers['authorization']
    user  = request.headers['user']
    params = {'token': token, 'user': user}
    url = 'http://127.0.0.1:8001/authorize'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        c.execute("SELECT plan FROM plans WHERE id=?", (id))
        plan = c.fetchone()
        return jsonify(plan=plan), 200
    else:
        return jsonify({'error': 'Acceso Denegado'}), 403


if __name__ == '__main__':
    app.run(port=8002)