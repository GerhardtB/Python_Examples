import numpy as np

x = np.arange(1,11)
xsquared = x**2
data = np.array([x,xsquared]).T
#print(data)
np.savetxt("xsquared_data.txt",data,fmt="%.3f")

