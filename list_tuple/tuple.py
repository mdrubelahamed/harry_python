# t1 = (1, 2, 3)
# print(t1)

# how to create an empty tuple
# a = 1  # ❌ it will evaluate as int
# a = (1,)  # ✅ it will evaluate as tuple

# tuple is immutable
a = (1, 7, 2)
# print(a.count(2)) # count of '2' how many times in the tuple
# print(a.index(7))  # return the index of the value  in first occurance


# PRACTICE SET
# 3. Check that a tuple type cannot be changed in python.
names = ("Rex", "batman")
# names.append("zuck") # return an error since tupel are immutable


# 5. Write a program to count the number of zeros in the following tuple:
def count_zeros():
    """Return how many zeros present in the tuple 'a'"""

    a = (7, 0, 8, 0, 0, 9)
    count_zero = a.count(0)
    return count_zero


# print(count_zeros())
