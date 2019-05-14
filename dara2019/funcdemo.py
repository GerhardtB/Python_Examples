def add(a,b):
    c = a+b
    return c

def myindex(alist,searchthing):
    ind=0
    for thing in alist:
        if thing==searchthing:
            print("found it at "+str(ind))
            return ind
        ind+=1
    print("it wasn't in the list")
    return

#print(add(2,3))

#testlist = ["a","b","c","d","e"]
#testind = myindex(testlist,"q")
#print(testind)
