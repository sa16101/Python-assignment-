# Task 1: Read a File and Handle Errors

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes extra spaces/newlines

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

