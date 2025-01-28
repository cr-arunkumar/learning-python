# tuples- ordered , immutable, allows duplicate elements, and allows multiple elements.
# ordered and unchangeable & allow duplicate values.
# In Python, tuples are written with round brackets.
# creation 
x=(1,2,3,4,5)
y=tuple([1,2,3,4,5])
print(x,y,type(x))
# accessing tuple items
print("Accessing Tuple Items:","--"*5)
print("x[0]:",x[0])
print("x[4]:",x[4])
print("x[-1]:",x[-1])
print("x[-2]:",x[-2])
# slicing tuple items
print("Slicing Tuple Items:","--"*5)
print("x[1:4]:",x[1:4])
print("x[:4]:",x[:4])
print("x[4:]:",x[4:])
print("x[:-1]:",x[:-1])
# updating tuple items - it is not possible
# x[0]=10
# print("x[0]:",x[0])
# x[1:3]=[20,30]
# print("x[1:3]:",x)


# methods on tuples
print("Methods on Tuples:","--"*5)
print("len(x):",len(x))
print("x.count(3):",x.count(3))
print("x.index(3):",x.index(3))
# x.append(6) - can't be used as tuple are the immutable sequence
print("x:",x)

# Check
x=[1,2,3,4,5,5,6]
print("x.count(5):",x.count(5))
print("x.index(5):",x.index(5))
print("5 exist in x",5 in x)
print("-5 exist in x",-5 in x)

thistuple = ("apple", "banana", "cherry")
if "kiwi" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("No, 'apple' is not in the fruits tuple")

# to add items into tuple we need to first convert it into list and then add the items
x=(1,2,3,4,5,6,7,8,9,10)
y=list(x)
y.append(11)
x=tuple(y)
print("x:",x)
y=(111,)
x+=y
print("x:",x)

# deleting the tuple or tuple item 
del x
# print("x:",x) # it will give error as x is not defined

# packing and unpacking
print("----------------unpacking----------------") 
x=(1,2,3,4,5,5,6,6,7,7,8,8,8,9,9,9,9,9,676)
a,b,c,*rest_items=x
print("a:",a)
print("b:",b)
print("c:",c)
print("rest_items:",rest_items,type(rest_items))


# looping 
print("----------------looping----------------") 
x=(1,2,3,4,5,5,6,6,7,7,8,8,8,9,9,9,9,9,676)
for item in x:
  print(item)

i=0
while i<len(x):
    print(x[i],end=" ")
    i+=1
for index,item in enumerate(x):
    print(f"Index:{index} and Item:{item}",end="  ")

print()
for i in range(len(x)):
    print(x[i],end=" ")


# combining or joining two or tuples
print("\n----------------combining----------------") 
x=(1,2,3,4,5)
y=(6,7,8,9,10)
z=x+y
print("z:",z)

print(x*2)