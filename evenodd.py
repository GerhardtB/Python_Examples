# example function to test eveness of number i using modulo (%)
def isEven(i):
    if i%2==0 :
        return True
    else:
        return False

#another function example -  square number i
def isquared(i):
    return i*i

n = 4
if(isEven(n)):
    print(str(n)+" is even!")
else:
    print(str(n)+" is odd")
print(str(n)+" squared is "+str(isquared(n)))
