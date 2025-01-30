import json

# JSON data
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data)
print(type(python_dict),python_dict)
# print the formatted JSON data
print(json.dumps(python_dict, indent=4,sort_keys=True)) 

# converting Python dictionary to JSON string
json_string = json.dumps(python_dict)
print(type(json_string), json_string)

# Accessing dictionary items
print("Accessing Dictionary Items:","--"*5)
print("python_dict['name']:",python_dict['name'])
print("python_dict['age']:",python_dict['age'])
print("python_dict['city']:",python_dict['city'])

# Adding new key-value pair to dictionary
python_dict['country']='USA'
print("After adding new item:",python_dict)

# Updating existing key-value pair in dictionary
python_dict['age']+=1
print("After updating item:",python_dict)

# Deleting key-value pair from dictionary
del python_dict['country']
print("After deleting item:",python_dict)

# Merging two dictionaries
dict1 = {'name': 'John', 'age': 30}
dict2 = {'city1': 'New York'}
merged_dict = {**dict1, **dict2}
print("Merged dictionaries:",merged_dict)


# List of dictionaries
list_of_dicts = [
    {'name': 'John', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 35}
]
# Sorting list of dictionaries by age
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
print("Sorted list of dictionaries by age:",sorted_list)
sorted_list = sorted(list_of_dicts, key=lambda x: x['name'])
print("Sorted list of dictionaries by name:",sorted_list)

# Converting list of dictionaries to JSON string
print("List of dictionaries to JSON string representation:","--"*5)
print(list_of_dicts)
print("---"*5)
json_string = json.dumps(list_of_dicts, indent=4, sort_keys=True)
print("JSON string representation of list of dictionaries:",json_string)