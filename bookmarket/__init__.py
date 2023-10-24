from flask import Flask
from flask_bcrypt import Bcrypt
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("FIREBASE_URL")})
bcrypt = Bcrypt(app)

from bookmarket import routes