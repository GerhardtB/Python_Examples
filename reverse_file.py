#program to reverse each line in a text file and write to a new file
#open input file for reading
infile = open("glug.txt","r")
#open output file for writing
outfile = open("glug_reversed.txt","w")
#loop over each line in the input file
for line in infile:
    #loop over each character in the line read from the file, in reverse
    for char in reversed(line):
        # we don't want to print the last newline at the beginning of the reversed line
        if(char!= "\n"):
            outfile.write(char)
    #put the newline at the end of each line
    outfile.write("\n")
    # A more concise way, using string slicing and no loops: outfile.write(line[len(line)-2::-1]+"\n")
#close both input and output file
infile.close()
outfile.close()
