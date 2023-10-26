from firebase_admin import db
from bookmarket.classes import User, Book, Blackwells
from datetime import datetime

def createUserData(user):
    username = user.username
    email = user.email
    password = user.password
    favourites = user.favourites
    recent_viewed = user.recent_viewed
    return {email.replace(".", ","): {"username": username, "email": email.replace(".", ","), "password": password, "favourites": favourites, "recent_viewed": recent_viewed}}

def getUserObject(email):
    ref = db.reference('/{}'.format(email.replace(".", ",")))
    user_obj = ref.get()
    return User(
        user_obj['username'], 
        user_obj['email'], 
        user_obj['password'], 
        user_obj['favourites'], 
        user_obj['recent_viewed'])

def getBookObject(book):
    return {book.isbn: {"isbn": book.isbn,
                        "title": book.title,
                        "desc": book.desc,
                        "author": book.author,
                        "cover": book.cover,
                        "type": book.type,
                        "pb_date": book.pb_date,
                        "price": book.price,
                        "url": book.url}}

def parseFavAmbiguous(dict):
    fav_list = []
    if dict != ['']:
        for key in dict:
            if key != '0':
                fav_list.append(key)

    return fav_list

def updateRecentViewed(new, email, isbn):
    recent_list = db.reference('/{}/recent_viewed'.format(email.replace(".", ",")).get())
    if len(recent_list) == 5 and isbn not in recent_list.keys():
        latest_date = ""
        remove_isbn = ""
        for key in recent_list:
            if key != '0':
                view_date = datetime.strptime(recent_list["key"]["date"], "%Y-%m-%d %H:%M:%S.%f")
                if latest_date == "" or view_date > latest_date:
                    latest_date = view_date
                    remove_isbn = key
        db.reference('/{}/recent_viewed/{}'.format(email.replace(".", ","), remove_isbn).delete())

    db.reference('/{}/recent_viewed'.format(email.replace(".", ",")).update(new))