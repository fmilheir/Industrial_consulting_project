from flask import Flask, jsonify 
from database import test_db_connection
from flask_cors import CORS

app = Flask(__name__)

## POOL IS IN THE DATABASE FILE

# Allow CORS for requests from 'http://localhost:8080'
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello, World!'})

@app.route('/database', methods=['GET']) ## checking if database is connecting
def get_database():
    return test_db_connection()


@app.route('/signup', methods=['POST'])
def signup():
    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    print('Hello world')
    app.run(host='0.0.0.0', port=5000, debug=True)
