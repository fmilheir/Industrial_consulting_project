from flask import Flask, jsonify 
from database import test_db_connection
app = Flask(__name__)






## POOL IS IN THE DATABASE FILE


@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello, World!'})

@app.route('/database', methods=['GET']) ## checking if database is connecting
def get_database():
    return test_db_connection()



if __name__ == '__main__':
    print('hello workd this is a print statement ')

    app.run(host= '0.0.0.0', port=5000, debug=True)

