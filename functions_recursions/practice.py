# PRACTICE SET
# 1. Write a program using functions to find greatest of three numbers.
def greatest_among_three_numbers():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))

    return max(num1, num2, num3)

    # print(greatest_among_three_numbers())


# 2. Write a python program using function to convert Celsius to Fahrenheit.
# F = (C * 9 / 5) + 32
def celsius_to_fahrenheit():
    celsius = float(input("Enter Temperature in °C: "))
    fahrenheit = (celsius * 9 / 5) + 32

    # Return as integer if Fahrenheit value is a whole number (e.g., 98.0 → 98), else keep it as float
    return int(fahrenheit) if fahrenheit.is_integer() else fahrenheit


# print(celsius_to_fahrenheit())


# 3. How do you prevent a python print() function to print a new line at the end.
def prevent_new_line_at_print():
    for i in range(5):
        print(i, end=" ")


# prevent_new_line_at_print()


# 4. Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_first_n_natural_number(n):
    if n == 1:
        return 1
    return n + sum_of_first_n_natural_number(n - 1)


# print(sum_of_first_n_natural_number(5))

"""
5. Write a python function to print first n lines of the following pattern:
for n = 3
***
** 
*
"""


def generate_star_pattern():
    n = int(input("Enter n value: "))
    pattern = ""
    for i in range(n, 0, -1):
        # not the best approach probably but try new approach
        pattern += "*" * i
        if i > 1:
            pattern += "\n"
    return pattern


# print(generate_star_pattern())


# 6. Write a python function which converts inches to cms.
def inch_to_cm():
    inch = float(input("Enter the inch value: "))
    cm = inch * 2.54

    return int(cm) if cm.is_integer() else cm


# print(inch_to_cm())

# 7. Write a python function to remove a given word from a list ad strip it at the same time


def remove_word_from_list(word_to_remove, word_list):
    cleaned_words = []

    for word in word_list:
        stripped_word = word.strip()
        if stripped_word.lower() != word_to_remove.lower():
            cleaned_words.append(word.strip())

    return cleaned_words


words = [" apple ", "banana", "  orange", "banana ", "grape "]
word_to_remove = "banana"

# print(remove_word_from_list(word_to_remove, words))


# 8. Write a python function to print multiplication table of a given number.
def multiplication_table():
    number = int(input("Which number's multiplication table would you like? "))

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")



# multiplication_table()
