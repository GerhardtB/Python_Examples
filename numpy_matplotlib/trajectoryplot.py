import matplotlib.pyplot as pl
import numpy as np

data = np.loadtxt("trajectory.csv",delimiter=",")
pl.subplot(2,1,1)
pl.plot(data[:,0],data[:,2],"g-")
pl.xlabel("Time (s)")
pl.ylabel("Height (m)")
pl.subplot(2,1,2)
pl.plot(data[:,1],data[:,2],"r-")
pl.xlabel("Horisontal distance (m)")
pl.ylabel("Height (m)")
pl.show()
