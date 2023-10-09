from flask import render_template, url_for, flash, redirect
from bargain import app

@app.route("/")
def index():
    return render_template('index.html')