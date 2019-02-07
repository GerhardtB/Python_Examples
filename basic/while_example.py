#short program showing how while-loops work
#The scenario is that an event is planned for the first five people alphabetically in a list.
#However, someone named Edward intends to gatecrash and added his name dishonestly...

#list of names
names=["Fred","Bob","Simon","Robert","Dave","Edward","William"]
#rearrange names in alphabetical order
names.sort()
# counter variable for while-loop
count = 0
# continue re-running the code below, until count reaches or exceeds five
while(count<5):
    # check whether the current name in the list is Not Edward
    if(names[count]!="Edward"):
        #if so, print the invitation
        print(names[count]+" is invited.")
        #add one to the counter, to reflect the number of invitees
        count = count + 1
    #however, if the person IS Edward...
    else:
        #print a message to show him the door
        print("Edward is not welcome here!")
        # remove his name from the list, and don't update count
        del(names[count])

