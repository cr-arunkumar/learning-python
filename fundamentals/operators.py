# 1 Arithmetic operator
x=10
y=5
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Division:",x/y)
print("Modulus:",x%y)
print("Exponentiation:",x**y)
x=55.555
print("division:",x/y)
print("Floor Division:",x//y) # it will not consider the floors value - {value}.0

# 2 Assignment operator
print("Assignment Operator:","--"*5)
x=10
x+=5
print("x+=5:",x)
x-=5
print("x-=5:",x)
x*=5
print("x*=5:",x)    


# 3 Comparison operator
x=4
y=8
print("Comparison Operator:","--"*5)
print("x==y:",x==y)
print("x!=y:",x!=y)
print("x<y:",x<y)
print("x<=y:",x<=y)
print("x>y:",x>y)
print("x>=y:",x>=y)

# 4 Logical operator
print("Logical Operator:","--"*5)
x=True
y=False
print("x and y:",x and y)
print("x or y:",x or y)
print("not x:",not x)
print("not y:",not y)

# 5 Bitwise operator
print("Bitwise Operator:","--"*5)
x=10
y=5
# display the value in binary format
print("Binary of x:",bin(x)[2:])
print("Binary of y:",bin(y)[2:])
# bitwise and operator
print("x & y:",x & y)
# bitwise or operator
print("x | y:",x | y)
# bitwise xor operator
print("x ^ y:",x ^ y)
# bitwise left shift operator
print("x << 1:",x << 1)
# bitwise right shift operator
print("x >> 1:",x >> 1)

# 6 Membership operator
print("Membership Operator:","--"*5)
x=[1,2,3,4,5]
y=6
print("y in x:",y in x)
print("y not in x:",y not in x)
str="i am not a robot"
print("o not in str:",'o' not in str)
print("robot" in  str)

# 7 Identity operator - 
# it is used to compare the objects, not if they are equal,
#  but if they are actually the same object, with the same memory location
print("Identity Operator:","--"*5)
x=10
y=10
print("x is y:",x is y)
print("x is not y:",x is not y)
x=[1,2,3,4]
y=x
print("x is y:",x is y)
y=[1,2,3,4]
print("x is y:",x is y)
print("x is not y:",x is not y)


# 8 Ternary operator
# very helpful for writing the conditional statements in a single line 
print("Ternary Operator:","--"*5)
x=10
y=5
print("x if y>5 else y:",x if y>5 else y)
print("x is greater than 5" if x>y else "x is less than 5")

# 9 Operator precedence
# it is used to determine the order of the operations in an expression
print("Operator Precedence:","--"*5)
x=10
y=5
z=3
print("x+y*z:",x+y*z) # here, it performs multiplication before addition
print("(x+y)*z:",(x+y)*z) # here it performs addition before multiplication

# Unary plus, unary minus, and bitwise NOT
print("Unary Plus, Unary Minus, Bitwise NOT:","--"*5)
x=10
print("+x:",+x)  # it will give the positive value of x 
print("-x:",-x) # it will give the negative value of x
x=10
print("~x:",~x) # it will give the bitwise not of x
# how to calculate bitwise not of
# 10 = 0000 1010
# ~10 = 1111 0101 = -11
