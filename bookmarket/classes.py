class User:
    def __init__(self, username, email, password, favourites=[""], recent_viewed=[""]):
        self.username = username
        self.email = email
        self.password = password
        self.favourites = favourites
        self.recent_viewed = recent_viewed

class Book:
    def __init__(self, isbn, title, desc, author, cover, type, pb_date, price, url):
        self.isbn = isbn
        self.title = title
        self.desc = desc
        self.author = author
        self.cover = cover
        self.dimensions = [[199, 300], [322, 500]]
        self.type = type
        self.pb_date = pb_date
        self.price = price
        self.new_price = 0
        self.url = url

class Blackwells(Book):
    def __init__(self, isbn, title, desc, author, cover, type, pb_date, price, url):
        super().__init__(isbn, title, desc, author, cover, type, pb_date, price, url)
        self.platform = "Blackwells"

class Wordery():
    def __init__(self, isbn, title, cover, price, url):
        self.isbn = isbn
        self.title = title
        self.cover = cover
        self.price = price
        self.url = url
        self.platform = "Wordery"

class BookAmbiguous():
    def __init__(self, isbn, title, cover, price):
        self.isbn = isbn
        self.title = title
        self.cover = cover
        self.price = price

class GeneralReview():
    def __init__(self, platform, origin, url, icon, value, count, reviewList, delivery):
        self.platform = platform
        self.origin = origin
        self.url = url
        self.icon = icon
        self.value = value
        self.count = count
        self.reviewList= reviewList
        self.delivery = delivery

class Review():
    def __init__(self, username, value, content, date):
        self.username = username
        self.value = value
        self.content = content
        self.date = date