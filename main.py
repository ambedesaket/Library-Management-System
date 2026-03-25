# Library Management System

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open('books.txt', 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        title, author, isbn, available = parts
                        book = Book(title, author, isbn)
                        book.available = available == 'True'
                        self.books.append(book)
        except FileNotFoundError:
            pass

    def save_books(self):
        with open('books.txt', 'w') as f:
            for book in self.books:
                f.write(
                    f"{book.title},{book.author},{book.isbn},{book.available}\n")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                self.save_books()
                return True
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                self.save_books()
                return True
        return False

    def track_availability(self):
        available_books = [book for book in self.books if book.available]
        return available_books


def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("Book added.")
        elif choice == '2':
            isbn = input("ISBN to issue: ")
            if library.issue_book(isbn):
                print("Book issued.")
            else:
                print("Book not available.")
        elif choice == '3':
            isbn = input("ISBN to return: ")
            if library.return_book(isbn):
                print("Book returned.")
            else:
                print("Book not found or already available.")
        elif choice == '4':
            available = library.track_availability()
            for book in available:
                print(f"{book.title} by {book.author}")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
