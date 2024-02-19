from flask import Flask, request, jsonify, make_response  # Import make_response
import bcrypt
from database import store_user_in_database
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/signup": {"origins": "http://localhost:8080"}})

@app.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    try:
        data = request.get_json()
        print("Raw Data Received:", data)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        phone_number = data.get('phoneNumber')
        password = data.get('password')

        if not all([first_name, last_name, email, phone_number, password]):
            return jsonify({'error': 'All fields must be filled'}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        print("Before insert:", first_name, last_name, email, phone_number, hashed_password)

        store_user_in_database(first_name, last_name, email, phone_number, hashed_password)
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        print("Signup Error:", e)
        return jsonify({'error': f'Unable to create user: {e}'}), 500
