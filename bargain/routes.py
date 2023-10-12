from flask import render_template, url_for, flash, redirect
from bargain.forms import SearchForm
from bargain import app

@app.route("/")
def index():
    form = SearchForm()
    return render_template('index.html', search=form)