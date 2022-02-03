from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/command', methods=['POST', 'GET'])
def command():
    if request.method == 'POST':
        data = request.get_json()
        print(data['action'])
        if data['action']=='up':
            print("blah")
        return jsonify(data)
