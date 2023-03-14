
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import requests
import sqlite3

token = "yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3ODgzMDYxNywianRpIjoiZDFjZmQwN2MtYzk0Yy00MDNhLWFlMTktMzg3OTYyZjk2NDNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6WzFdLCJuYmYiOjE2Nzg4MzA2MTcsImV4cCI6MTY3ODgzMTUxN30.Krqa79EjXgpuMZeJu3nLFriL3R_pxO4F6nTpKRPYi54"
user = "user1"
conn = sqlite3.connect('userDB.db', check_same_thread=False)
c = conn.cursor()
c.execute("UPDATE users SET token = ? WHERE id = ?", (token, 1))
c.execute("SELECT authorization FROM users WHERE id=?", (1,))
autho = c.fetchone()
print(autho[0])

if autho[0] == token:
    print("go")