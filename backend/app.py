from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)
print('hello workd')