from flask import Flask, render_template, url_for, flash, redirect, request
from bookmarket.blackwells import bw_scrape
from bookmarket.wordery import wd_scrape

from bookmarket import app
    
@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        try:
            keyword = request.form['keyword']
            return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
        except Exception:
            pass

        try:
            isbn = request.form['isbn']
            return redirect('/item/{}'.format(isbn))
        except Exception:
            pass
    
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
            return redirect('/item/{}'.format(isbn))
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

    if request.method == "POST":
        try:
            keyword = request.form['keyword']
            return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
        except Exception:
            pass

        try:
            isbn = request.form['isbn']
            return redirect('/item/{}'.format(isbn))
        except Exception:
            pass

    try:
        bw_search = bw_scrape(isbn)
        wd_search = wd_scrape(isbn)
        return render_template("compare.html", bw=bw_search[0], wd=wd_search)
    
    except Exception:
        return render_template("error.html")
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    try:
        return render_template("signup.html")
    except Exception:
        return render_template("error.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        return render_template("login.html")
    except Exception:
        return render_template("error.html")