class Book:
    def __init__(self, isbn, title, author, cover, type, price, url):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.cover = cover
        self.type = type
        self.price = price
        self.url = url

class Blackwells(Book):
    def __init__(self, isbn, title, author, cover, type, price, url):
        super().__init__(isbn, title, author, cover, type, price, url)
        self.platform = "Blackwells"

class Wordery(Book):
    def __init__(self, isbn, title, author, cover, type, price, url):
        super().__init__(isbn, title, author, cover, type, price, url)
        self.platform = "Wordery"