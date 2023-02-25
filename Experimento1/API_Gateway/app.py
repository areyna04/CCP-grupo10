from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido'

if __name__ == '__main__':
    app.run(port=8001)