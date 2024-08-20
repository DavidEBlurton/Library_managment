# models.py

class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = True

    # Getters and Setters
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def pub_date(self):
        return self.__pub_date

    @pub_date.setter
    def pub_date(self, value):
        self.__pub_date = value

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Published: {self.__pub_date}, Available: {self.__available}"


class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id
        self.__borrowed_books = []

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    @borrowed_books.setter
    def borrowed_books(self, value):
        self.__borrowed_books = value

    def __str__(self):
        return f"Name: {self.__name}, User ID: {self.__user_id}, Borrowed Books: {', '.join(self.__borrowed_books)}"


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def biography(self):
        return self.__biography

    @biography.setter
    def biography(self, value):
        self.__biography = value

    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
