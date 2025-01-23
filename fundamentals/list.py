# list - lists are mutable and used to store multiple items in a single variable.
x=[1,2,3,4,5,6,7,8,9]
print(x,type(x))
# also we can create a list by using the list constructor
x1=list([1,2,3,4,5])
print(x1,type(x1))

# accessing list items 
print("Accessing List Items:","--"*5)
print("x[0]:",x[0])
print("x[4]:",x[4])
print("x[-1]:",x[-1])
print("x[-2]:",x[-2])

# slicing list items
print("Slicing List Items:","--"*5)
print("x[1:4]:",x[1:4])
print("x[:4]:",x[:4])
print("x[4:]:",x[4:])
print("x[:-1]:",x[:-1])

# updating list items
print(f"before updating x:{x}")
print("Updating List Items:","--"*5)
x[0]=10
print("x[0]:",x[0])
x[1:3]=[20,30]
print("x[1:3]:",x)
x[2:5]=[40,50,60]
print("x[2:5]:",x) 

# deleting list items
result=x.remove(40) #Raises ValueError if the value is not present
print(f"after removing x from x:{x}: {result}")
del x[1]
print(f"after deleting x[1] from x:{x}")

# list methods'
print(f"Original x:{x}")
x.append(70)
print(f"after appending 70 to x:{x}")
x.insert(2,55)
print(f"after inserting 55 at index 2 to x:{x}")
x.extend([80,90])
print(f"after extending x with [80,90] to x:{x}")
print(f"popped item from x:{x.pop()}") # it removes the last item from the list
print(f"popped item from x at index 2: {x.pop(2)}") # it removes the item at given index
# if index is not found then it will throw IndexError exception


# list comprehension
print("List Comprehension:","--"*5)
x=[i for i in range(10)]
print("x:",x)
y=[i**2 for i in range(10)]
print("y:",y)
z=[i for i in range(10) if i%2==0]
print("z:",z)

# nested list comprehension
print("Nested List Comprehension:","--"*5)
x=[[i for i in range(3)] for j in range(8)]
print("x:",x)

# sorting list
x=[i for i in range(10)]
x.sort(reverse=True)
print("x after sorting:",x)

# joining list items
print("Joining List Items:","--"*5)
x=["a","b","c"]
y=["d","e","f"]
z=x+y
print("z:",z)
z=" ".join(x+y)
print("z:",z)

# checking if item is in list
print("Checking if item is in list:","--"*5)
x=[1,2,3,4,5]
print(5 in x)
print(6 in x)
print(x.index(3)) # it returns the index of the item



# list comprehension with multiple conditions
print("List Comprehension with multiple conditions:","--"*5)
x=[i for i in range(1,10) if i%2==0 and i%3==0]
print("x:",x)

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0,4554);
mylist=[str(x) for x in mylist] 
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)

# separate by type and then perform sort 
x=x.append([i for i in range(10)])
numbers = [x for x in mylist if isinstance(x, (int, float))]
strings = [x for x in mylist if isinstance(x, str)]
numbers.sort()
strings.sort()
sorted_list = numbers + strings
print("Sorted after separating types:", sorted_list)
