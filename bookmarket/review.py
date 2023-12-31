import httpx
from selectolax.parser import HTMLParser
from bookmarket.classes import Review, GeneralReview

urlbw = 'https://uk.trustpilot.com/review/bookshop.blackwell.co.uk'

urlwd = 'https://www.reviews.io/company-reviews/store/wordery'

def bwReviews():
    resp = httpx.get(urlbw)
    parse = HTMLParser(resp.text)

    icon = str(parse.css_first("img.business-profile-image_image__jCBDc").attributes['src'])

    value = parse.css_first("p.typography_body-l__KUYFJ").text(strip=True, deep=False)
    
    count = ""
    count_scrape = [int(s) for s in str(parse.css("span.typography_body-l__KUYFJ")[1].text(deep=False, strip=True)) if s.isdigit()]
    for digit in count_scrape:
        count += str(digit)

    reviewList = bwCompileTopReviews(parse)

    return GeneralReview(
        "Blackwells.co.uk",
        "Trustpilot",
        "https://uk.trustpilot.com/review/bookshop.blackwell.co.uk",
        icon,
        value,
        count,
        reviewList,
        'https://blackwells.co.uk/bookshop/delivery'
    )

def bwCompileTopReviews(parse):
    reviewList = []
    cardCounter = 0

    for card in parse.css("div.styles_cardWrapper__LcCPA"):
        if cardCounter < 3:
            username = card.css_first("span.typography_heading-xxs__QKBS8").text()

            for img in card.css("img"):
                if 'Rated' in str(img.attributes['alt']):
                    value = int(str(img.attributes['alt'])[6])

            content = card.css_first("p.typography_body-l__KUYFJ").text()

            date = card.css_first("p.typography_body-m__xgxZ_").text(deep=False, strip=True)

            reviewList.append(Review(
                username,
                value,
                content,
                date
            ))
            
            cardCounter += 1

        else:
            break

    return reviewList

def wdReviews():
    resp = httpx.get(urlwd)
    parse = HTMLParser(resp.text)

    icon = str(parse.css_first("img.LogoComponent__image ").attributes['src'])

    strong = parse.css("strong")
    value = strong[0].text(strip=True)
    count = str(strong[1].text(strip=True)).replace(',', '')

    reviewList = wdCompileTopReviews(parse)

    return GeneralReview(
        "Wordery.com Ltd",
        "Reviews.io",
        "https://www.reviews.io/company-reviews/store/wordery",
        icon,
        value,
        count,
        reviewList,
        'https://wordery.com/cs/help#faq-delivery'
    )

def wdCompileTopReviews(parse):
    reviewList = []
    cardCounter = 0

    for card in parse.css("div.Review"):
        if cardCounter < 3:
            username = card.css_first("a.Review__author").text(strip=True)

            stars = card.css("i.stars__icon")
            value = len(stars)

            content = str(card.css_first("span.Review__body").text(strip=True))[1:-1]

            date = card.css_first("div.Review__dateSource").text(strip=True)[7:]

            reviewList.append(Review(
                username,
                value,
                content,
                date
            ))
            
            cardCounter += 1
        
        else:
            break

    return reviewList