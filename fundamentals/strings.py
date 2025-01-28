str="My String,i don't have"
print(str)

str='Hello, i don"t have"'
print(str)
print("*"*60)
str="""My String,
i don't "" ''' have"""
print(str)

str='''Hello, """ i don't have"'''
print(str)

str="My String, i don't have\nline break"
print("My Str",str)
# adding spaces or tabs we used \t
str="My String, i don't have\tone line space"
print("My Str with one space ",str)

# Accessing and manipulating strings
str="He.llo.Wo.rl.d!"
print(str[0]) #return the fist postion character
print(str[6:]) #returns the characters from 6 postion
print(str[::5]) #returns the characters from start to end with size of 5 .
print(str[::2]) # same it returns the string with size of 2 characters
print(str[::-1]) # it return the whole string from end to start.
print(str.upper()) # it converts all the characters to uppercase
print(str.lower()) # it converts all the characters to lowercase
print(str.replace("World","Python")) # it replaces the given string with another string
print(str.split(".")) # it splits the string into a list of words
print(str.find("o")) # it returns the first occurrence of the character in the string
print(str.count("o")) # it returns the count of the character in the string
print(str.startswith("He")) # it returns True if the string starts with the given string
print(str.endswith("!")) # it returns True if the string ends with the given string
print(str.strip()) # it removes the leading and trailing spaces in the string
print(str.lstrip()) # it removes the leading spaces in the string
print(str.rstrip()) # it removes the trailing spaces in the string
str="hello123 world!"
print(str.isalnum()) # it returns True if the string contains only alphanumeric characters

print("---"*20)
# Formatting strings
name="arun"
last_name="kumar"
age=30
print("My name is {} and I am {} years old.".format(name,age))
print(f"My name is {name} and I am {age} years old.")
print(f"my full name is {name}{last_name}.")
print(f"my full name is {name.upper()} {last_name.upper()}.")
print(f"my full name is {name.capitalize()} {last_name.capitalize()}.")


print("---"*10,"looping on strings","---"*10)
str=f"my name is {name.capitalize()} {last_name.capitalize()}"
print(str)
# 1. iterate using for loop
for char in str:
    print(char, end="")  
print()
# 2. iterate using while loop
print("using while loop")
i=0
strLen=len(str)

while i<strLen:
    print(str[i].upper(),end="")
    i+=1
print()
# check a phrase contains a string or not 
phrase="My name is ARUN and I am 30 years old."
search_string="Arun"
if search_string.lower() in phrase.lower():
    print(f"{search_string} found in the phrase.")
else:
    print(f"{search_string} not found in the phrase.")
# phrase+='age '
print("age" not in phrase.lower())

b = "Hello, World!"
print(b[:5])
# reverse the first 5 characters
print(b[:5][::-1])  

#String Concatenation
str1="Hello"
str2="World"
print(str1+str2)

str=22
# print(str+str2) # this will throw an error as string and integer can't be concatenated
str3=344.55454
print(str+str3)
str="43.33"
str4="World"
print(str+str4)

str1=23.4
str2="World"
# print(str1+str2) # this will throw an error as string and float can't be concatenated
str2=33
print(str1+str2)


# Escape Character
str="Hello, \"My Name is Arun\" World!"
print(str)
# adding backSlashes
str="Hello, \\My Name is Arun\\ World!"
print(str)
# adding double backslashes
str="Hello, \\\\My Name is Arun\\\\ World!"
str="Hello from python"
print(str.center(42))
print(str.rjust(42))

