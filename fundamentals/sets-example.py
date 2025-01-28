# sets - A set is a collection which is unordered, unchangeable*, and unindexed.
# In Python sets are written with curly brackets.
# creation
x = {"apple", "banana", "cherry"}
print(x)

# access items in set
print("Accessing Set Items:","--"*5)
for i in x:
    print(i,end=" ")
i=0;
print("Access using while loop:","--"*5)
while i<len(x):
    print(x.pop(),end=" ")
    i+=1

my_bool_set={0,1,2,4,True,False}
print(my_bool_set,end=" ")
# 0 and False inside the set are considered as 0 or same if both are present in the set
# 1 and True inside the set are considered as 1 or same if both are present in the set 
print("Length of my_bool_set:",len(my_bool_set))
print("0 in my_bool_set:",0 in my_bool_set)
print("199 in my_bool_set:",199 in my_bool_set)
print("type of my_bool_set:",type(my_bool_set))
# we can create a set using set() constructor 
x1=set([1,2,3,4,5])
print(x1)
# Sets are the unchangeable but we can remove items or add the new items 
x1.remove(1);
print(x1)
x1.add(11)
print(x1)
x1.pop() # this removes the top element from the set
print(x1)
print("------"*9)
# Accessing the set items
# we can't access the set items directly using indexes 
# we can loop over the items

for i in x1:
    print(i,end=" ")
print()

# Add the new items
x1={1,2,3,"apple","banana","cherry"}
print(x1)
# x1.add([1,2,3]) # it will give error as list is not hashable
x.add(3)
print(x1)
# --------------------------------
# update the set items 
x1.update([5,6,7,"x","y","z"])
print(x1)
# Remove Item
# x1.remove(1)
x.discard(1)
print("after removing 1:",x1)
# main Difference between remove and discard is that remove() method throws error when item is not present
# while discard() method not.
# pop() method always remove the item. - it will rm item randomly from the set

# clear() method - removes all items from the set but it will not delete set
x1.clear()
print(x1) 
x1.update(["appple"])
print(x1)
# del x1
# print("after deleting x1:",x1) # it will give error as x1 is deleted
print()
print("--------------------------------","Join sets","--------------------------------")
print()
# join two sets
x1={1,2,3,4,5,6,7,8,9,10}
x2={112,122}
# merge or join 
x1=x1.union(x2)
print(x1)

# union() and '|' operator have same effect 
x2.add("Hello world")
x1=x1 | x2
print(x1)

# intersection() and '&' operator have same effect
# intersection operator used to take the duplicates from the two sets
x1={1,2,3,4,5,6,7,8,9,10}
x2={7,8,10,11,123,23,24,25,26,27}
print(x1.intersection(x2),"have same effect when we use & operator",x1 & x2)

# joins multiple sets 
x1={1,2,3,4,5,6,7,8,9,10}
x2={11,12,13,14,15}
x3={16,17,18,19,20}
x4={21,22,23,24,25}
x5=x1.union(x2,x3,x4)
print(x5)

# union() operator allows us to join a set with other data types like list,tuple
x1={1,2,3,4,5,6,7,8,9,10}
x2=[11,12,13,14,15]
x3=(16,17,18,19,20)
x4={"Hello","World"}
x5=x1.union(x2,x3,x4)
print(x5)

#  The  | operator only allows you to join sets with sets.

# update() method modify the original set not return new set 
x1={1,2,3,4,5,6,7,8,9,10}
x2={1,11,12,13,14,15}
x1.update(x2)
print(x1)

# & allow intersection only with set while intersection() allows with other data types.


# intersection_update() - metod allow to do intersection and instead of returning new set it will 
# update/modify the original set so we will get set the duplicates items 
x1={1,2,3,4,5,6,7,8,9,10}
x2={1,11,12,13,14,15}   
x1.intersection_update(x2)
print(x1)

# difference() and '-' operator have same effect
# difference() or '-' operator return a new set that will contain only 
# the items from the first set that are not present in the other set.
x1={1,2,3,4,13,12,11}
x2={11,12,13,14,15,1}
print(x1.difference(x2),"have same effect when we use - operator",x1 - x2)
# '-' operator only works with sets while difference operator works with other data types as well 
# symmetric_difference - it only keep the items that are not present both sets 
# it keeps all items that are not present both sets
# '^' operator only works with sets and have same effect as SymmetricDifference method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print("symmetric_difference",set3)


x1={1,2,3}
x1_copy=x1.copy()
x1.clear()
print("x1 after clear:",x1)
print("x1 is x1_copy",x1 is x1_copy)
print("x1_copy:",x1_copy)
