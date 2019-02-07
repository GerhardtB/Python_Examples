import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10)
y1 = x**2
y2 = x**4
plt.subplot(1,2,1)
plt.plot(x,y1,"r*")
plt.subplot(1,2,2)
plt.plot(x,y2,"g-")
plt.savefig("graph.png")
plt.show()
