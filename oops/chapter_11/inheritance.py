class Programmer:
    language = "Python"

    def getLanguage(self):
        print(f"Language: {self.language}")


class Coder:
    language = "Java"

    def getLanguage(self):
        print(f"Language: {self.language}")


class Employee(Programmer, Coder):
    comapny = "Google"

    def show(self):
        print(f"Company Name: {self.comapny}")


e = Employee()
# e.show()

# e.getLanguage()  # Output: Language: Python
"""
Why:
Because of Method Resolution Order (MRO) in Python.
In class Employee(Programmer, Coder), Programmer is listed first.
Python looks for methods in the first parent (Programmer) before checking the next (Coder).

Since Programmer has a getLanguage method, Python uses that — even though Coder also has one.
"""


# ################### Multilevel Inheritance ###################
class GrandParent:
    def show_grandparent(self):
        print("I am grandparent")


class Parent(GrandParent):
    def show_parent(self):
        print("I am parent")


class Child(Parent):
    def show_child(self):
        print("I am child")


c = Child()
# c.show_grandparent()  # Output: I am grandparent
# c.show_parent()  # Output: I am parent
# c.show_child()  # Output: I am child

print(len("My ability to select your most important task at each momen"))
