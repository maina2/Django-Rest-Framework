import os
import json
import threading
import time

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Copies: {self.copies})"

class Library:
    """Represents a library system."""
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = {}
        self.load_data()

    def add_book(self, book):
        if book.isbn in self.books:
            self.books[book.isbn].copies += book.copies
        else:
            self.books[book.isbn] = book
        print(f"Added {book.copies} copy/copies of '{book.title}'.")

    def remove_book(self, isbn, quantity=1):
        if isbn in self.books:
            if self.books[isbn].copies > quantity:
                self.books[isbn].copies -= quantity
                print(f"Removed {quantity} copy/copies of '{self.books[isbn].title}'.")
            elif self.books[isbn].copies == quantity:
                del self.books[isbn]
                print(f"Removed all copies of the book with ISBN: {isbn}.")
            else:
                print(f"Cannot remove {quantity} copies. Only {self.books[isbn].copies} available.")
        else:
            print(f"No book found with ISBN: {isbn}.")

    def search_book(self, keyword):
        results = [book for book in self.books.values() if keyword.lower() in book.title.lower()]
        if results:
            print(f"Search results for '{keyword}':")
            for book in results:
                print(book)
        else:
            print(f"No books found for the keyword '{keyword}'.")

    def list_books(self):
        if self.books:
            print("Library Catalog:")
            for book in self.books.values():
                print(book)
        else:
            print("The library catalog is empty.")

    def save_data(self):
        data = {isbn: vars(book) for isbn, book in self.books.items()}
        with open(f"{self.library_name}_data.json", "w") as file:
            json.dump(data, file)
        print("Library data saved successfully.")

    def load_data(self):
        if os.path.exists(f"{self.library_name}_data.json"):
            with open(f"{self.library_name}_data.json", "r") as file:
                data = json.load(file)
                for isbn, book_data in data.items():
                    self.books[isbn] = Book(**book_data)
            print("Library data loaded successfully.")

class LibraryThread(threading.Thread):
    def __init__(self, library):
        super().__init__()
        self.library = library

    def run(self):
        print("Library management thread started.")
        while True:
            time.sleep(10)  # Auto-save every 10 seconds
            self.library.save_data()

# Main Program
def main():
    library = Library("Central Library")
    library_thread = LibraryThread(library)
    library_thread.daemon = True  # Ensures the thread stops when the main program exits
    library_thread.start()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List Books")
        print("5. Save and Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            try:
                copies = int(input("Enter number of copies: "))
            except ValueError:
                print("Invalid input for copies. Defaulting to 1 copy.")
                copies = 1
            book = Book(title, author, isbn, copies)
            library.add_book(book)

        elif choice == 2:
            isbn = input("Enter book ISBN to remove: ")
            try:
                quantity = int(input("Enter quantity to remove: "))
            except ValueError:
                print("Invalid input for quantity. Defaulting to 1 copy.")
                quantity = 1
            library.remove_book(isbn, quantity)

        elif choice == 3:
            keyword = input("Enter keyword to search: ")
            library.search_book(keyword)

        elif choice == 4:
            library.list_books()

        elif choice == 5:
            library.save_data()
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
