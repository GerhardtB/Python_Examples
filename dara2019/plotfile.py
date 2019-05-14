import numpy as np
import matplotlib.pyplot as plt

mydata = np.loadtxt("xsquared_data.txt")
x = mydata[:,0]
y = mydata[:,1]
plt.plot(x,y,"g^")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid()
plt.legend(["y = x squared"])
plt.savefig("xsquared_graph.png")
plt.show() #you can comment this out and look at the png image
