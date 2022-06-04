import json
from flask import Flask, request

app = Flask('abc123')

@app.route('/wall', methods=['GET'])
def handle_request():
    data = request.args.get('code')

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
