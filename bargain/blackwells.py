import httpx
from selectolax.parser import HTMLParser
from bargain.classes import Blackwells

bw_url = 'https://blackwells.co.uk'

def search(keyword, hits):
    keyword_header = keyword.replace(' ', '+')
    headers = '/bookshop/search/?keyword={}&maxhits={}&offset={}'.format(keyword_header, hits, hits)

    r = httpx.get(bw_url + headers)

    return HTMLParser(r.text)

def search_isbn(isbn):
    headers = '/bookshop/product/{}'.format(isbn)

    r = httpx.get(bw_url + headers)

    return HTMLParser(r.text)

def get_details(item):
    
    isbn = item.css_first("a.btn").attributes['data-isbn']
    item_page = search_isbn(isbn)

    item_details = item_page.css("div.container--50")

    title_list = item_details[0].css_first("h1.product__name").text(strip=True, deep=False).split(" ")
    title = ""
    for word in title_list:
        if "\t" not in word:
            title += word

    desc = ""
    if item_details[1].css_first("font"):
        desc = item_details[1].css_first("font").text(strip=True deep=False)
    else:
        para_list = item_details[1].css("p")
        if len(para_list) >= 1 and len(para_list) <= 2:
            desc = para_list[0].text(strip=True, deep=False)
        elif len(para_list) > 2:
            desc = para_list[1].text(strip=True, deep=False)
        else:
            desc = "Description Unavailable"

    author = ""
    author_list = item_details[0].css_first("p.product__author")
    if len(author_list) <= 1:
        author = author_list.text(strip=True, deep=False)
    else:
        for node in author_list:
            author += node.text(strip=True, deep=False)
                
    

    type_pbd_nodes = page.css("p.product-format > span")
    type = type_pbd_nodes[0].text()
    pbd = type_pbd_nodes[1].text()

    book = Blackwells(
        isbn = item.css_first("a.btn").attributes['data-isbn'],
        title = title,
        desc = get_desc(item.css_first("a.btn").attributes['data-isbn']),
        author = item.css_first("p.product-author").text(),
        cover = bw_url + str(item.css_first("img").attributes['src']),
        type = type,
        pb_date = pbd,
        price = item.css_first("li.product-price--current").text().strip(),
        url = bw_url + str(item.css_first("a.product-name").attributes["href"])
    )

def bw_scrape(keyword, hits):

    if (len(keyword) == 13) and (keyword.isdigit()):
        page = search_isbn(keyword)
        details =  page.css("div.container--50")

        title_list = details[0].css_first("h1.product__name").text(strip=True, deep=False).split(" ")
        title = ""
        for word in title_list:
            if "\t" not in word:
                title += word
        

    else:
        page = search(keyword, hits)
        book_list = []
        
        for item in page.css("li.search-result__item"):

            book = get_details(item)

            book_list.append(book)

    return(book_list)