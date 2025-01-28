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

for i in range(1,5):
    print(i)

c=[1,2,3,4]
for item in c:
    print(item*55)
d=[item for item in c]
print("Dictionary",d)
import time 


result=[item for i in range(10)]
print(result)
result=[item for item in range(100001)]
start_time = time.time()
print(10000 in result)
end_time = time.time()
print("Time taken to check 5 in list: ", end_time - start_time)

result=set(item for item in range(100001))
start_time = time.time()
print(10000 in result)
end_time = time.time()
print("Time taken to check 5 in set: ", end_time - start_time)

import sys
# ram in gb 
print("Python version", sys.version)

# extend 
list1=[1,2,3,4]
list2=["a","b","c"]

list1.extend(list2)
print("Extended list1:",list1)

# insert
list1.insert(0,"z")
# insert at the end
list1.insert(len(list1),"y")
print("Inserted list1:",list1)

# remove
list1.append("z")
print("Removing list1:",list1)
list1.remove("z")
print("Removed 'z' from list1:",list1)


# count
print("Count of 'a' in list1:",list1.count("a"))
print("Len of 'a' in list1:",len(list1))


# reverse
list1.reverse()
print("Reversed list1:",list1)

# sort
list1=[str(item) for i in list1]
list1.sort()
print("Sorted list1:",list1)

# index

try:
    print("Index of 'b' in list1:", list1.index("b"))
except Exception as e:
    print("Error:", str(e))


# join
print("Joined list1:", ",".join(list1))     

# slicing
print("Sliced list1:", list1[0:3])

# list comprehension
print("List Comprehension:", [i for i in range(10) if i%2==0])

# removing the items from the list 
list1=[1,2,3,4,5]
del list1[0]
print("List after removing first item:", list1)

list1.pop(0)
print("List after popping first item:", list1)

list1.remove(5)
print("List after removing 5:", list1)
# pop(index) - it will rm the item based on index
# remove(value) - it will remove the item based on value else it will throw ValueError
# clear() - it will clear the list or rm all items from the list and list will have empty 
# copy() - it will return the shallow copy of the list
# count(value) - it will return the count of the value in the list
# extend(iterable) - it will extend the list with the iterable items

print("List before the cleaning up:", list1)
list1.clear()
print("List after the cleaning up:", list1)
list1=[1,2,3,4,5]
clist1=list1.copy();
print("List after copying:", clist1)
# is they the same in terms of memory
print("Is list1 and clist1 the same?", list1 == clist1)
print("Is list2 and clist2 the same?", clist1 is list1)
clist1.append("Hello World")
print("List after appending 'Hello World' to clist1:", clist1,"list1\n",list1)


# looping over the list
# 1. 
for i in list1:
    print(i,end=" ")
# 2
for i in range(len(list1)):
    print(list1[i],end=" ")

# 3
list_len=len(list1)
i=list_len-1
print()
while i>=0 :
    print(list1[list_len-i-1],end=" ")
    i-=1

print("\n----------------------------------------------------------------")
# 4
[print(item,end=" ") for item in list1]
(print(item,end=" ") for item in list1)



fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'I am {index+1} and I love {fruits[index]}')

# sorting the list 
list1=[2,33,4,5,6,7,8,9,1]
list1.sort()
print("Sorted list:",list1)
# in reverse order or in decreasing order
list1.sort(reverse=True)
print("Reversed list:",list1)

# sorting the list based on length of the strings
list1=['apple', 'banana', 'cherry', 'date', 'elderberry']
def MyStringFunc(e):
      print("🚀 ~ e:", e)
      return len(e)

list1.sort(key=MyStringFunc)
print("List sorted by length:",list1)

list1=['apple', 'Banana', 'cherry', 'Date', 'elderberry']
list1.sort(key=lambda x : x.lower())
print("List sorted",list1)

# copying the list
list1=['apple', 'Banana', 'cherry', 'Date', 'elderberry']
l1Copy=list1.copy()
l2Copy=list(list1);
l3Copy=list1
l4Copy=list[:];

print("Copied list:",l1Copy)
print("Is list1 and l3Copy sorted the same?",list1 is l3Copy)
print("Is list1 and l4Copy sorted the same?",list1 is l4Copy)
print("Is list1 and l2Copy sorted the same?",list1 is l2Copy)
print("Is list1 and l1Copy the same?",list1 is l1Copy)


#  Join Lists
list1=['apple', 'banana', 'cherry']
list2=['date', 'elderberry']

list1.extend(list2)
print("Extended list:",list1)

list1=['apple', 'banana', 'cherry']
list2=['date', 'elderberry']
list1=list1+list2
print("Concatenated list:",list1)

list1=[1,2,3]
list2=[4,5,6]

for i in list2:
    list1.append(i)
print("Appended list:",list1)
