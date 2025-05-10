import random


# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft
class Programmer:
    company = "Microsoft"

    def __init__(self, name, language):
        self.name = name
        self.language = language


harry = Programmer("harry", "python")
# print(harry.name, harry.language, harry.company)

josh = Programmer("josh", "python")
# print(josh.name, josh.language, josh.company)

nasim = Programmer("nasim", "python")
# print(nasim.name, nasim.language, nasim.company)


# 2. Write a class “Calculator” capable of finding square, cube and square root of a number
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** (1/2)

    @staticmethod
    def greet():
        return "Hello!"


calc = Calculator(9)

# print(calc.square())
# print(calc.cube())
# print(calc.square_root())
# print(calc.greet())

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


class Demo:
    a = 4


o = Demo()
# o.a = 2
# print(o.a)


# 4. Add a static method in problem 2, to greet the user with hello.
# done => check in problem 2

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:

    def __init__(self, train_no):
        self.train_no = train_no

    def book_ticket(self, start, end):
        return f"Ticket is booked in train no: {self.train_no} from {start} to {end}."

    def get_status(self):
        return f"Train {self.train_no} is running successfully."

    def get_fare(self, start, end):
        return f"Ticket fare in train no: {self.train_no} from {start} to {end} is {random.randint(10, 500)}$ ."


t = Train(123543)
# print(t.book_ticket("howrah", "malda"))
# print(t.get_status())
# print(t.get_fare("howrah", "malda"))

# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.


class Demo2:
    def __init__(slf, name):
        slf.name = name

    def desc(slf):
        return f"Name: {slf.name}"


# d = Demo2("rex")
# print(d.desc())
