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