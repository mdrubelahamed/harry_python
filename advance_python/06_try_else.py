try:
    a = int(input("Enter a number: "))

except ValueError as e:
    print(e)

else:
    print("I am inside else.")

# Code will only go to 'else' block if it successfully executes the try block,
# which means there were no exceptions raised in the try block.
