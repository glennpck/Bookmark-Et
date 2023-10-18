import httpx
from selectolax.parser import HTMLParser
from bookmarket.classes import Wordery

def search(keyword):
    wd_url = 'https://wordery.com'
    keyword_header = keyword.replace(' ', '+')
    headers = '{}'.format(keyword_header)

    r = httpx.get(wd_url + headers)

    return HTMLParser(r.text)

def wd_scrape():
    pass