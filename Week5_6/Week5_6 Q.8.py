import csv
import os

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_list(self):
        return [self.book_id, self.title, self.author, str(self.available)]

class Library:
    def __init__(self, filename="books.csv"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.filename):
            return  # No file yet
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                self.books = []
                for row in reader:
                    if row:
                        book = Book(row[0], row[1], row[2], row[3] == 'True')
                        self.books.append(book)
        except Exception as e:
            print("Error reading book file:", e)

    def save_books(self):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for book in self.books:
                    writer.writerow(book.to_list())
        except Exception as e:
            print("Error saving book file:", e)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print("Book added successfully.")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    self.save_books()
                    print(f"Book '{book.title}' issued successfully.")
                    return
                else:
                    print(f"Book '{book.title}' is already issued.")
                    return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    self.save_books()
                    print(f"Book '{book.title}' returned successfully.")
                    return
                else:
                    print(f"Book '{book.title}' is already available.")
                    return
        print("Book not found.")

    def search_book(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                found = True
                status = "Available" if book.available else "Issued"
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")
        if not found:
            print("No matching books found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                book_id = input("Enter Book ID: ")
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                book = Book(book_id, title, author)
                library.add_book(book)
            except Exception as e:
                print("Error adding book:", e)

        elif choice == '2':
            title = input("Enter the title of the book to issue: ")
            library.issue_book(title)

        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '4':
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == '5':
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
