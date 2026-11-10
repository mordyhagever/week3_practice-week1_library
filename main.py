from validations import choose_checker
from book_manager import *

def active1():
    print(display_books())
def active2(book_name):
    print(search_book(book_name))
def active3(name, author, book):
    print(add_book(name, author, book))
def active4(book_id):
    print(borrow_book(book_id))
def active5(book_id):
    print(return_book(book_id))
def active6():
    print(display_books())
def active7(author):
    print(get_book_by_author(author))




def print_menu():
    print("""
    ================================
         LIBRARY MANAGEMENT
    ================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:

    """)
    choose = input()
    while not choose_checker(choose):
        choose = input("Enter a valid number from the menu")
    choose = int(choose)
    return choose

def activator():
    choice = print_menu()
    print(choice)
    while choice != 8:
        if choice == 1:
            active1()
        if choice == 2:
            book_name = input("Enter book name")
            active2(book_name)
        if choice == 3:
            b_name = input("Enter book name: ")
            b_author = input("Enter book author: ")
            b_year = input("Enter book year: ")
            active3(b_name, b_author, b_year)
        if choice == 4:
            b_id = input("Enter book id: ")
            active4(b_id)
        if choice == 5:
            b_id = input("Enter book id: ")
            active5(b_id)
        if choice == 6:
            active6()
        if choice == 7:
            author = input("Enter author name: ")
            active7(author)
        choice = print_menu()
    print("progress has finished successfully")

activator()