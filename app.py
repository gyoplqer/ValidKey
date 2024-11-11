# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Sample JSON data
data = {
    "key": "23233f3d83f"
}

@app.route('/key', methods=['GET'])
def get_fact():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
