from flask import Flask, render_template, url_for, flash, redirect, request, session
from bookmarket import bcrypt
from bookmarket.blackwells import bw_scrape
from bookmarket.wordery import wd_scrape
from bookmarket.classes import User
from firebase_admin import db
from bookmarket import app
from datetime import datetime

from bookmarket.methods import createUserData, getUserObject, getBookObject, parseFavAmbiguous, updateRecentViewed, parseRecentViewed

@app.route("/")
def welcome():
    return redirect('/index')
    
@app.route("/index", methods=['GET', 'POST'])
def index():

    username = ""
    recent_list = ['']
    try:
        username = session['username']
        user = getUserObject(session['email'])
        recent_list = parseRecentViewed(user.recent_viewed) if user.recent_viewed != [''] else user.recent_viewed
    except Exception:
        pass

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
        if username != "":
            return render_template("index.html", username=username, recent_viewed=recent_list)
        else:
            return render_template("index.html", recent_viewed=recent_list)
        
    except Exception:
        if username != "":
            return render_template("error.html", username=username)
        else:
            return render_template("error.html")
    
@app.route("/search/keyword=<string:keyword>", methods=['GET', 'POST'])
def search(keyword):
     
    username = ""
    try:
        username = session['username']
        fav_list = parseFavAmbiguous(db.reference('/{}/favourites'.format(session['email'].replace(".", ","))).get())
    except Exception:
        pass

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
        if username != "":
            if (len(search) >= 1):
                return render_template("list.html", search=search, username=username, fav_list=fav_list)
            else:
                return render_template("empty.html", username=username)
            
        else:
            if (len(search) >= 1):
                return render_template("list.html", search=search)
            else:
                return render_template("empty.html")
        
    except Exception:

        if username != "":
            return render_template("error.html", username=username)
        else:
            return render_template("error.html")
    
@app.route("/item/<string:isbn>", methods=['GET', 'POST'])
def book(isbn):

    username = ""
    try:
        username = session['username']
        fav_list = parseFavAmbiguous(db.reference('/{}/favourites'.format(session['email'].replace(".", ","))).get())
    except Exception:
        pass

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

    search = bw_scrape(isbn)
    now = str(datetime.now())
    book_obj = {search[0].isbn: {"isbn": search[0].isbn, "title": search[0].title, "cover": search[0].cover, "price": search[0].price, "date": now}}
    updateRecentViewed(book_obj, session['email'], search[0].isbn)

    try:
        if username != "":
            return render_template("item.html", book=search[0], username=username, fav_list=fav_list)
        else:
            return render_template("item.html", book=search[0])
    
    except Exception:
        if username != "":
            return render_template("error.html", username=username)
        else:
            return render_template("error.html")
    
@app.route("/compare/<string:isbn>", methods=['GET', 'POST'])
def compare(isbn):

    username = ""
    try:
        username = session['username']
    except Exception:
        pass

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
        if username != "":
            return render_template("compare.html", bw=bw_search[0], wd=wd_search, username=username)
        else:
            return render_template("compare.html", bw=bw_search[0], wd=wd_search)
    
    except Exception:
        if username != "":
            return render_template("error.html", username=username)
        else:
            return render_template("error.html")
    
@app.route("/signup", methods=["GET", "POST"])
def signup():

    username = ''
    try:
        username = session['username']
    except Exception:
        pass

    if username != '':
        return redirect(url_for('index'))

    if request.method == "POST":
        try:
            keyword = request.form['keyword']
            return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
        except Exception:
            pass

        try:
            email = request.form['email']
            ref = db.reference('/{}'.format(email.replace(".", ",")))
            if not ref.get():
                username = request.form['username']
                password = request.form['pass']
                hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(username, email, hashed_pw)
                db.reference("/").update(createUserData(user))
                flash('Account Created Successfully! Welcome to Bookmarket', 'success')
                session['username'] = user.username
                session['email'] = user.email
                return redirect(url_for('index'))

            else:
                flash('Account with specified email already exists!', 'danger')
                return redirect(url_for('signup'))

        except Exception:
            return render_template("error.html")

    try:
        return render_template("signup.html")
    
    except Exception:
        return render_template("error.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    
    username = ''
    try:
        username = session['username']
    except Exception:
        pass

    if username != '':
        return redirect(url_for('index'))

    if request.method == "POST":
        try:
            keyword = request.form['keyword']
            return redirect('/search/keyword={}'.format(keyword.replace(" ", "+")))
        except Exception:
            pass

        try:
            email = request.form['email']
            password = request.form['pass']
            ref = db.reference('/{}'.format(email.replace(".", ",")))
            if ref.get() and bcrypt.check_password_hash(ref.get()['password'], password):
                user_object = ref.get()
                session['username'] = user_object['username']
                session['email'] = user_object['email'].replace(",",".")
                return redirect(url_for('index'))

            else:
                flash('Invalid Email or Password! Please try again', 'danger')
                return redirect(url_for('login'))
        
        except Exception:
            return render_template("error.html")

    try:
        return render_template("login.html")
    
    except Exception:
        return render_template("error.html")

@app.route("/signout")
def signout():
    session.pop('username', None)
    session.pop('email', None)
    try:
        return redirect(url_for('index'))
    except Exception:
        return render_template("error.html")
    
@app.route("/renderFavourite")
def render_favourite():
    isbn = request.args.get('book')
    book = bw_scrape(isbn)
    fav_dict = db.reference('/{}/favourites'.format(session['email'].replace(".",","))).get()
    if book[0].isbn not in fav_dict:
        db.reference('/{}/favourites'.format(session['email'].replace(".",","))).update(getBookObject(book[0]))
    elif book[0].isbn in fav_dict:
        db.reference('/{}/favourites/{}'.format(session['email'].replace(".",","), book[0].isbn)).delete()
    return isbn