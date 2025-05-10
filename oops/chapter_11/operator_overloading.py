class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n


a = Number(1)
b = Number(2)
# print(a + b)

# ##################### Common Magic Dunder Methods ############################


class MyClass:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"MyClass with value {self.x}"


obj = MyClass(10)
# print(obj)  # Output: MyClass with value 10

# compare with teh previus 'MyClass' for __str__


class MyClass:
    def __init__(self, x):
        self.x = x

    def hello(self):
        return f"MyClass with value {self.x}"


obj = MyClass(10)
# print(obj.hello())  # Output: MyClass with value 10

"""Create a class called Book with two attributes: title and author.

Add an __init__ method to store the title and author.

Add a __str__ method so that when you print a Book object, it shows:"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# list_of_books = [
#     Book("The Catcher in the Rye", "J.D. Salinger"),
#     Book("To Kill a Mockingbird", "Harper Lee"),
#     Book("1984", "George Orwell"),]

# for book in list_of_books:
#     print(book)

books = [
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),
    ("Animal Farm", "George Orwell")
]

# author_to_filter = "George Orwell"

# for title, author in books:
#     # Create a new Book instance
#     book = Book(title, author)

#     # Apply the filter to print only books by George Orwell
#     if book.author == author_to_filter:
#         print(book)


"""Add Book object instances using loop"""
# books = [
#     ("The Catcher in the Rye", "J.D. Salinger"),
#     ("To Kill a Mockingbird", "Harper Lee"),
#     ("1984", "George Orwell"),
# ]

# book_objects = {}

# for title, author in books:
#     key = title.lower().replace(" ", "_")
#     book_objects[key] = Book(title, author)
""""""
