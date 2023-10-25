from flask import Flask, render_template, url_for, flash, redirect, request, session
from bookmarket import bcrypt
from bookmarket.blackwells import bw_scrape
from bookmarket.wordery import wd_scrape
from bookmarket.classes import User
from firebase_admin import db
from bookmarket import app

def createUserData(user):
    username = user.username
    email = user.email
    password = user.password
    favourites = user.favourites
    recent_viewed = user.recent_viewed
    return {email.replace(".", ","): {"username": username, "email": email.replace(".", ","), "password": password, "favourites": favourites, "recent_viewed": recent_viewed}}

@app.route("/")
def welcome():
    return redirect('/index')
    
@app.route("/index", methods=['GET', 'POST'])
def index():

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
        if username != "":
            return render_template("index.html", username=username)
        else:
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
                session['email'] = user_object['email']
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