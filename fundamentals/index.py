# syntax,variables, and comments
print("Hello world!")
x,y,z =1,2,3
print(x,y,z)

# This is a comment
# single comment
# single comment
# multiple comments
"""
this is multi-line comment
"""

"""
# user input
name = input("Enter your name: ")
print("Hello", name)
# //take multiple input 
names = input("Enter multiple names separated by comma: ").split(",")
print(names)
description = input("Enter your description:\n")
print(description)
# take input and cast into different types
num = int(input("Enter a number: "))
print(num * 2,"type of ",type(num))
# more
MyFloat = float(input("Enter a float: "))
print(MyFloat * 2,"type of",type(MyFloat))

fruits=["apple", "mango", "banana", "cherry"]
f1,f2,f3,f4=fruits
print(f1,f2,f3,f4)
"""

# global variables
global_var = "This is global variable"
def print_global_var():
    local_var = "This is local variable"
    global_var="This is global variable inside function wala"
    print(local_var)
    print(global_var)

print_global_var()

g="this is a strict global variable"

def print_global_var():
    global g 
    g="this is a strict global variable inside function wala"
    print(g)

print_global_var()
print(g)
