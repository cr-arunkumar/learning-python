# creating a  function
def add_numbers(a, b):
    """
    This function adds two numbers.
    """
    return a + b
def add_numbers_args(*args):
    print(type(args))
    """
    This function adds all the arguments passed to it.
    """
    return sum(args)

# calling the function
print(add_numbers(3, 5),type(add_numbers))
print(add_numbers_args(2,3,45,6,5,6,44),type(add_numbers_args))

# we can pass the arguments as key-value pairs
print("----------------------------------------------------------------")
def add_numbers_keys(*args,**kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    """
    This function adds all the key-value pairs passed to it.
    """
    return sum(kwargs.values())

# calling the function with key-value pairs
print(add_numbers_keys(a=2, b=3),type(add_numbers_keys))

# we can also pass arguments as a list of tuples
print("----------------------------------------------------------------")
def add_numbers_list_of_tuples(*args):
    print(type(args), args)
    """
    This function adds all the numbers in the list of tuples passed to it.
    """
    total = 0
    for num_tuple in args:
        total += sum(num_tuple)
    return total

# calling the function with a list of tuples
print(add_numbers_list_of_tuples((2,3), (4,5), (6,7)), type(add_numbers_list_of_tuples))


# function definitions cannot be empty 
# we can use pass keyword to avoid error 
print("----------------------------------------------------------------")
def empty_function():
    pass

print("-------------------------")

# Positional-Only Arguments - we can specify that a function can have ONLY positional 
# arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:


def positional_only_args(a, /, b, c,*args,**kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    return a + b + c
print(positional_only_args(1, 2, 3))  # Positional-only arguments


def my_function(x, /):
      print(x)

# my_function(x = 3)  #error got positional-only atguments as keyword arguments
# Keyword-Only Arguments
# we can specify a function that can have only accept keyword arguments using "*"
print("-------------------keyword arguments only---------------------------------------------")

def keyword_only_args(*, a, b, c):
    return a + b + c

print(keyword_only_args(c=98,a=-18,b=-80))  # Keyword-only arguments

# Combine Positional-Only and Keyword-Only

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def combine_positional_and_keyword_args(a, /, b, c, *, d, e):
    return a + b + c + d + e

print(combine_positional_and_keyword_args(1, 2, 3, d=4, e=5))  # Combine Positional-Only and Keyword-Only arguments


# Lamda Function 
print("-------------------Lamda Function---------------------------------------------")
'''
A lamda function is an anonymous function
it can take any number of arguments but can only have one expression

Syntax:
lambda arguments : expression

'''
add = lambda x, y: x + y
print(add(3, 5))

from functools import reduce
 
multiplication_n = lambda *args: reduce(lambda x, y: x * y, args)
print(multiplication_n(1, 2, 3,4,5,6)) # multiplication


def fun_closer(initial_value):
    count = [initial_value]
    return lambda value: (count.insert(0,count[0] + value) or count[0])

counter = fun_closer(10)
print(counter(5))   # Output: 15 
print(counter(-3))  # Output: 12 
print(counter(2))   # Output: 14 
print(counter(-4))  # Output: 10 