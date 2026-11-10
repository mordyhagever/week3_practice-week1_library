from data_base import books
def is_int(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False

def choose_checker(num):
    if not is_int(num):
        return False
    num = int(num)
    if num < 1 or num > 8:
        return False
    return True

def str_check(name):
    if len(name) < 1:
        return False
    return True

def check_year_published(year):
    if not is_int(year):
        return False
    year = int(year)
    if year < 0:
        return False
    return True

def check_existence(name, author):
    for book in books:
        if book["name"] == name and book["author"] == author:
            return False
    return True

def check_if_id_exist(book_id):
    if is_int(book_id):
        book_id = int(book_id)
    for book in books:
        if book["id"] == book_id:
            return True
    return False

def check_if_borrowed(book_id):
    if is_int(book_id):
        book_id = int(book_id)
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                return False
    return True

