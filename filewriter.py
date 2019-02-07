#short program to write some text to a python file
# a string variable containing some text
randomword="blob"
# open the file "pythonwritten.txt" for writing
f = open("pythonwritten.txt","w")
for i in range(100):
    # write each number from 0 to 99 and its square, as well as the text to a line in the file
    f.write(str(i)+","+str(i**2)+","+randomword+"\n")
# close the file once all lines are written
f.close()
