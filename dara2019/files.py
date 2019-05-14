f = open("data.txt","r")
totals = [0,0,0]
for line in f:
    #print(line[:len(line)-1])
    #or:
    row=line[:-1].split()
    for i in range(len(row)):
        totals[i]+=int(row[i])

f.close()
print(totals)


