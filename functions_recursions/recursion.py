# factorial using recursion


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number: "))
print(factorial(n))

"""
The programmer needs to be extremely careful while working with recursion to ensure
that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
direct way to code an algorithm.
"""
