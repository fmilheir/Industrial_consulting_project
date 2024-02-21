from flask import request, jsonify, make_response
import bcrypt
from database import *
import jwt
from email_sending import send_verification_email
import traceback

def configure_routes(app, mail):

    @app.route('/signup', methods=['POST', 'OPTIONS'])
    def signup():
        if request.method == 'OPTIONS':
            response = make_response(jsonify({'status': 'OK'}), 200)
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            return _build_cors_preflight_response()
        try:
            data = request.get_json()
            print("Received data:", data)
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')
            phone_number = data.get('phoneNumber')
            password = data.get('password')

            if not all([first_name, last_name, email, phone_number, password]):
                return jsonify({'error': 'All fields must be filled'}), 400

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            verification_token = generate_jwt_token(email)
             
            print("Verification token generated:", verification_token)
            if verification_token is None:
                print("Failed to generate verification token")
                return jsonify({'error': 'Failed to generate verification token'}), 500

            store_user_result = store_user_in_database(first_name, last_name, email, phone_number, hashed_password, verification_token)
            if isinstance(store_user_result, tuple):
                # Unpacking for clarity
                error_message, status_code = store_user_result
                print(f"Error storing user: {error_message}")
                return jsonify({'error': error_message}), status_code

            email_sent = send_verification_email(email, verification_token, mail, app)
            if email_sent: 
                return jsonify({'success': f'User created successfully. Please check your inbox or spam folder for a verification email'}), 201
            return jsonify({'message': 'User created successfully, verification email sent', 'token': verification_token}), 201
        except Exception as e:
            error_traceback = traceback.format_exc()
            logger.exception(f"Exception in signup: {e}\n{error_traceback}")
            return jsonify({
                'error': 'Failed to signup',
                'message': str(e),
                'traceback': error_traceback
            }), 500
        




    @app.route('/verify', methods=['POST'])
    def verify_user():
        data = request.get_json()
        email = data.get('email')
        token = data.get('token')
        return _verify_user_logic(email, token, mail, app)

    def _verify_user_logic(email, token, mail, app):
        data = request.get_json()
        email = data.get('email')
        token = data.get('token')
        try:
            jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            message = verify_user_account(email, token)
            return jsonify({'message': message}), 200
        except jwt.ExpiredSignatureError:
            # If the token has expired, genereate a new one and send it 
            new_token = generate_jwt_token(email)
            send_verification_email(email, new_token, mail, app)
            return jsonify({'error': 'Token expired, new token sent'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

    def _build_cors_preflight_response():
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response