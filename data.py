import httpx
from selectolax.parser import HTMLParser
import pandas as pd
import time

columns = ["Content", "Score"]
reviews = pd.DataFrame(columns=columns)
page_counter = 1
cardCounter = 0

while cardCounter < 10000:
    time.sleep(30)

    url = "https://www.trustpilot.com/review/bookshop.blackwell.co.uk?page={}".format(page_counter)

    r = httpx.get(url)

    parse = HTMLParser(r.text)
    
    for card in parse.css("div.styles_cardWrapper__LcCPA"):
        try:
            content = card.css_first("p.typography_body-l__KUYFJ").text(strip=True)
        except Exception:
            content = card.css_first("h2.typography_heading-s__f7029").text(strip=True)

        value = 0

        for img in card.css("img"):
                if 'Rated' in str(img.attributes['alt']):
                    value = int(str(img.attributes['alt'])[6])

        row = [content, value]
        review_row = pd.DataFrame([row], columns=columns)
        reviews = pd.concat([reviews, review_row])

        print(reviews)
        
        cardCounter += 1


    print(page_counter)
    page_counter += 1

with pd.ExcelWriter("bw_reviews.xlsx", engine="xlsxwriter") as writer:
    reviews.to_excel(writer, sheet_name="reviews")