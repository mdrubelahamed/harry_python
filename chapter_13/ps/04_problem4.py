# 4. Write a program to filter a list of numbers which are divisible by 5.

list1 = [i for i in range(1, 50)]

result = filter(lambda x : x % 5 == 0, list1)
print(list(result))
