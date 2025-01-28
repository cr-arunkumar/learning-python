# similar to map() 
my_dict={
    "name":"John",
    "age":25,
    "city":"New York"
}
# use dict() constructor
new_dict=dict(my_dict.items())
new_dict=dict(name="arun",age="John",city="New York")
print(new_dict)

print(len(new_dict))
print("my_dict is new_dict",my_dict is new_dict)
# using list comprehension
# new_dict=[(k,v) for k,v in my_dict.items()]
# print(new_dict)
# dict are the ordered 
# Dictionaries are changeable, meaning that we can change, add or remove items
# duplicates items are not allowed
# we can get the length of dictionary
print(len(new_dict))
print(type(my_dict))
#  Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# accessing items 
print("Accessing Dictionary Items:","--"*5)
print("my_dict['name']:",my_dict['name'])
print("my_dict['age']:",my_dict['age'])
print("my_dict['city']:",my_dict['city'])
# if key is not present then it will raise keyError 
print("USING GET METHOD",my_dict.get("city"))
# it will not raise the keyError else it will return the None value
print("USING get METHOD",my_dict.get("citye")) 
# to avoid the KeyError we can use get() method with a default value
print("USING GET METHOD with default value",my_dict.get("citye","Unknown"))

# get all keys of the dictionary
print("Keys of my_dict:",type(my_dict.keys()),my_dict.keys())
# get all values of the dictionary
print("Values of my_dict:",type(my_dict.values()),my_dict.values())

# add new item/update to the dictionary
new_dict["country"]="USA"
print("After adding new item:",new_dict)
new_dict["city"]="Ahmedabad"    
print("After updating item:",new_dict)

print("city is present in the dictionary", "city" in my_dict)

# updae()
my_dict.update({"country":"India","city":"Ahmedabad"})
print("After updating item using update():",my_dict)

# deleting the items from the dictionary 
del my_dict["country"]
print("After deleting item:",my_dict)
my_dict.pop("city")
print("After popping item:",my_dict)
my_dict.clear()
print("After clearing the dictionary:",my_dict)
# del my_dict
# print("my_dict is deleted",my_dict) # raise error  "my_dict is not defined"

# looping over dictionary
print("----------------Looping over dictionary----------------") 
my_dict={
    "name":"John",
    "age":25,
    "city":"New York",
    "country":"USA",
    "hobbies":["reading","painting"]
}
for key, value in my_dict.items():
    print(key,":",value)

# looping over values.

# loop over values and keys together
for value in my_dict.values():
    print(value)

# loop over keys
for key in my_dict.keys():
    print(key)


print()
print("--------","copying the values","----------")
# copying the values of dictionary
my_dict_copy=my_dict.copy()
my_dict_copy1=my_dict;
print("my_dict_copy:",my_dict_copy)
print("my_dict is my_dict_copy?",my_dict is my_dict_copy)
# print("my_dict_copy1:",my_dict_copy1 is my_dict) # True 

my_dict_copy2=dict(my_dict)
print("my_dict_copy2:",my_dict_copy2 is my_dict) # False

# Nested dictionary
my_dict_nested={
    "name":"John",
    "age":25,
    "city":"New York",
    "country":"USA",
    "hobbies":["reading","painting"],
    "address":{
        "street":"123 Main St",
        "city":"New York",
        "state":"NY"
    }
}
print("my_dict_nested['address']['city']:",my_dict_nested['address']['city'])

# looping over nested dict - similar to normal one
print("----------------Looping over nested dictionary----------------") 
for key, value in my_dict_nested.items():
    print(key,":",value)

for value in my_dict_nested.values():
    print(value)

for x , my_obj in my_dict_nested.items():
     print("key",x)
     if isinstance(my_obj,dict):
          for key1, value1 in my_obj.items():
               print("key1",key1)
               print("value1",value1)
