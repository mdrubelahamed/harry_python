# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.
l1 = [1, 2, 3, 4, 5, 6, 7, 8]

for index, num in enumerate(l1):
    if index in [2, 4, 6]:
        print(num)
