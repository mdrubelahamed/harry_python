# Write a program to print the content of a list using while loops
# Example list with multiple contents
example_list = [1, "apple", 3.14, True, "banana", 42, "Python", False, 7.89, "grape"]

# i = 0
# while i < len(example_list):
#     print(example_list[i])
#     i += 1

# for with else

# for i in range(4):
#     print(i)
# else:
#     print("Done")


# PRACTICE SET
# 1. Write a program to print multiplication table of a given number using for loop.
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")


# multiplication_table(10)

# 2. Write a program to greet all the person names stored in a list ‘l’ and which stars with S. l = ["Harry", "Soham", "Sachin", "Rahul"]
l = ["Harry", "Soham", "Sachin", "Rahul"]


def greet_names_starting_with_s(l):
    for name in l:
        if name[0].lower() == "s":
            print(f"Good Morning! {name}")


# greet_names_starting_with_s(l)


# 3. Attempt problem 1 using while loop.
# PROBLEM 1. Write a program to print multiplication table of a given number using for loop.
def multiplication_table_using_while_loop(num):
    i = 1
    while i <= 10:
        print(f"{num} X {i} = {num * i}")
        i += 1


# multiplication_table_using_while_loop(10)


# 4. Write a program to find whether a given number is prime or not.
def is_prime_number():
    num = int(input("Enter a number: "))

    if num < 2:
        return f"{num} is not a prime number."

    if num == 2:
        return f"{num} is a prime number."

    for i in range(2, int((num**0.5) + 1)):
        if num % i == 0:
            return f"{num} is not a prime number."
    return f"{num} is a prime number."


# print(is_prime_number())


# 5. Write a program to find the sum of first n natural numbers using while loop.
def sum_of_first_n_natural_number(num):
    i = 1
    total = 0
    while i <= num:
        total += i
        i += 1
    return total


# approach 2 (Without loop) // efficient and much faster
def sum_of_first_n_natural_number(num):
    return (num * (num + 1)) // 2


# print(sum_of_first_n_natural_number(10))


# 6. Write a program to calculate the factorial of a given number using for loop.
def factorial(num):
    i = 1
    total = 1

    if num < 0:
        return "Factorial is not defined for negative numbers."

    if num == 0:
        total = 0
        return 1

    # using for loop
    for i in range(i, num + 1):
        total *= i
    return total


# print(factorial(0))

"""
For n = 3
  *
 ***
*****
"""


def print_pyramid():
    n = int(input("Enter the number for pyramid pattern: "))
    for i in range(1, n + 1):
        space = n - i
        stars = 2 * i - 1
        pattern = " " * space + "*" * stars

        print(f"{' ' * space}{'*' * stars}")
        # print(pattern)


# print_pyramid()


"""8. Write a program to print the following star pattern:
for n =3
*
**
***
"""


def print_star():
    n = int(input("Enter a int number: "))
    for i in range(1, n + 1):
        # pattern = "*" * i
        # print(pattern)
        print(f"{'*' * i}")


# print_star()

"""
9. Write a program to print the following star pattern.
for n = 3
* * *
*   *
* * * 

=> for 1st and last line all start based on n
=> inside the all middle line only the start and finish star

"""


def print_square_border_pattern(num):
    for i in range(1, num + 1):
        if i == 1 or i == num:
            print("*" * num)
        else:
            if num > 2:
                print("*" + " " * (num - 2) + "*")
            else:
                print("*" * num)  # For very small numbers like 2


# print_square_border_pattern(5)


# 10. Write a program to print multiplication table of n using for loops in reversed order
def multiplication_table_reversed_order():
    num = int(input("Enter which number table you want? "))

    # # approach 1
    # for i in range(1, 11):
    #     print(f"{num} * {11 - i} = {num * (11 - i)}")

    # approach 2 (better)
    for i in range(10, 0, -1):
        print(f"{num} * {i} = {num * i}")


# multiplication_table_reversed_order()
