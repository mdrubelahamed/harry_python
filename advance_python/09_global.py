a = 89
# access and modify global variable in a function


def func():
    a = 3


def access_global():
    """Access and print the global variable."""
    print(f"inside func a: {a}")


func()
print(f"global value of a : {a}")


# want to access global value inside a func also change the global value

def func2():
    global a
    a = 3
    print(f"inside func2 a: {a}")


func2()
print(f"global value of a : {a}")
