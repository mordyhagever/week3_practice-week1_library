from data_base import books
from validations import *
from json_dealer import *
def display_books():
    loads = get_json()
    return loads


def get_next_book_id():
    loads = get_json()
    last_book = loads[-1]
    return last_book["id"] + 1

def search_book(name):
    if not str_check(name):
        return "name or author are empty"
    loads = get_json()
    for book in loads:
        if book["name"] == name:
            return book
    return None

def add_book(name, author, year):
    if not str_check(name) or not str_check(author):
        return "name or author are empty"
    if not check_year_published(year):
        return "year has to be positive number"
    year = int(year)
    if not check_existence(name, author):
        return "book already exist"

    new_book = {}
    new_book["id"] = get_next_book_id()
    new_book["name"] = name
    new_book["author"] = author
    new_book["year"] = year
    new_book["available"] = True
    add_to_json(new_book)
    return "added successfully"


def borrow_book(book_id):
    if not check_if_id_exist(book_id):
        return "Book doesn't exist"
    if not check_if_borrowed(book_id):
        return "books is already borrowed"
    book_id = int(book_id)
    loads = get_json()
    for book in loads:
        if book["id"] == book_id:
            book["available"] = "False"
            update_json(loads)
            return "book has been borrowed"
    return "ERROR, couldn't find the book"

def return_book(book_id):
    if not check_if_id_exist(book_id):
        return "Book doesn't exist"
    if check_if_borrowed(book_id):
        return "book is already in library"
    book_id = int(book_id)
    loads = get_json()
    for book in loads:
        if book["id"] == book_id:
            book["available"] = "True"
            update_json(loads)
            return "book had been returned"
    return "ERROR, couldn't find the book"


def get_available_books():
    available = []
    loads = get_json()
    for book in loads:
        if book["available"] == "True":
            available.append(book)
    return available

def get_book_by_author(author):
    loads = get_json()
    for book in loads:
        if book["author"] == author:
            return book
    return "ERROR book has not found"




