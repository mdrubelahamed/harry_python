# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    """
    z1 = a + bi
    z2 = c + di
    z1 * z2 = (ac -bd) + (ad + bc)i
    """

    def __mul__(self, other):
        real = (self.r * other.r - self.i * other.i)
        imaginary = (self.r * other.i + self.i * other.r)

        return Complex(real, imaginary)

    def __str__(self):
        return f"{self.r} + {self.i}i"


a = Complex(1, 2)
b = Complex(3, 4)
# print(a)
# print(a + b)
# print(a * b)
