from flask import Flask, render_template, url_for, flash, redirect, request
from bookmarket.blackwells import bw_scrape
from bookmarket.wordery import wd_scrape

from bookmarket import app

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        keyword = request.form['keyword']
        return redirect('/search/{}'.format(keyword))
    
    try:
        return render_template("index.html")
    except Exception:
        pass
    
@app.route("/search/<string:keyword>", methods=["GET"])
def search(keyword):
    
    search = bw_scrape(keyword, 30)

    if (len(search) == 1):
        return render_template("item.html", product=search[0])
    
    else:
        return render_template("list.html", product=search)

    