# data types
# 1. string
x="string"
print(type(x))

# 2 Numeric Types:	int, float, complex 
x=10
y=2.5
z=1j
print(type(x),type(y),type(z))

# 3 Sequence Types:	list, tuple, range 
x=[1,2,3] # define the sequence type
y=(1,2,3) # define the tuple
z=range(1,4) 
# another ways - by using the class constructor
x1=list([ 1,2,4,5])
y1=tuple([1,2,4,5]) # tuple are the immutable sequence
my_tuple=(1,2,4,5) 
my_list=[1,2,4,5]
my_list.append(34343);
print(my_list,my_tuple)
print(type(x),type(y),type(z))
print(type(x1),type(y1),type(z))

# 4 Mapping Type:    dict
x={"name":"John", "age":30}
print(type(x))
# using class constructor 
x1=dict([("name","John"), ("age",30)])
print(type(x1))

# 5 Set Types:      set, frozenset
# diff bet set and frozenset
# A set is mutable (can be modified after creation)
# A frozenset is immutable (cannot be modified after creation)
x = {1, 2, 3}  # set
y = frozenset({1, 2, 3})  # frozenset

# Example of set mutability
x.add(4)       # Works fine with set
# y.add(4)     # Would raise AttributeError - frozenset has no add method

x={1,2,3}
y=frozenset({1,2,3})
print(type(x),type(y))

# 6 Boolean Type:    bool
x=True
print(type(x))

# 7 Binary Types:    bytes, bytearray
x=b"Hello"
y=bytearray(x)
print("MY Byte array",y)
print(type(x),type(y))

# 8 None Type:      None
x=None
print(type(x))

# 9 Ellipsis Type:  ...
x=...

# 10 Function Type: def
def my_function():
    pass
print(type(my_function))

# 11 Class Type:    class
class MyClass:
    pass
print(type(MyClass),"My class")

# 12 Instance Type: object
x=MyClass()
print(type(x))

# 13 Type Type:      type
x=type(int)
print(type(x))

# 14 Generator Type: generator
def my_generator():
    yield 1
    yield 2
    yield 3
print(type(my_generator()))

# 15 Module Type:    module
import math
print(type(math))

print("----------------------------------------------------------------")
# 16 Callables Type: callable
x=print
print(type(x))

# 17 Awaitable Type: awaitable
import asyncio
async def my_async_function():
    await asyncio.sleep(41)
    return "Hello"
print(type(my_async_function()))


x = 3+5j
y = 5j
z = -5j

print(type(x),"Complex",x.real)
print(type(y))
print(type(z))
