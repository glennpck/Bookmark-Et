import httpx
from selectolax.parser import HTMLParser
from bookmarket.classes import Blackwells

bw_url = 'https://blackwells.co.uk'

def search(keyword, hits):
    keyword_header = keyword.replace(' ', '+')
    headers = '/bookshop/search/?keyword={}&maxhits={}'.format(keyword_header, hits, hits)

    r = httpx.get(bw_url + headers)

    return HTMLParser(r.text)

def search_isbn(isbn):
    headers = '/bookshop/product/{}'.format(isbn)

    r = httpx.get(bw_url + headers)

    return HTMLParser(r.text)

def get_details(item=None, isbn=""):
    
    if isbn == "":
        try:
            isbn = item.css_first("a.btn").attributes['data-isbn']

        except AttributeError:
            return None

    item_page = search_isbn(isbn)

    item_details = item_page.css("div.container--50")

    title_list = item_details[0].css_first("h1.product__name").text(strip=True, deep=False).split(" ")
    title = ""
    for word in title_list:
        if "\t" in word:
            snip = word.replace("\t", "")
            title += snip + " "
        else:
            title += word + " "

    desc = ""
    desc_nodes = item_details[1].css("div")
    for node in desc_nodes:
        try:
            attr = node.attributes['itemprop']
            desc = node.text(strip=True, deep=True)
        except KeyError:
            pass

    author = ""
    author_list = item_details[0].css("p.product__author > a")
    for node in author_list:
        author += node.text(strip=True, deep=False)
                
    product_format = item_details[0].css("p.product__format > span")
    type = product_format[0].text(strip=True, deep=False)
    pb_date = product_format[1].text(strip=True, deep=False)[1:-1]

    return Blackwells(
        isbn = isbn,
        title = title,
        desc = desc,
        author = author,
        cover = bw_url + str(item_details[0].css_first("img").attributes['src']).replace("500x500", "300x300"),
        type = type,
        pb_date = pb_date,
        price = item_details[0].css_first("li.product-price--current").text(strip=True, deep=False),
        url = bw_url + "/bookshop/product/{}".format(isbn)
    )

def bw_scrape(keyword, hits):

    book_list = []
    
    if (len(keyword) == 13) and (keyword.isdigit()):
        book = get_details(isbn=keyword)
   
        book_list.append(book)
        

    else:
        page = search(keyword, hits)
        
        for item in page.css("li.search-result__item"):

            book = get_details(item)

            if book != None:

                book_list.append(book)

    return(book_list)