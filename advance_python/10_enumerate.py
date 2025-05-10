def print_alphabet():
    l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for index, letter in enumerate(l1):
        print(f"The letter at index {index} is {letter}")

# print_alphabet()


def print_books():
    books = ["The Alchemist", "1984", "To Kill a Mockingbird",
             "The Great Gatsby", "Moby Dick"]

    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")


print_books()
