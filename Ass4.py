# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to a file
user_input = input("Enter some data to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")  # Writing user input

print("Data written to output.txt.")

# Step 2: Append additional data
append_data = input("Enter additional data to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_data + "\n")  # Appending data

print("Data appended to output.txt.")

# Step 3: Read and display the final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
