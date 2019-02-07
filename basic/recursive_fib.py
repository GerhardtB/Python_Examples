# fibonacci series function to demonstrate function recursion
def fib(n):
    # as before, hardcode 0 and 1 as the first two values in the series
    if (n==0):
        return 0
    elif(n==1):
        return 1
    #otherwise, use recursion and the definition of fibonacci:
    #the sum of the previous two numbers in the series
    else:
        return fib(n-1)+fib(n-2)

# we can't print the number within the function, so we have to loop through the sequence of numbers and print
for i in range(20):
    print(str(i)+": "+str(fib(i)))
