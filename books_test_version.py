
import requests as rq
from bs4 import BeautifulSoup

import pandas as pdd

url_wb = 'https://books.toscrape.com/'

request = rq.get(url=url_wb)

if request.ok:
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        rating = book.p['class'][1]
        print(f'Book title: {title}, book price: {price}, book rating: {rating}')
else:
    print('error in request')


# print(books)
