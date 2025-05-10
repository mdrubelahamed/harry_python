# Notes/Important topic 
1. Modules, Comment, pip
2. Variable, Data type
3. Strings
4. List, Tuples
5. Dictionary, Set
6. Conditional Expression
7. Loops in python
8. Functions, Recursions
9. Snake, Water, Gun - Game (project 1)
10. oop
11. Inheritance
12. Guessing Game (project 2)
13. Advance Python




``git rev-parse --is-inside-work-tree >/dev/null 2>&1 && echo "Git repo" || echo "Not a Git repo"``


## Test code for new themes in python
```
import math
import datetime


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement this")

    def __str__(self):
        return f"{self.name} Shape"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Circle(2.3),
    ]

    for shape in shapes:
        try:
            print(f"{shape}: Area = {shape.area():.2f}")
        except Exception as e:
            print(f"Error: {e}")

    now = datetime.datetime.now()
    print(f"Script ran on: {now.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
```