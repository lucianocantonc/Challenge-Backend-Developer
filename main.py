from google.cloud import vision
from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/text_detector', methods=['POST'])
def detect_text():

    data = request.get_json()

    response = {
        'message' : 'thank you',
    }
    
    return jsonify(response), 200
    
    

if __name__ == '__main__':
    if os.environ.get('GAE_ENV') != 'standard':
        app.run(host='127.0.0.1', port=8080, debug=True)