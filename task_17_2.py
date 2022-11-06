class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name} {self.country} {self.birthday} {self.books}"


class Book:
    count_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.count_books += 1

    def get_all_books(self):
        return self.count_books

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name} {self.year} {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        self.books.append(Book(name, year, author))
        if author not in self.authors:
            self.authors.append(author)

    def group_by_author(self, author: Author):
        return author.books

    def group_by_year(self, year: int):
        return [book for book in self.books if year == book.year]

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name} {self.books} {self.authors}"


library = Library('Kyiv Library 1')
stephen_king = Author('Stephen King', 'USA', '21.09.1947',
                      ['The Shining', 'It', 'The Green Mile', 'Dreamcatcher'])
george_orwell = Author('George Orwell', 'United Kingdom', '25.05.1903',
                       ['Nineteen Eighty-Four', 'Animal Farm', 'Burmese Days'])
ayn_rand = Author('Ayn Rand', 'USA', '02.02.1905',
                  ['Atlas Shrugged', 'The Fountainhead', 'We the Living'])
library.new_book(name=stephen_king.books[1], year=1970, author=stephen_king)
library.new_book(name=george_orwell.books[1], year=1968, author=george_orwell)
library.new_book(name=ayn_rand.books[2], year=1968, author=ayn_rand)
print(library.books)
print(library.group_by_author(stephen_king))
print(library.group_by_year(1968))
print(Book.count_books)
