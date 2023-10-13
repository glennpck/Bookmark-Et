class Book:
    def __init__(self, isbn, title, desc, author, cover, type, pb_date, price, url):
        self.isbn = isbn
        self.title = title
        self.desc = desc
        self.author = author
        self.cover = cover
        self.dimensions = [266, 400]
        self.type = type
        self.pb_date = pb_date
        self.price = price
        self.url = url

class Blackwells(Book):
    def __init__(self, isbn, title, desc, author, cover, type, pb_date, price, url):
        super().__init__(isbn, title, desc, author, cover, type, pb_date, price, url)
        self.platform = "Blackwells"

class Wordery(Book):
    def __init__(self, isbn, title, author, cover, type, price, url):
        super().__init__(isbn, title, author, cover, type, price, url)
        self.platform = "Wordery"