
from requests import get
from bs4 import BeautifulSoup
import json

from ask_for_category import selected

if selected == 'books_1':
    url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
else:
    url = f'https://books.toscrape.com/catalogue/category/books/{selected}/index.html'
    
# url = 'https://books.toscrape.com/' is old url without categories

ratings = { # looks strange but i need that for parsing
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

user_request = {
    # 'title': input('Book title to find: '),
    'price': (float(input('Min book price, £: ')), float(input('Max book price, £: '))),
    'rating': int(input('Min book rating, 0-5: '))
}

index_counter = 0
books_to_dump = {}
def filter_book(book):
    global index_counter
    with open('smartparser/books_file.json', 'w') as file:
        if book['rating'] >= user_request['rating']:
            if user_request['price'][0] <= book['price'] <= user_request['price'][1]:
                books_to_dump[index_counter] = book
                index_counter += 1
        # print(books_to_dump)
        json.dump(books_to_dump, file, indent=4)


request = get(url=url)
if request.ok:
    soup = BeautifulSoup(request.text, 'lxml')
    soup_books = soup.find_all('article', class_='product_pod')
    for soup_book in soup_books:
        book = {
            'title': soup_book.h3.a['title'],
            'price': float(soup_book.find('p', class_='price_color').text.replace('Â£', '')),
            'rating': ratings[str(soup_book.p['class'][1])]
        }
        filter_book(book=book)
else:
    print(request)
