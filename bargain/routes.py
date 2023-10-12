from flask import Flask, render_template, url_for, flash, redirect, request
from bargain.forms import SearchForm
from bargain import app

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

    if request.method == "POST":
        keyword = request.form['keyword']
        return redirect('/search/{}'.format(keyword))
    
@app.route("/search/<string:keyword>", methods=["GET"])
def search(keyword):
    search_list = bw_scrape(keyword, 20)

    search_list += wd_scrape(keyword, 20)

    