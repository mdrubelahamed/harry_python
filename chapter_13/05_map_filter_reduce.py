from functools import reduce

# Map example
list1 = [1, 2, 3, 4, 5]
def square(x): return x * x


sq_list = map(square, list1)
# for i in sq_list:
#     print(i)

# print(list(sq_list))


#  Filter Example
"""
filter(function, iterable)
function: returns True if the item should be included.
iterable: the data you want to filter (list, tuple, etc.).
⚡ Returns a filter object → convert it to list() or tuple() to see results.
"""


def even(n):
    return n % 2 == 0


result = filter(even, list1)
# print(list(result))

# Reduce

# sum using reduce


def sum(a: int, b: int) -> int:
    return a + b


print(reduce(sum, [1, 2]))

# multiply using reduce

# syntax : reduce(func, iterable, optional)
# optional is from where it will start since we are multipling i gave it 1
mul = reduce(lambda x, y: x * y, list1, 1)
print(mul)
