# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

# Calling the function with a sample number
sample_number = 5
result = factorial(sample_number)

# Printing the output
print(f"The factorial of {sample_number} is {result}")
