def list_current_directory_contents():
    """Print the contents of the current directory using the os module."""

    import os

    # Get the path of the current directory
    path = os.getcwd()

    # List contents of the directory
    contents = os.listdir(path)

    # Print each item
    for item in contents:
        print(item)


# list_current_directory_contents()


# 2. Write a python program to find remainder when a number is divided by z.
def find_remainder(dividend, divisor):
    """return the remainder using two param(dividend, divisor)"""

    remainder = dividend - ((dividend // divisor) * divisor)
    return remainder


# print(find_remainder(24, 5))

# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80


def is_a_greater_than_b(a, b):
    "return a is greater than b or not"

    if a > b:
        return f"a is greater than b"
    return f"b is greater than a"


# print(comparision_check(34, 80))


# 5. Write a python program to find an average of two numbers entered by the user.
def average_of_two_num():
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    num3 = float(input("Enter num3: "))

    return "{:.2f}".format((num1 + num2 + num3) / 3)


# print(average_of_two_num())


# 6. Write a python program to calculate the square of a number entered by the user.
def square_of_a_number(num):
    """return square of a number given by user"""
    return num**2


# print(square_of_a_number(25 ))


# Write a python program to display a user entered name followed by Good Afternoon using input () function.
def greet():
    """user name in title case followed by Good Afternoon!"""

    username = input("Enter your name: ")
    if len(username) > 0:
        return f"Good Afternoon, {username.title()}"
    else:
        return f"Provide a valid user name"


# print(greet())

# 2. Write a program to fill in a letter template given below with name and date.
letter = """
Dear <|Name|>,
You are selected!
<|Date|>"""


def fill_in_the_blanks():
    name = input("Suggest a name: ")
    date = input("Suggest a date(DDMMYYYY): ")

    filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)
    return filled_letter


# print(fill_in_the_blanks())

# 3. Write a program to detect double space in a string.
# str = "this string has double space  inside it."
# print(str.find("  "))

letter = "Dear Rex,\n\tThis python course is nice.\nThanks!"
print(letter)
