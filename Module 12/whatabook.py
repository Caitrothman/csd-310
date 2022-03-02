import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("--MAIN MENU --")

    print (" 1. View Books\n 2. View Store Locations\n 3. My Account")

    try:
        option = int(input(" Please enter menu option\n "))

        return option 

    except ValueError:
        print("\n Invalid number\n")
        mysql.exit 

def view_books(_cursor):
    _cursor.execute ("SELECT book_id, boo_name, author, details FROM book")

    books = cursor.fetchall()

    print('\n --DISPLAYING BOOKS --')
    for book in books:
        print("Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2]))
    cursor.execute(mysql)

def view_location (_cursor):
    _cursor.execute ('SELECT store_id, local FROM store;')

    locations = _cursor.fetchall()

    print ('\n--DISPLAYING LOCATIONS--')
    for location in locations:
        print("Locale: {}\n".format(location[1]))
    cursor.execute(mysql)

def validate_user ():

    user_id = int(input('Enter your user ID'))

    return user_id 

def view_account_menu():
    print('\n --User Menu--')
    print(' 1. Wishlist\n   2. Add Book\n       3. Main Menu')

    user_option = int(input('Enter menu option number\n '))

    return user_option 

def view_wishlist (_cursor, _user_id):

    _cursor.execute ('SELECT user.user_id, user.fist_name, user.last_name, book.book_id, book.book_name, book.author'
        'FROM wishlist' +
        'INNER JOIN user ON wishlist.user_id = user.user_id' +
        'INNER JOIN book ON wishlist.book_id = user.book_id' +
        'WHERE user.user_id = {}'.format(_user_id))

    wishlist = cursor.fetchall()

    print('\n --DISPLAYING WISHLIST BOOKS--')
    for book in wishlist:
        print(' Book Name: {}\n     Author: {}\n'.format(book[4], book[5]))

def view_books_to_add (_cursor, _user_id):
    not_in_wishlist = ("SELECT book_id, book_name, author, details"
        "FROM book "
        "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(not_in_wishlist)
    print(not_in_wishlist)

    add_books = _cursor.fetchall()

    print('\n--AVAILABLE BOOKS--')
    for book in add_books:
        print(' Book ID: {}\n   Book Name: {}\n'.format(book[0], book[1]))

def add_books_to_wishlist (_cursor, user_id, book_id):
    _cursor.execute ('INSERT INTO wishlist (user_id, book_id) VALUES ({}, {})'.format(user_id, book_id))

try:

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print ('WhatABook Application!')

    user_selection = show_menu()


    while user_selection != 4:

        if user_selection == 1:
            view_books(cursor)

        if user_selection == 2:
            view_location(cursor)

        if user_selection ==3:
            the_user_id = validate_user()
            account_option = view_account_menu()

            while account_option != 3:

                if account_option == 1:
                    view_wishlist(cursor, the_user_id)

                if account_option == 2:
                    view_books_to_add(cursor, the_user_id)
                    book_id = int(input("\n Enter the ID of the book you want to add: "))
                    add_books_to_wishlist(cursor, the_user_id, book_id)

                    db.commit()

                    print("\n   Book ID: {} was added to your wishlist!".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("\n Invalid option, try again...")

                account_option = view_account_menu()

            if user_selection < 0 or user_selection >4:
                print("\n Invalid option, try again...")

            user_selection = show_menu()

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" This database does not exist")

    else: 
        print(err)

finally:
    db.close()

