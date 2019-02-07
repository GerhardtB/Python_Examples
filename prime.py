from math import *

#function to check for primeness of number
# is_prime takes one parameter- the number to test (x)
# returns true if x is prime, and false if not
#uses the sieve of eratosthenes method.
def is_prime(x):
    # check all numbers between the first prime (2) and the square root of the number
    for ii in range(2,int(sqrt(x))+1):
        # if the number has even one factor (ie there  is no remainder)...
        if(x%ii==0):
            # then that is one factor too many - it is not prime, so exit the loop and return false
            return False
    return True
    # otherwise if no factors are found and the loop completes, return true

#ask the user how many prime numbers are wanted
ind = int(input("which prime number? "))
#initialize counter variable
count = 1
#start with the second prime number (3)
num = 3
# hard-code message for first prime number
print("The 1st prime number is: 2")
# keep checking for prime numbers until we've found enough
while(count<ind):
    if(is_prime(num)):
        #increment the counter whenever we find a prime
        count =  count + 1
        print("The "+str(count)+"th prime number is: "+str(num))
    #add 2 onto the number to test each time (the only even prime is 2)
    num = num + 2

#correct the value of num after the last iteration, in case we need it
num = num - 2
