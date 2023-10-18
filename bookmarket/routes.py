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
        pass
    
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
    
    # elif request.method == "GET":
    #     isbn = request.form['isbn']
    #     return redirect('/search/keyword={}'.format(isbn))
    
    search = bw_scrape(keyword, 10)

    if (len(search) == 1):
        return render_template("item.html", book=search[0])
    
    else:
        return render_template("list.html", search=search)

    