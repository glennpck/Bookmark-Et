import httpx
from selectolax.parser import HTMLParser
from bargain.classes import Blackwells

def search(keyword):
    bw_url = 'https://blackwells.co.uk'
    keyword_header = keyword.replace(' ', '+')
    headers = '/bookshop/search/?keyword={}'.format(keyword_header)

    r = httpx.get(bw_url + headers)

    return HTMLParser(r.text)

def bw_scrape():
    pass