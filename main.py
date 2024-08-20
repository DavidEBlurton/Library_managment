import re
from system import Book, User, Author

books = []
users = []
authors = []

def display_menu():
    print('''\nWelcome to the Library Management System!
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit''')

def book_operations():
    print('''\nBook Operations:
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books''')

def user_operations():
    print('''\nUser Operations:
    1. Add a new user
    2. View user details
    3. Display all users''')

def author_operations():
    print('''\nAuthor Operations:
    1. Add a new author
    2. View author details
    3. Display all authors''')

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre: ")
    pub_date = input("Enter the publication date: ")
    books.append(Book(title, author, genre, pub_date))
    print("Book added successfully.")

def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    for book in books:
        if book.title == title and book.available:
            book.available = False
            user_id = input("Enter your user ID: ")
            for user in users:
                if user.user_id == user_id:
                    user.borrowed_books.append(title)
                    print("Book borrowed successfully.")
                    return
            print("User ID not found.")
            return
    print("Book not available or not found.")

def return_book():
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book.title == title and not book.available:
            book.available = True
            user_id = input("Enter your user ID: ")
            for user in users:
                if user.user_id == user_id:
                    if title in user.borrowed_books:
                        user.borrowed_books.remove(title)
                        print("Book returned successfully.")
                        return
                    else:
                        print("This book was not borrowed by you.")
                        return
            print("User ID not found.")
            return
    print("Book not found or was not borrowed.")

def search_book():
    title = input("Enter the title of the book to search: ")
    for book in books:
        if book.title == title:
            print(book)
            return
    print("Book not found.")

def display_all_books():
    if not books:
        print("No books in the library.")
    for book in books:
        print(book)

def add_user():
    name = input("Enter the user's name: ")
    user_id = input("Enter the user ID: ")
    users.append(User(name, user_id))
    print("User added successfully.")

def view_user():
    user_id = input("Enter the user ID to view details: ")
    for user in users:
        if user.user_id == user_id:
            print(user)
            return
    print("User not found.")

def display_all_users():
    if not users:
        print("No users in the system.")
    for user in users:
        print(user)

def add_author():
    name = input("Enter the author's name: ")
    biography = input("Enter the author's biography: ")
    authors.append(Author(name, biography))
    print("Author added successfully.")

def view_author():
    name = input("Enter the author's name to view details: ")
    for author in authors:
        if author.name == name:
            print(author)
            return
    print("Author not found.")

def display_all_authors():
    if not authors:
        print("No authors in the system.")
    for author in authors:
        print(author)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations()
            book_choice = input("Enter your choice: ")
            if book_choice == '1':
                add_book()
            elif book_choice == '2':
                borrow_book()
            elif book_choice == '3':
                return_book()
            elif book_choice == '4':
                search_book()
            elif book_choice == '5':
                display_all_books()
            else:
                print("Invalid choice.")

        elif choice == '2':
            user_operations()
            user_choice = input("Enter your choice: ")
            if user_choice == '1':
                add_user()
            elif user_choice == '2':
                view_user()
            elif user_choice == '3':
                display_all_users()
            else:
                print("Invalid choice.")

        elif choice == '3':
            author_operations()
            author_choice = input("Enter your choice: ")
            if author_choice == '1':
                add_author()
            elif author_choice == '2':
                view_author()
            elif author_choice == '3':
                display_all_authors()
            else:
                print("Invalid choice.")

        elif choice == '4':
            print("Quitting the application.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
