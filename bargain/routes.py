from flask import render_template, url_for, flash, redirect
from bargain import app

@app.route("/home")
def index():
    return render_template('test.html')