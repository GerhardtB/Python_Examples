import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("xydata.csv",delimiter=",",skiprows=1)
x=data[:,0]
y=data[:,1]

plt.plot(x,y,"g^")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("xyplot.png")
plt.show()
