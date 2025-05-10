#  3. Create a class ‘Employee’ and add salary and increment properties to it.
class Employee:
    salary = 100
    increment = 20

    @property
    def salary_after_increment(self):
        return self.salary + ((self. salary * self.increment) / 100)

    @salary_after_increment.setter
    def salary_after_increment(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()
# print(e.salary_after_increment)
e.salary_after_increment = 300
print(e.increment)
