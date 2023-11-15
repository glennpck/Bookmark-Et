from firebase_admin import db
from bookmarket.classes import User, Book, BookAmbiguous
from datetime import datetime
import re
import httpx
from selectolax.parser import HTMLParser

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
    recent_list = db.reference('/{}/recent_viewed'.format(email.replace(".", ","))).get()
    if len(recent_list) == 5 and isbn not in recent_list.keys():
        latest_date = ""
        remove_isbn = ""
        for key in recent_list:
            if key != '0':
                view_date = datetime.strptime(recent_list[key]["date"], "%Y-%m-%d %H:%M:%S.%f")
                if latest_date == "" or view_date < latest_date:
                    latest_date = view_date
                    remove_isbn = key
        db.reference('/{}/recent_viewed/{}'.format(email.replace(".", ","), remove_isbn)).delete()

    db.reference('/{}/recent_viewed'.format(email.replace(".", ","))).update(new)

def parseRecentViewed(recent_list):
    parsed_recent = []
    for key in recent_list:
        if key != '0':
            ambig_book = BookAmbiguous(
                key,
                recent_list[key]['title'],
                recent_list[key]['cover'],
                recent_list[key]['price']
            )
            parsed_recent.append(ambig_book)

    return parsed_recent

def retrieveFavList(email):
    fav_list = []
    obj_list = db.reference('/{}/favourites'.format(email.replace(".", ","))).get()
    for key in obj_list:
        if key != '0':
            fav_list.append(Book(
                key, 
                obj_list[key]['title'],
                obj_list[key]['desc'],
                obj_list[key]['author'],
                obj_list[key]['cover'],
                obj_list[key]['type'],
                obj_list[key]['pb_date'],
                obj_list[key]['price'],
                obj_list[key]['url']))
            
    return fav_list

def tracking(favList):
    updateFavList = []
    exp = "\d+\.\d+"
    for book in favList:
        url = "https://blackwells.co.uk/bookshop/product/{}".format(book.isbn)
        r = httpx.get(url)
        new_price_str = getNewPrice(HTMLParser(r.text))
        new_price = float(re.findall(exp, new_price_str)[0])
        origin_price = float(re.findall(exp, book.price)[0])
        if new_price != origin_price:
            book.new_price = new_price_str
        updateFavList.append(book)
    return updateFavList

def getNewPrice(page):
    return page.css_first("li.product-price--current").text(strip=True, deep=False)
        