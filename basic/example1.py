#!/usr/bin/env python3
# read in the user's name
name=input("Please enter your name: ")
#print a greeting to the user
print("Hello, "+name)
#ask the user by name for one number
num1=float(input(name+", please enter a number: "))
#ask for a second number
num2=float(input(name+", please enter another number: "))
#print the sum of the numbers
print(name+", the sum of "+str(num1)+" and "+str(num2)+" is "+str(num1+num2))
