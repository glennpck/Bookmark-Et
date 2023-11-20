# Bookmark-Et

Bookmark-Et | Knowledge About Knowledge

## Prerequisites

- Python 3.11.5 and above : [Install Here](https://www.python.org/downloads/)
- Docker Desktop : [Install Here](https://www.docker.com/products/docker-desktop/)

## Project Structure

```bash
.
├── run.py
├── bookmarket
├── readme.md
└── bookmarket
    ├── __init__.py
    ├── blackwells.py
    ├── classes.py
    ├── methods.py
    ├── review.py
    ├── routes.py
    ├── wordery.py
    ├── templates
    │   ├── base.html
    │   ├── compare.html
    │   ├── empty.html
    │   ├── error.html
    │   ├── favourite.html
    │   ├── index.html
    │   ├── info.html
    │   ├── item.html
    │   ├── list.html
    │   ├── login.html
    │   └── signup.html
    └── static
        ├── main.css
        ├── main.js
        ├── script.js
        └── logo.png

```

## Frameworks and Dependencies

- [flask](https://flask.palletsprojects.com/) - Python Html Web Framework
- [bootstrap](https://getbootstrap.com/) - Application Styling Method
- [selectolax](https://selectolax.readthedocs.io/) - Data Scraping
- [httpx](https://www.python-httpx.org/) - Html Parser
- [firebase](https://firebase.google.com/) - User Information and Item Database

## **Build with Docker**
```bash
docker build -t bookmarket .
docker run -p 5000:5000 bookmarket
```

## Overview

An information terminal that provides details regarding books. The terminal provides useful information regarding book prices, publishing dates, distributor reviews and ratings, etc.

## Base Platform

The base platform of the application uses [Blackwells Book Store](https://blackwells.co.uk/bookshop/home) as Blackwells is the current globally leading online bookshop that rarely has titles running out of stock and has a wide variety of books for sale.

## What it does

The terminal scrapes data from its base platform and displays the results in its webpage. If the consumer wishes to do so, they can go further and have the terminal display prices from a different distributor (Other than Blackwells) for a price comparison.

## Benefits

If users choose to register an account, they will be able to collate a list of their favourite titles and have it stored in the database. Upon logging in, users will receive price updates on their favourite titles on the homepage (if any). The favourites tab will display the original price and the updated price.

## Demo