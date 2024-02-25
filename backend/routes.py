from flask import request, jsonify, make_response
import bcrypt
from database import *
import jwt
from email_sending import send_verification_email, send_password_reset_email
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
        
    @app.route('/login', methods=['POST', 'OPTIONS'])
    def login():
        if request.method == 'OPTIONS':
            response = make_response(jsonify({'status': 'OK'}), 200)
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            return _build_cors_preflight_response()
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            if not all([email, password]):
                return jsonify({'error': 'All fields must be filled'}), 400
            user = get_user_by_email(email)
            if user is None:
                return jsonify({'error': 'User with that email does not exist'}), 404
            if not user['verified']:
                return jsonify({'error': 'User is not verified'}), 403
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):
                token = generate_jwt_token(email)
                return jsonify({'token': token}), 200
            return jsonify({'error': 'Invalid password'}), 401
        except Exception as e:
            logger.exception(f"Exception in login: {e}")
            return jsonify({'error': 'Failed to login'}), 500
        


    # This endpoint sends a password reset link or code to the user's email
    @app.route('/request_password_reset', methods=['POST'])
    def request_password_reset():
        try:
            data = request.get_json()
            email = data.get('email')
            # Log the incoming email
            app.logger.debug(f"Received password reset request for email: {email}")
            # Check if the email exists in the database 
            user_exists = check_user_email(email)
            if user_exists:
                # Generate the password reset token
                token = generate_jwt_token(email)
                app.logger.debug(f"Generated password reset token: {token}")
                # Send the password reset email
                email_sent = send_password_reset_email(email, token, mail, app)
                # Log the email sending result
                if email_sent:
                    return jsonify({'message': 'Password reset email sent successfully'}), 200
                else:
                    app.logger.error("Failed to send password reset email")
                    return jsonify({'error': 'Failed to send password reset email'}), 500 
            else:
                return jsonify({'error': 'User with that email does not exist'}), 404
        except Exception as e:
            app.logger.exception(f"Exception in /request_password_reset: {e}") 
            return jsonify({'error': 'Failed to process password reset request'}), 500
          


    # This endpoint confirms the password reset using the token and updates the password
    @app.route('/confirm_password_reset', methods=['POST'])
    def confirm_password_reset():

        data = request.get_json()
        token = data.get('token')
        new_password = data.get('newPassword')
        email = data.get('email')
            
        user_id = check_password_reset_token(email, token)
        if user_id:
            update_user_password(email, new_password)
            return jsonify({'message': 'Password reset successfully'}), 200
        else:
            return jsonify({'error': 'Invalid or expired reset token'}), 400 
        


    

    def _build_cors_preflight_response():
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response