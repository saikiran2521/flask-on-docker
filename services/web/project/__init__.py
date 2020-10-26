import requests
from flask import (
    Flask,
    request,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

jc_api_url = 'https://console.jumpcloud.com/api/systemusers'
headers = {"x-api-key":"1a007f3b4d75127958f2bcce0c619382850177cf", "Accept": "application/json", "Content-Type":"application/json"}


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

@app.route('/list_user/<id>', methods=['GET'])
def list_user(id):
    uid = request.view_args['id']
    res = requests.get(jc_api_url+f'/{uid}', headers=headers).content.decode('utf-8')
    return jsonify(data=res, status=200)

@app.route('/list_users', methods=['GET'])
def list_users():
    res = requests.get(jc_api_url, headers=headers).content.decode('utf-8')
    return jsonify(data=res, status=200)

@app.route('/create_user', methods=['POST'])
def create_user():
    inbound_user = {}
    inbound_user['username'] = request.form['username']
    inbound_user['email'] = request.form['email']
    inbound_user['firstname'] = request.form['firstname']
    inbound_user['lastname'] = request.form['lastname']
    print(inbound_user)
    res = requests.post(jc_api_url, headers=headers, data=inbound_user)
    return jsonify(status=200)