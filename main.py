
"""

я уверен - никто не будет смотреть в этот коммит
но если вы это читаете, напишите в Issues репозитория:

"код не работает - технические шоколадки"

и я куплю вам шоколадку
просто так

"""

import requests
from bs4 import BeautifulSoup
import json

url = 'https://books.toscrape.com/'

request = requests.get(url=url)

ratings = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

if request.ok:
    soup = BeautifulSoup(request.text, 'lxml')
    soup_books = soup.find_all('article', class_='product_pod')

    index_counter = 0
    books = {}
    for soup_book in soup_books:
        books[index_counter] = {
            'title': soup_book.h3.a['title'],
            'price': float(soup_book.find('p', class_='price_color').text.replace('Â£', '')),
            'rating': ratings[str(soup_book.p['class'][1])]
        }
        index_counter += 1
    with open('books_file.json', 'w') as file:
        json.dump(books, file, indent=4)

else:
    print('something went wrong')
