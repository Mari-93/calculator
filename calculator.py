#############
# This script is created for calculator operations
# Author:
# Created at:
# Last modified at:
###############


from math import pow, sqrt, pi

def add(a,b): # Format
    return a+b

def sub(a,b): # always add function document.
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b):
    return pow(a,b)

def square(a):
    return sqrt(a)

def circle(r):
    return pi*(r**2)


print("choose any operation from the below list:") # Why there are 2 print statement, You can achieve the same in one print statemnt itself.
print(''' 1. Add
2. Sub
3. Multiply
4. Divide
5. Find the power of
6. Find the square root of
7. Find the Area of a circle''')
while True:
    n = int(input("Enter a choice: "))

    if n==1:
        print("Enter two numbers")
        a=int(input("A: ")) # Getting input is repeated, could you create a function for getting input from user. 
        b=int(input("B: "))
        print(add(a,b))
        break

    elif n==2:
        print("Enter two numbers")
        a=int(input("A: "))
        b=int(input("B: "))
        print(sub(a,b))
        break

    elif n==3:
        print("Enter two numbers")
        a=int(input("A: "))
        b=int(input("B: "))
        print(multiply(a,b))
        break

    elif n==4:
        print("Enter two numbers")
        a=int(input("A: "))
        b=int(input("B: "))
        print(divide(a,b))
        break

    elif n==5:
        a=int(input("Enter a number: "))
        b=int(input("Choose the power to find: "))
        print(int(power(a,b)))
        break

    elif n==6:
        a=int(input("Enter the number to find the square root : "))
        print(square(a))
        break

    elif n==7:
        a=int(input("Enter the radius: "))
        print(circle(a))
        break

    else:
        print("choose only from the option")



# There are lot of things to change in calculator program. But some of them are advanced concepts. We will learn step by step. 