# an example demonstrating while-loops, continue and break statements
# create a counter variable and set to 0
count = 0
# the loop will continue to execute all statements within until count >= 20
while count < 20:
    # print out the value of count, to see what happens to it
    print(count)
    if count == 5:
        count+=1
        #continue aborts the present step in the loop,
        #returning straight to the test at the top of the loop,
        #and ignoring the remainder of the loop code block
        continue
    elif count == 9:
        #break immediately exits the loop, whether or not the loop condition is True or False
        break
    else:
        #increment the counter manually, unlike a for-loop over an integer range
        count+=1
