import random

fout = open("random.csv","w")
rows = 10
cols = 4
for i in range(rows):
    for j in range(cols):
        num = random.uniform(0,1)
        fout.write(str(num)+",")
    fout.write("\n")
fout.close()
