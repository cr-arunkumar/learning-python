# namespace in python
#  is a collection of variables, functions, classes, and modules that are grouped together.
# types of namespaces:
'''
 1 . Global namespace: This is the main namespace that contains all global variables.
 eg. global_var = "I am global variable"

 2. Local namespace: This is created when a function is called. It contains local variables and arguments.
 eg. def print_local_var():
    local_var = "I am local variable"
    print(local_var)

 3. Built-in namespace: This contains all built-in functions, variables, and classes in Python.
 eg. print(),id() etc.
 print("Hello, World!")
 '''
# Closure in python
'''
A closure is a function object that 
remembers values in enclosing scopes even if they're not present in memory.
'''
# closures can be created using nested functions
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # Outputs: 15
print(closure(10))  # Outputs: 20



def counter_factory(start=0):
    count = start
    def counter():
        nonlocal count  # Needed to modify enclosing variable
        # (it means it behaving as outer fun variable)
        count += 1
        return count
    return counter

c1 = counter_factory()
print(c1())  # 1
print(c1())  # 2

c2 = counter_factory(10)
print(c2())  # 11 

# decorators in python
# decorators are functions that take another function as an argument and return a new function.
# it is much similar to highrer order functions in js 
def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        print("Before function execution")
        func(*args, **kwargs)
        print("After function execution")
    return wrapper_function

def wait_for_seconds(seconds):
    import time
    time.sleep(seconds)

def do_later_work(duration_sec):
    print("Doing later work")
    wait_for_seconds(duration_sec)
    print('My work is done')
    return "Done"

my_func=decorator_function(do_later_work)
my_func(0)

# istead of assigning the function to a variable, 
# we can use it directly as decorator with @ symbol

print("\n --------------- -------------- Decorator Example ----------------- \n")

@decorator_function
def do_later_work_with_decorator(sec):
    print("Doing later work")
    wait_for_seconds(sec)
    print('My work is done')
    return "Done"

do_later_work_with_decorator(0)


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello {name}")

say_hello("Alice")

from functools import cache
import time
# either we can use @cache decorator or mannually caching the results
def fibonacci(n,mp):
    if n <= 1:
        return n
    if n not in mp:
        mp[n] = fibonacci(n-1, mp) + fibonacci(n-2, mp)
    return mp[n]

start_time = time.time()
mp={}
print(fibonacci(899,mp))
print(f"Time taken: {time.time() - start_time} seconds")
