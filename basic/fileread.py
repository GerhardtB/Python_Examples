#open a text file "glug.txt" for reading
f = open("glug.txt","r")
# loop through the lines in the text file using a for loop
for line in f:
    # print out each line
    print(line)
    #print the number of characters in each line - including the final newline char
    print("line length in chars: "+str(len(line)))
#once the file has been completely read by the loop, close it again.
f.close()
