from distutils.log import debug
import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/exemplo', methods=['POST'])
def exemplo():
    json = request.get_json()
    nome = json['first_name'].upper()
    time = json['time'].upper()
    role = json['role'].upper()
    print(json)
    return jsonify(nome=nome,time=time,role=role)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)