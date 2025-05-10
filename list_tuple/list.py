l1 = [10, True, 4, 5, 1, True, 2, False]
# l1.sort()
# l1.pop() # remove the last element if index not given
# l1.remove(2) # remove value 2 from the list
# l1.insert(3, 333)  # insert '333' at index 3
# print(l1)


# PRACTICE SET
# 1. Write a program to store seven fruits in a list entered by the user.
def get_fruits_list_from_user(fruits_count):
    fruits = []
    for i in range(1, 8):
        fruit = input(f"Enter fruit {i} name: ")
        fruits.append(fruit)
    return fruits


# print(get_fruits_list_from_user())


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
def sort_students_based_on_marks():
    students = []
    for i in range(1, 7):
        marks = int(input(f"Enter student {i} marks: "))
        students.append(marks)
    students.sort()
    return students


# print(sort_students_based_on_marks())


# 4. Write a program to sum a list with  numbers.
def sum_of_list_elements(numbers_count):
    """Take input of 'numbers_count' numbers and return their sum."""

    numbers = []

    for i in range(numbers_count):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)

    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum


# print(sum_of_list_elements(4))
