import sqlite3
from datetime import datetime

# Initialize the database
def initialize_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            user TEXT NOT NULL,
            type TEXT NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
    """)
    conn.commit()
    conn.close()

# Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def save_to_database(self):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO books (title, author, year) VALUES (?, ?, ?)
        """, (self.title, self.author, self.year))
        conn.commit()
        conn.close()

# Library Management
class Library:
    @staticmethod
    def add_book():
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = int(input("Enter publication year: "))
        book = Book(title, author, year)
        book.save_to_database()
        print(f"Book '{title}' added successfully!")

    @staticmethod
    def view_books():
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        print("\nLibrary Books:")
        print("ID | Title                | Author              | Year | Status")
        print("-" * 60)
        for book in books:
            print(f"{book[0]:<3} | {book[1]:<20} | {book[2]:<20} | {book[3]:<4} | {book[4]}")
        conn.close()

    @staticmethod
    def borrow_book():
        Library.view_books()
        book_id = int(input("\nEnter the ID of the book to borrow: "))
        user = input("Enter your name: ")
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        if book and book[0] == "Available":
            cursor.execute("UPDATE books SET status = 'Borrowed' WHERE id = ?", (book_id,))
            cursor.execute("""
                INSERT INTO transactions (book_id, user, type, date)
                VALUES (?, ?, 'Borrow', ?)
            """, (book_id, user, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            print("Book borrowed successfully!")
        else:
            print("Sorry, the book is not available!")
        conn.close()

    @staticmethod
    def return_book():
        Library.view_books()
        book_id = int(input("\nEnter the ID of the book to return: "))
        user = input("Enter your name: ")
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        if book and book[0] == "Borrowed":
            cursor.execute("UPDATE books SET status = 'Available' WHERE id = ?", (book_id,))
            cursor.execute("""
                INSERT INTO transactions (book_id, user, type, date)
                VALUES (?, ?, 'Return', ?)
            """, (book_id, user, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            print("Book returned successfully!")
        else:
            print("The book is not marked as borrowed!")
        conn.close()

    @staticmethod
    def view_transactions():
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.id, b.title, t.user, t.type, t.date
            FROM transactions t
            JOIN books b ON t.book_id = b.id
        """)
        transactions = cursor.fetchall()
        print("\nTransactions:")
        print("ID | Book Title          | User               | Type    | Date")
        print("-" * 70)
        for transaction in transactions:
            print(f"{transaction[0]:<3} | {transaction[1]:<20} | {transaction[2]:<18} | {transaction[3]:<7} | {transaction[4]}")
        conn.close()

# Main menu
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View Transactions")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Library.add_book()
        elif choice == "2":
            Library.view_books()
        elif choice == "3":
            Library.borrow_book()
        elif choice == "4":
            Library.return_book()
        elif choice == "5":
            Library.view_transactions()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Initialize database and run the program
if __name__ == "__main__":
    initialize_database()
    main_menu()
