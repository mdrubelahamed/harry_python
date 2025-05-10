# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.


class Vector:
    def __init__(self, l):
        self.l = l

    def __add__(self, other):
        result = Vector([self.l[i] + other.l[i] for i in range(len(self.l))])
        return result

    def __mul__(self, other):
        result = sum([self.l[i] * other.l[i] for i in range(len(self.l))])
        return result

    def __str__(self):
        return f"Vector({', '.join(str(i) for i in self.l)})"

    def __len__(self):
        return len(self.l)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)
print(len(v1))
