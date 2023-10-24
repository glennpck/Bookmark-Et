from flask import Flask
from flask_bcrypt import Bcrypt
import firebase_admin
from firebase_admin import credentials
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '9d87de6a296e5fafce4eb599607a9dd4'
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("FIREBASE_URL")})
bcrypt = Bcrypt(app)

from bookmarket import routes