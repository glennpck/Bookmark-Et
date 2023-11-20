import httpx
from selectolax.parser import HTMLParser
from bookmarket.classes import Wordery
# from forex_python.converter import CurrencyRates
# from decimal import Decimal

# c = CurrencyRates(force_decimal=True)
wd_url = 'https://wordery.com'

def search(isbn):
    headers = "/{}".format(isbn)

    r = httpx.get(wd_url + headers)

    return HTMLParser(r.text)

def get_details(page, isbn):
    item_details = page.css_first("div.o-layout--huge")
    title = item_details.css_first("strong").text()
    cover = wd_url + str(item_details.css_first("img").attributes['src'])[:-9] + 'height=500'

    price = "Unavailable on this platform"
    try:
        check = item_details.css_first("strong.u-fs--ex").attributes
        price = item_details.css_first("strong.u-fs--ex").text()
        # Code block for forex-python package (Currently unusable)
        #====================================================================================================
        # try:
        #     price = c.convert('USD', 'SGD', Decimal(price.replace("$", "")))
        # except Exception:
        #     pass

    except Exception:
        pass

    return Wordery(
        isbn,
        title,
        cover,
        price,
        wd_url + "/{}".format(isbn)
    )

def wd_scrape(isbn):
    page = search(isbn)

    book = get_details(page, isbn)

    return book