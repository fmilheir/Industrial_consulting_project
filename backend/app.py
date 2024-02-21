from flask import Flask, request, jsonify, make_response 
import bcrypt
from database import *
from flask_cors import CORS
from flask_mail import Mail
import os 
from dotenv import load_dotenv
from email_sending import *
from routes import configure_routes


load_dotenv()


app = Flask(__name__)
mail = Mail(app)


## POOL IS IN THE DATABASE FILE
# Mail configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['JWT_SECRET'] = os.environ.get('JWT_SECRET')   


  # This will configure the mail instance with the app

# Allow CORS for requests from 'http://localhost:8080'
CORS(app)

configure_routes(app, mail)
@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello, World!'})

@app.route('/database', methods=['GET']) ## checking if database is connecting
def get_database():
    return test_db_connection()


@app.route('/email_sending', methods=['POST'])
def send_verification_email():
    return jsonify({'message': 'Verification email sent successfully'}), 200


# Calling the function of the create table to ensure that database is created on startup 
with app.app_context():
    create_table_user_if_not_exists()


if __name__ == '__main__':
     # Initialize the database connection pool
    DBPool.get_instance()
    print('Starting the application')
    app.run(host='0.0.0.0', port=5000, debug=True)
