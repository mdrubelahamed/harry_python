def get_user_input_and_handle_exceptions():
    try:
        user_input = int(input("Please enter the first number: "))
        print(user_input)
    except ValueError as error:
        print(error)
    finally:
        print("Thank you for your input.")

# get_user_input_and_handle_exceptions()


def divide_two_numbers_and_handle_exceptions():
    try:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))

        if b == 0:
            raise ZeroDivisionError("The second number cannot be 0.")
        else:
            print(
                f"The division of {a} by {b} is {a / b}.")

    except ValueError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)

    finally:
        print("Thank you for your input.")


divide_two_numbers_and_handle_exceptions()
