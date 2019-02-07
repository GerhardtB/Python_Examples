# calculates how many odd numbers must be summed to reach a target
tot = 0
odd = 1
target = 100

while(tot < target):
    tot = tot + odd
    print(str(odd)+" "+str(tot))
    odd = odd + 2
    if(odd>target):
        print("odd number greater than target - aborting loop!")
        break
print("all done")

