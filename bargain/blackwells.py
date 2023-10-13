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
    bw_url = 'https://blackwells.co.uk'
    page = search(keyword, hits)
    book_list = []
    
    for item in page.css("li.search-result__item"):

        title_nodes = item.css("a.product-name")
        title = ''
        for node in title_nodes:
            try:
                validateValue = node.attributes['itemprop']
                title = node.text()
            except KeyError:
                pass

        type_pbd_nodes = page.css("p.product-format > span")
        type = type_pbd_nodes[0].text()
        pbd = type_pbd_nodes[1].text()

        book = Blackwells(
            isbn = item.css_first("a.btn").attributes['data-isbn'],
            title = title,
            desc = "",
            author = item.css_first("p.product-author").text(),
            cover = bw_url + str(item.css_first("img").attributes['src']),
            type = type,
            pb_date = pbd,
            price = item.css_first("li.product-price--current").text().strip(),
            url = bw_url + str(item.css_first("a.product-name").attributes["href"])
        )

        book_list.append(book)

    return(book_list)