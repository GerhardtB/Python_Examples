f = open("squares.txt","w")
for i in range(1,11):
    f.write(str(i**2)+"\n")
f.close()
