class Employee:
    a = 1

    # but i want class attribute of a value
    @classmethod
    def show(cls):
        print(f"Value of a: {cls.a}")


e = Employee()
e.a = 45
e.show()
