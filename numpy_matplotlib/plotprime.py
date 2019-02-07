from math import *
import numpy as np
import matplotlib.pyplot as pl

def is_prime(x):
    for ii in range(2,int(sqrt(x))+1):
        if(x%ii==0):
            return False
    return True

"""
for jj in range(2,100):
    if(is_prime(jj)):
        print(str(jj)+" is PRIME!")
    else:
        print(str(jj)+" is not prime")
"""
ind = int(input("which prime number? "))
count = 1
num = 3
primes = [2]
numbers = [1]
print("The 1st prime number is: 2")
while(count<ind):
    if(is_prime(num)):
        count =  count + 1
        primes.append(num)
        numbers.append(count)
        #print("The "+str(count)+"th prime number is: "+str(num))
    num = num + 2
pl.plot(primes,numbers,"r")
pl.plot(np.array(primes),np.array(primes)/np.log(np.array(primes)))
pl.show()
