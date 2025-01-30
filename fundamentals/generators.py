# Generators in Python are a simple way to create iterators. 
# it is used by defining a function with a yield statement instead of a return statement.
# When the function is called, it returns a generator object.
# Benefits of generators are:
#     - allows us to iterate over large data sets without loading the entire data set into memory
#     - saves memory when working with large data sets
#     - enables us to write code that is more readable and concise

def fib(nums):
    a, b = 0, 1
    for _ in range(nums):
        yield a
        a, b = b, a + b

def get_square(nums):
    for num in nums:
        yield num**2


print(sum(get_square(fib(10))))


# Generator expressions are a more compact way to create generators.

print("Generator expressions:")

def getNames():
    yield "John"
    yield "Alice"
    yield "Bob"
    yield "Charlie"

names = getNames()
print(type(names))

for name in names:
    print(name)

print("---------counter generator--------")
def counter_generator(n):
    value=0
    while value<n:
        yield value
        value+=1

counter = counter_generator(10)
print(type(counter))

print(next(counter))
print(next(counter))

for value in counter:
    print(value,end=" ")

# generators are great for handling large data sets or can handle infinite data streams.
def generate_odd_numbers():
    num = 1
    while True:
        yield num
        num += 2

odd_numbers = generate_odd_numbers()
print("\nOdd numbers:")
for _ in range(2):
    print(next(odd_numbers), end=" ")
print()
print(next(odd_numbers))

# Generators can be used with other Python features like list comprehensions, map(), and filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_numbers = (num**2 for num in numbers)
print("\nSquared numbers:")
for num in squared_numbers:
    print(num, end=" ")

print("get fibonacci for x with squared:")
print()
print(sum(get_square(fib(10))))


# Generators - generate values on the fly
def generate_numbers():
    for i in range(10**6):  # Large range
        yield i  # Generates one item at a time

gen = generate_numbers()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

def my_numbers():
    for i in range(1,5):
        yield i

print("My numbers:")
for square in get_square(my_numbers()):
    print(square, end=" ")

#List Comprehensions
print("\nList Comprehension:")
numbers = [i for i in range(10)]
print(numbers)

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

print([even_num for even_num in numbers if even_num % 2 == 0])

# Generator expressions
print("\nGenerator expressions:")
squared_numbers = (num**2 for num in numbers)
print(list(squared_numbers),type(squared_numbers))

# Map and Filter
# map - used to apply a function to all items in an iterable
# filter - used to create a new iterable with items that satisfy a condition
print("\nMap and Filter:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print all even numbers
my_evens=list(filter(lambda x: x % 2 == 0, numbers))
print(my_evens,"----even numbers")
# lets square all numbers
squared_nums=(map(lambda x:x**2, numbers))
print(type(squared_nums),tuple(squared_nums),"----squared numbers")


def map_handler(x):
    print("Map handler",x)
    return x**2

def filter_handler(x):
    print("Filter handler",x)
    return x%2!=0

odd_numbers=filter(filter_handler, numbers)
print("My Odd numbers:",list(odd_numbers))

with_square=map(map_handler, numbers)
print()
print("My Squared numbers:",list(with_square))
