def myFunc():
    """
    Prints a message from a function
    """
    print("Hello from a function")
    print(__name__)  # this will be '__main__' if executed directly from the file


# This block of code will only run if this file is executed directly
# When a Python file is run, the special variable __name__ is set to "__main__"
# If the file is imported as a module, __name__ will be set to the module's name
# This allows us to separate code that should run on import from code that should run on execution
if __name__ == "__main__":
    myFunc()
