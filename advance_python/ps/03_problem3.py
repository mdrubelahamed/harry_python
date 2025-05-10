# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter you multiplication number: "))
multiplication_table = [f"{n * i}" for i in range(1, 11)]

print(multiplication_table)
