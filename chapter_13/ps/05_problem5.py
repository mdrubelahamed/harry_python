# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce


list1 = [i for i in range(1, 20)]

result = reduce(lambda x, y: x if x > y else y, list1)
print(result)
