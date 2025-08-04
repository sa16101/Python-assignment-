import math

# 1. Ask the user for a number as input
number = float(input("Enter a number: "))

# 2. Perform mathematical calculations using math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)  # number is considered in radians

# 3. Display the calculated results
print(f"\nResults for the number {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm (base e): {natural_log}")
print(f"Sine (in radians): {sine_value}")
