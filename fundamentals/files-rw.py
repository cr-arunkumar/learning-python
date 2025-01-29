# File Handling in Python
# open() function is used to open a file in different modes
'''
"r" - read mode (default) if the file does not exist, Python will raise an error
"w" - write mode, if the file does not exist, a new file will be created. If the file exists, 
its content will be erased
"a" - append mode, if the file does not exist, a new file will be created. If the file exists,it will append 
"x" - exclusive creation mode, if the file already exists, Python will raise an error
'b" - binary mode for binary files (eg. images, audio files)
"t" - text mode (default) for reading text files (default)
"+" - read and write mode
'''

# Example 1: Opening a file in read mode
try:
    file = open("./fundamentals/demo.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
# Alternatively, you can use the 'with' statement to automatically close the file after use
try:
   with open("./fundamentals/demo.xt", "r") as file:
    print(file.read())
except FileNotFoundError:
    print("Error: File not found.")


# Example 2: Opening a file in write mode
try:
    file = open("./fundamentals/demo.txt", "w")
    file.write("This is a test file.\n") # it will overwrite the existing content 
    file.close()
except FileNotFoundError:
    print("Error: File not found.")

# Example 3: Opening a file in append mode
try:
    file = open("./fundamentals/demo.txt", "a+")
    file.write("This is an additional line.\n") # it will append the content to the end of the file
    file.seek(0)  # Move the file pointer back to the beginning of the file
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")


# Example 4: Opening a file in exclusive creation mode
try:
    file = open("./fundamentals/demo1.txt", "x")
    file.write("This is a test file.\n")
    file.close()
except FileExistsError:
    print("Error: File already exists.")


# Example 5: Binary mode for binary files
try:
    with open("./fundamentals/monkey.jpg", "rb") as file:
        # print(file.read())
        print(file.read(10),"....")  # Read first 100 bytes of the file
except FileNotFoundError as e:
    print("Error: File not found.",e)


# Example 6: Text mode for reading text files
try:
    with open("./fundamentals/demo.txt", "rt") as file:
        print(file.read())
except FileNotFoundError as e:
    print("Error: File not found.",e)

# Example 7: Reading a file line by line
try:
    with open("./fundamentals/demo.txt", "r") as file:
        for line in file:
            print(line.strip(),end="--")
except FileNotFoundError as e:
    print("Error: File not found.",e)


# Readline() function reads a single line from the file
print("\n----------------------------------------------------------------")
try:
    with open("./fundamentals/demo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError as e:
    print("Error: File not found.",e)

# Delete a file using os module
try:
    with open("./fundamentals/demo_testing.txt", "a+") as file:
        file.write("This is a test file for deletion.\n")
        file.seek(0)  # Move the file pointer back to the beginning of the file
        print(file.read())
except FileNotFoundError as e:
    print("Error: File not found.",e)

# delet the file 
try:
    import os
    os.remove("./fundamentals/demo_testing.txt")
    print("File deleted successfully.")
except FileNotFoundError as e:
    print("Error: File not found.",e)
except PermissionError as e:
    print("Error: Permission denied.",e)   
except Exception as e:
    print("An unexpected error occurred:",e) 

# Check if File exist:
if(os.path.exists("./fundamentals/demo.txt")):
    print("File exists.")
else:
    print("File does not exist.")

# delete the directory
# try:
#     os.rmdir("./test_dir")
#     print("Directory deleted successfully.")
# except FileNotFoundError as e:
#     print("Error: Directory not found.",e)

