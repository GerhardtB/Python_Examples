# Define function to calculate fibonacci sequence.
# The function takes one argument - the number of terms in the sequence
def fib(terms):
    # the first two terms of the series are 0 and 1
    a = 0
    b = 1
    # create a counter variable
    n = 0
    while(n<terms-1):
        tmp = b # use a temporary variable to store the old value of b
        b = a + b
        a = tmp
        #pythonic alternative: a,b = b,a+b
        n+=1 #increment counter variable
        print(n+1,a)
    return b

# test the function to 50 terms
fib(50)
