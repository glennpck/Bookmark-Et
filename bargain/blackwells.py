import httpx
from selectolax.parser import HTMLParser
from bargain.classes import Blackwells

def search(keyword, hits):
    bw_url = 'https://blackwells.co.uk'
    keyword_header = keyword.replace(' ', '+')
    headers = '/bookshop/search/?keyword={}&maxhits={}&offset={}'.format(keyword_header, hits, hits)

    r = httpx.get(bw_url + headers)

    return HTMLParser(r.text)

def bw_scrape(keyword, hits):
    page = search(keyword, hits)
    
    for item in page.css("li.search-result__item"):

        title_nodes = item.css("a.product-name")
        title = ''
        for node in title_nodes:
            try:
                validateValue = node.attributes['itemprop']
                title = node.text()
            except KeyError:
                pass