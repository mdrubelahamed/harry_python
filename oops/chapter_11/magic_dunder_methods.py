"""
Magic Dunder Methods in Python

Magic methods (also called dunder methods, short for "double underscore") in Python are special methods that allow you to define how your objects behave with built-in Python operators and functions. These methods are not explicitly called in your code, but instead are invoked automatically when you perform specific actions, like adding two objects or printing an object.

How Do Magic Methods Work?

Magic methods have a double underscore prefix and suffix (e.g., __add__, __str__). They allow you to:

1. Customize how operators (like +, -, ==, etc.) work with your class.
2. Define how objects of your class should behave with Python functions like len(), str(), or repr().
3. Override default behaviors for built-in operations.

Common Magic Methods:

1. __init__(self, ...): The constructor, called when an object is created.
2. __str__(self): Called by str() or print() to return a string representation of the object.
3. __repr__(self): Called by repr() to return a string that represents the object for debugging.
4. __add__(self, other): Called when the + operator is used between two objects.
5. __eq__(self, other): Called when the == operator is used to compare two objects.
6. __len__(self): Called by len() to return the length of an object.

Example: Using __str__, __repr__, and __add__ in a Class

Let's combine a few of these methods to create a simple Product class, which will use __str__, __repr__, and __add__:
"""

"""
Example: Using `__str__`, `__repr__`, and `__add__` in a Class
"""

# 1. __init__(self, ...): The constructor, called when an object is created.


class MyClass:
    def __init__(self, x):
        self.x = x


# obj = MyClass(10)
# print(obj.x)  # 10

# --------------------------------------------------------------------------------------------
# 2. __str__(self): Called by str() or print() to return a string representation of the object.
class MyClass:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"MyClass with value {self.x}"

# obj = MyClass(10)
# print(obj)  # Output: MyClass with value 10

# -----------------------------------------------------------------------------------------------
# 3. __repr__(self): Called by repr() to return a string that represents the object for debugging.


class MyClass:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"MyClass({self.x})"


# obj = MyClass(10)
# print(repr(obj))  # Output: MyClass(10)

# -------------------------------------------------------------------------------
# 4. __add__(self, other): Called when the + operator is used between two objects.


class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

    def __str__(self):
        return f"Value: {self.value}"


# a = MyClass(5)
# b = MyClass(10)
# c = a + b
# print(c)  # Output: Value: 15

# ----------------------------------------------------------------------------------
# 5. __eq__(self, other): Called when the == operator is used to compare two objects.


class MyClass:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x


# a = MyClass(10)
# b = MyClass(10)
# print(a == b)  # Output: True

# -------------------------------------------------------------------------------
# 6. __len__(self): Called by len() to return the length of an object.


class MyClass:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


# obj = MyClass([1, 2, 3])
# print(len(obj))  # Output: 3


# --------------------------------------------------------------------------------------------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # String representation for user-friendly display
    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}"

    # Detailed representation for debugging
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    # Add two products' prices
    def __add__(self, other):
        return Product(self.name + " & " + other.name, self.price + other.price)


# Example usage:
p1 = Product("Laptop", 1000)
p2 = Product("Phone", 500)


# print(p1)           # Output: Product: Laptop, Price: $1000
# print(repr(p1))     # Output: Product('Laptop', 1000)
# p3 = p1 + p2
# print(p3)           # Output: Product: Laptop & Phone, Price: $1500
