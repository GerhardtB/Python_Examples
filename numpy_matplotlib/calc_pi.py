import math
import random
import matplotlib.pylab as pl
# calculate pi using monte-carlo approach using basic python

#number of points to use
n_pts=100000

# counter for number of points within circle
in_tot=0

# loop executes for each point
for i in range(n_pts):
    # generate random x and y-coordinates for each point, between 0 and 1
    x=random.uniform(0,1) #alternatively: x=np.random.rand()
    y=random.uniform(0,1)
    # check whether points are within unit distance from origin (0,0)
    if(x*x+y*y<1):
        #if so, update the counter
        in_tot+=1
        # plot all points within the quarter-circle in blue
        pl.plot(x,y,"bo")
    else:
        # plot all points outside the quarter-circle in red
        pl.plot(x,y,"ro")
        #to see the running estimate: print("Iteration "+str(i+1)+" PI est: "+str(4*in_tot/(i+1)))

#print out the final estimate, after calculating the fraction of total points within the quarter circle,
# and multiplying by 4 for a full circle:
print("final pi est: "+str(4*in_tot/n_pts))
pl.show()
