my_list = [1, 2, 3, 4, 5]

squared_list = []
for number in my_list:
    squared_list.append(number ** 2)

print(squared_list)

# using list comprehension
squared_list = [number**2 for number in my_list]
# print(squared_list)
