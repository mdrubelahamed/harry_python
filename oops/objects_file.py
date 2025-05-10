# 1. create an object
class Student:
    college_name = "Kingston"
    age = 22

    # def greet(self):
    #     print("Good Morning.")

    # if we don't want to pass the object inside func wehre it isn't required
    @staticmethod
    def greet():
        print("Good Morning.")


rex = Student()
# print(rex.college_name, rex.age)

# will give an error
# rex.greet()
# TypeError: Student.greet() takes 0 positional arguments but 1 was given because,
# rex.greet() => Student.greet(rex)


# object with self init
class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def describe(self):
        return f"id: {self.id}\nname: {self.name}\nage: {self.age}"


# rohan = Employee(1, "Rohan", 22)
# print(rohan.id, rohan.name, rohan.age)
# print(rohan.describe())
