x=(1,2,3,4,5,6,7)
my_itr=iter(x)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))



class MyIterator:
    def __init__(self):
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
            if self.index <10:
              self.index += 1
              return self.index
            else:
                  raise StopIteration

my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator()
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
try:
     print(next(my_iterator))
     print(next(my_iterator))

except StopIteration:
     print("Iteration complete.")


# Scoping in python 
print("-----------Scoping------------")

y=120
def outer_function():
    def inner_function():
        global y  # accessing global variable inside inner function
        y = 15
        print("Inner function:", y)
    inner_function()
    print("Outer function:", y)
print("Global variable:", y)
outer_function()
print("Global variable:", y)

# nonlocal keyword - used to access variables in the outer function from within an inner function
# or make them to belongs to outer function
print("-----------Nonlocal------------")
def outer_function():
    x = 10
    def inner_function():
        nonlocal x 
        x = 20
    inner_function()
    return x
print("Value",outer_function())