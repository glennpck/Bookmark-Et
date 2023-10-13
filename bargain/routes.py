from flask import Flask, render_template, url_for, flash, redirect, request
from blackwells import bw_scrape
from wordery import wd_scrape

from bargain import app

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

    if request.method == "POST":
        keyword = request.form['keyword']
        return redirect('/search/{}'.format(keyword))
    
@app.route("/search/<string:keyword>", methods=["GET"])
def search(keyword):
    
    search = bw_scrape(keyword, 30)

    if (len(search) == 1):
        return render_template("detail.html", product=search[0])
    
    else:
        return render_template("results.html", product=search)

    