# This file demonstrates how Python's string formatting works with floating-point numbers

def main():
    # Example data - three numbers to average
    num1 = 10
    num2 = 15.75
    num3 = 20.333

    # Calculate the average
    average = (num1 + num2 + num3) / 3  # This equals 15.361

    print("Original format example:")
    print(f"   The average is: {average}")  # Without formatting
    
    # Using .format() with different precisions
    print("\nDifferent decimal precisions using .format():")
    print("   No decimal specification: {}".format(average))
    print("   Zero decimal places: {:.0f}".format(average))  # Rounds to nearest integer
    print("   One decimal place: {:.1f}".format(average))    # Rounds to 1 decimal place
    print("   Two decimal places: {:.2f}".format(average))   # Rounds to 2 decimal places
    print("   Four decimal places: {:.4f}".format(average))  # Rounds to 4 decimal places
    
    # Width and alignment
    print("\nWidth and alignment:")
    print("   Width of 10, right aligned: {:10.2f}".format(average))  # Width of 10, 2 decimal places
    print("   Width of 10, left aligned: {:<10.2f}".format(average))  # Left aligned
    print("   Width of 10, centered: {:^10.2f}".format(average))      # Centered
    
    # Including the sign
    print("\nControlling the sign:")
    print("   Always show sign: {:+.2f}".format(average))           # Show + for positive numbers
    print("   Space for positive numbers: {: .2f}".format(average)) # Space for positive numbers
    
    # Thousands separator
    large_number = 1234567.89
    print("\nUsing thousand separators:")
    print("   With comma separator: {:,.2f}".format(large_number))
    
    # Explaining our specific example
    print("\nExplaining the original example:")
    example_result = "{:.2f}".format((num1 + num2 + num3) / 3)
    print(f"   Input: num1={num1}, num2={num2}, num3={num3}")
    print(f"   Calculation: ({num1} + {num2} + {num3}) / 3 = {average}")
    print(f"   Formatted output: {example_result}")
    print("   This formats the result to exactly 2 decimal places, rounding if necessary.")

if __name__ == "__main__":
    main()

