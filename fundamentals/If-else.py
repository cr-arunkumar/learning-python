a=103
b=103

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

# using else if statement
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a and b are equal")

print("--------------------------------")
# Short hand 
print("a is greater than b" if a>b else "b is greater than a")
a=900
b=900
print("--------------------------------")
if a>b:print("a is greater than b")
elif a<b:print("b is greater than a")
else:print("a and b are equal")
print("--------------------------------")
# using Ternary Operators, or Conditional Expressions.
x=100
y=100
print("x is greater than y" if x > y else "y is greater than x" if x < y else "x and y are equal")
# "a>b" if a>b else "a<b" if a<b else "a==b"

print("--------------------------------")
# nested if statement
x=10
y=5
if x>y:
    print("x is greater than y")
    if x%2==0:
        print("x is even")
    else:
        print("x is odd")
print("--------------------------------")
a=12
b=4
if a>5 and a<20:
    print("a is between 5 and 20")
else:
    print("a is not between 5 and 20")

# we can use or , not ,and logical operators in the if else statements

## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["ahmedabad","Surat","mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

my_city = str(input("Enter Your city name: "))

if my_city.lower() in india:
    print(f"Your city {my_city} belongs to india")
elif my_city.lower() in pakistan:
    print(f"Your city {my_city} belongs to pakistan")
elif my_city.lower() in bangladesh:
    print(f"Your city {my_city} belongs to bangladesh")
else:
    print("i won't able to tell about your city , which contry its belongs to")
