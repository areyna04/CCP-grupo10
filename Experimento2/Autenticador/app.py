from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import requests
import sqlite3
import json

conn = sqlite3.connect('userDB.db', check_same_thread=False)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 's'

jwt = JWTManager(app)
c = conn.cursor()

@app.route('/login')
def login():
    user = request.args.get('user')
    password = request.args.get('password')
    c.execute("SELECT id FROM users WHERE user=? AND password=?", (user, password))
    user = c.fetchone()
    if user:
        access_token = create_access_token(identity=user)
        c.execute("UPDATE users SET token = ? WHERE id = ?", (access_token, user[0]))
        conn.commit()
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Acceso Denegado'}), 403 

@app.route('/authorize')
def authorize():
    token = request.args.get('token')
    user = request.args.get('user')
    c.execute("SELECT authorization FROM users WHERE token=?", (token,))
    autho = c.fetchone()
    if autho[0] == 10:
        
        return jsonify({'response': 'Acceso Autorizado'}), 200
    else:
        return jsonify({'error': 'Acceso Denegado'}), 403
    

if __name__ == '__main__':
    app.run(port=8001)