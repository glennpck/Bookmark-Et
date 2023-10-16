from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '9d87de6a296e5fafce4eb599607a9dd4'

from bookmarket import routes