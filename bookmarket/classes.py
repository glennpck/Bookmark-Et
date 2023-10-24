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

