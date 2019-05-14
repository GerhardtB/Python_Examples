total = 0
limit = 10

for i in range(1,limit+1):
    total+=i**2
    print("i="+str(i)+", i squared="+str(i**2)+" total="+str(total))
#    if(total > 250):
#        print("limit of 250 reached")
#        break
print("final total of series: "+str(total))
