# Write a program to calculate the first N prime numbers-
# numbers which have only themselves and one as factors.

# Write a function to test if a number is a prime or not.
# If it is a prime, return True. If not, return False
# Use the sieve of Erastosthenes (or more a sophisticated method)
# check remainder of num divided by each number between 2 and sqrt(num).
# If its zero, you've found a factor and it's not prime - return False
# Otherwise, if no factors are found, it is Prime -return True
from math import sqrt

def isPrime(num):
    if(num<2):
        return False
    else:
        for i in range(2,int(sqrt(num)+1)):
            if num%i==0:
                return False
        return True

#find the first 343 primes
primesfound=0
j = 2
while(primesfound<343):
    if(isPrime(j)):
        print(j)
        primesfound = primesfound + 1
    j = j + 1

#if(isPrime(344)):
#    print("344 is a prime!")
#else:
#    print("344 is NOT a prime!")  
# MAIN PROGRAM
# write a loop to calculate prime numbers until you have found N primes,
# using the isPrime function which you wrote
