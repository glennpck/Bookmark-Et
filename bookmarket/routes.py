from flask import Flask, render_template, url_for, flash, redirect, request
from bookmarket.blackwells import bw_scrape
from bookmarket.wordery import wd_scrape

from bookmarket import app

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        keyword = request.form['keyword']
        return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
    
    try:
        return render_template("index.html")
    except Exception:
        return render_template("error.html")
    
@app.route("/search/keyword=<string:keyword>", methods=['GET', 'POST'])
def search(keyword):

    if request.method == "POST":

        try:
            keyword = request.form['keyword']
            return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
        except Exception:
            pass

        try:
            isbn = request.form['isbn']
            return redirect('/search/keyword={}'.format(isbn))
        except Exception:
            pass
    
    if (len(keyword) == 13) and (keyword.isdigit()):
        return redirect('/item/{}'.format(keyword))

    search = bw_scrape(keyword)
    
    try:
        if (len(search) >= 1):
            return render_template("list.html", search=search)
        
        else:
            return render_template("empty.html")
        
    except Exception:
        return render_template("error.html")
    
@app.route("/item/<string:isbn>", methods=['GET', 'POST'])
def book(isbn):

    if request.method == "POST":
        try:
            keyword = request.form['keyword']
            return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
        except Exception:
            pass

        try:
            isbn = request.form['isbn']
            return redirect('/compare/{}'.format(isbn))
        except Exception:
            pass

    try:
        search = bw_scrape(isbn)
        return render_template("item.html", book=search[0])
    
    except Exception:
        return render_template("error.html")
    
@app.route("/compare/<string:isbn>", methods=['GET', 'POST'])
def compare(isbn):
    pass