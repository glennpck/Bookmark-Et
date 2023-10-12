import httpx
from selectolax.parser import HTMLParser
from bargain.classes import Wordery

def search(keyword):
    wd_url = 'https://wordery.com'
    keyword_header = keyword.replace(' ', '+')
    headers = '/search/?term={}'.format(keyword_header)

    r = httpx.get(wd_url + headers)

    return HTMLParser(r.text)

def wd_scrape():
    pass