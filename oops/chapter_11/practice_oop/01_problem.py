class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available  # True/False

    def __str__(self):
        if self.available:
            return f"Book: {self.title} written by {self.author}. Isbn no of this book: {self.isbn} and it is available to read."
        return f"Book: {self.title} written by {self.author}. Isbn no of this book: {self.isbn} and it is not available to read."


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                print(f"{book.title} has been borrowed.")
                return
        print("Book is either not available or does not exist.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                print(f"{book.title} has been returned.")
                return
        print("Book was not borrowed or does not exist.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(book)
        else:
            print("No books available.")


# Creating books
atomic_habits = Book("Atomic Habits", "James Clear", 9788075550989, True)
rich_dad_poor_dat = Book(
    "Rich Dad Poor Dad", "Robert Kiyosaki", 9781591843609, False)
eat_that_frog = Book("Eat That Frog", "Tim Ferriss", 9781591843620, True)
deep_work = Book("Deep Work", "Cal Newport", 9781455586691, True)
the_power_of_habit = Book("The Power of Habit",
                          "Charles Duhigg", 9780812981605, True)

# Initialize library and add books
library = Library()
library.add_book(atomic_habits)
library.add_book(rich_dad_poor_dat)
library.add_book(eat_that_frog)
library.add_book(deep_work)
library.add_book(the_power_of_habit)

# Borrow a book
library.borrow_book(9781591843609)  # Borrow "Rich Dad Poor Dad"

# List available books
library.list_available_books()

# Return a book
library.return_book(9781591843609)  # Return "Rich Dad Poor Dad"

# List available books again
library.list_available_books()
