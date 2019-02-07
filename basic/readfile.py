f = open("data2.csv","r")
for line in f:
    #print(line[:-1])
    #if(len(line)>1):
    try:
        datastr=line[:-1].split(sep=",")
        rowtot=0
        for dat in datastr:
            rowtot = rowtot + float(dat)
        print("row total = "+str(rowtot))
    except:
        pass
    # add an if-statement to deal with empty lines
