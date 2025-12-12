class Book:
    def __init__(self, isbn, title, year):
        self.isbn = isbn
        self.title = title
        self.year = year

    def __str__(self):
        return f"Book(isbn={self.isbn},title={self.title},year={self.year})"


# class Library:
#     def __init__(self):
#         self.books = []
# 
#     def print_books(self):
#         for b in self.books:
#             print(f"- {b.isbn}: {b.title} ({b.year})")
# 
#     def add(self, book):
#         self.books.append(book)
# 
#     def remove(self, isbn):
#         for b in self.books:
#             if b.isbn == isbn:
#                 self.books.remove(b)


class Library:
    def __init__(self):
        self.books = {}

    def find(self, isbn):
        return self.books.get(isbn)

    def add(self, book):
        self.books[book.isbn] = book

    def size(self):
        return len(self.books)

    def remove(self, isbn):
        b = self.books.get(isbn)
        if b:
            del self.books[isbn]
        return b
        
    def contains(self, isbn):
        return isbn in self.books

    def print_books(self):
        for b in self.books.values():
            print(f"- {b.isbn}: {b.title} ({b.year})")


def print_menu():
    print("BLIBLIOTECA")
    print("1. Mostrar llibres")
    print("2. Afegir llibre")
    print("3. Eliminar llibre")
    print("0. Eixir")


def read_option(max=3):
    n = int(input())
    while n < 0 or n > max:
        print("ERROR: Opció invàlida")
        n = int(input())
    return n


def read_book():
    isbn = input("ISBN:")
    title = input("Títol:")
    year = int(input("Any:"))
    return Book(isbn, title, year)


def read_isbn():
    return input("ISBN:")


if __name__ == '__main__':
    l = Library()

    running = True
    while running:
        print_menu()
        n = read_option()
        match n:
            case 1:
                if l.size() == 0:
                    print("No hi ha cap llibre.")
                else:
                    l.print_books()
            case 2:
                book = read_book()
                l.add(book)
            case 3:
                isbn = read_isbn()
                if l.contains(isbn):
                    book = l.remove(isbn)
                    print(f"S'ha eliminat el llibre {book}")
                else:
                    print(f"No hi ha cap llibre amb ISBN: {isbn}")
            case 0:
                running = False
