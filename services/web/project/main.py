import requests
from flask import (
    Flask,
    request,
    jsonify
)

app = Flask(__name__)

jc_api_url = 'https://console.jumpcloud.com/api/systemusers'
headers = {"x-api-key":"1a007f3b4d75127958f2bcce0c619382850177cf", "Accept": "application/json", "Content-Type":"application/json"}

@app.route('/list_user/<id>', methods=['GET'])
def list_user(id):
    uid = request.view_args['id']
    res = requests.get(jc_api_url+f'/{uid}', headers=headers).content.decode('utf-8')
    return jsonify(data=res, status=200)

@app.route('/list_users', methods=['GET'])
def list_users():
    res = requests.get(jc_api_url, headers=headers).content.decode('utf-8')
    return jsonify(data=res, status=200)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)