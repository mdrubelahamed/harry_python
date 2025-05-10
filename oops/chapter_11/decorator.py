
def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function


@decorator
def initial_function():
    print("Initial Functionality")


initial_function()

"""
What's happening
You defined a decorator function decorator that takes another function f as an argument. Inside decorator, you defined a new function new_function. This new_function calls the original function f using f().

When you applied the @decorator syntax above initial_function, it's equivalent to writing:
initial_function = decorator(initial_function)

"""
