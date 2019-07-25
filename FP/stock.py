import json
from copy import copy
from operator import itemgetter, attrgetter
from functools import reduce, partial



class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw = True)

# sort_by_publish_year = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# print(sort_by_publish_year[0]['publish_date'], sort_by_publish_year[-2]['publish_date'])
# num_page = sorted(BOOKS, key=attrgetter('number_of_pages'))
# print(num_page[0].number_of_pages, num_page[-3].number_of_pages)


def sales_price(book):
    '''Apply a 20% discount to the books's price'''
    book = copy(book)
    book.price = round(book.price - book.price * .2, 2)
    return book

# saled_book = list(map(sales_price, BOOKS))
# print(BOOKS[0].price)
# print(saled_book[0].price)

def is_long_book(book):
    '''Does a book have 600+ pages?'''
    return book.number_of_pages >= 600

# long_books = list(filter(is_long_book, BOOKS))
# long_books2 = [each for each in BOOKS if is_long_book(each)]

# def is_long_book(book):
#     return any(['Roland' in subject for subject in book.subjets])

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

def is_good_deal(book):
    return book.price <= 5

cheap_books = sorted(filter(is_good_deal, map(sales_price, BOOKS)), key=attrgetter('price'))

# print(cheap_books[3].price)



# LAMBDA

total = reduce(lambda x, y: x + y, [each.price for each in BOOKS])
# print(total)
long_books = list(filter(lambda x: x.number_of_pages >=600, BOOKS))
# print(len(long_books))
good_deal = list(filter(lambda x: x.price <= 6, BOOKS))
# print(len(good_deal))


# PARTIALS

def markdown(book, discount):
    book = copy(book)
    book.price = round(book.price - book.price * discount, 2)
    return book

half = partial(markdown, discount=.5)
long_be_half = map(half, filter(is_long_book, BOOKS))

print(half(BOOKS[0]).price)

print(list(long_be_half))