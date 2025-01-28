# for loop

for i in range(10):
    print(i,end=" ")
print()
i=0
while i<10:
    print(i,end=" ")
    i+=1
print()
for i in range(1430):
    if i==99:
        break
    if i%2==0:
        print("even",i)
    else:
        print("odd",i)

fruits=["mango","banana","orange","peach"]
for fruit in fruits:
    print(fruit)

for x in range(6):
  print(x)

# nested loops
for x in range(4):
      for y in range(3):
         print(x,y)

print("----------------------------------------------------------------")
for x in range(100):
    pass
print("above loop has been runs 100 times")

'''
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads
'''
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for item in result:
    if item=="heads":
        count+=1
print("Number of heads:",count)
print()

# Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    if i%2==0:
        continue
    print(i**2)

print()

# Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
months_dict={
    0:"JAN",
    1:"FEB",
    2:"MAR",
    3:"APR",
    4:"MAY",
    5:"JUN",
    6:"JUL",
    7:"AUG",
    8:"SEP",
    9:"OCT",
    10:"NOV",
    11:"DEC"
}
'''
Write a program that asks you to enter an expense amount and program should
tell you in which month that expense occurred. If expense is not found then it should print that as well.
'''
input_amount =int(input("Please enter an amount:"))

if input_amount in expense_list:
    index = expense_list.index(input_amount)
    print(f"Expense of {input_amount} occurred in {months_dict[index]}")

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message


for i in range(5):
    print(f"Distance covered: {i+1} km")
    response = input("Are you tired? (yes/no): ")
    if response == "yes":
        print("You didn't finish the race")
        break
    if i==4:
     print("Congratulations! You finished the race")
    else:
      print("You didn't finish the race")

'''
*
**
***
****
*****
'''
for i in range(5):
    print("*"*i)