# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

def student_details():
    name = input("What is your name? ")
    marks = int(input("Enter your marks: "))
    phone_number = int(input("Enter you mobile no: "))

    # return f"The name of the student is {name.title()}, his marks are {marks} and phone number is {phone_number}"

    return "The name of the student is {}, his marks are {} and phone number is {}".format(name.title(), marks, phone_number)

# print(student_details())

"""
3. A list contains the multiplication table of 7. write a program to convert it to vertical
string of same numbers.
"""
multiplication_table = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

for num in multiplication_table:
    print(str(num))