# write a program that requests a size,
# then prints a triangle of stars of that size ("*")
# for instance a size 3 triangle:
# *
# **
# ***
# **
# *

trisize = int(input("Please enter a triangle size: "))

#now use for loops and string multiplication (eg 4*"*"="****")
# to draw the triangle
for i in range(1,trisize+1):
    print(i*"*")
for j in range(trisize-1,0,-1):
    print(j*"*")






