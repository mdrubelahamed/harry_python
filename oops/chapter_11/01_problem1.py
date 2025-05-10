# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vector is x:{self.x}, y:{self.y}")


class vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The vector is x:{self.x}, y:{self.y}, z:{self.z}")


# example usage
a = Vector2D(1, 2)
a.show()
b = vector3D(1, 2, 3)
b.show()