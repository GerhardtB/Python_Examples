import numpy as np
import matplotlib.pyplot as pl

#load dirty dataset into a numpy array called data, using numpy.genfromtxt
data = np.genfromtxt("Land_and_Ocean_complete.txt",comments='%',filling_values='NaN')
#print out first column of data
print(np.array2string(data[0]))
print(np.shape(data))
#calculate the year as a floating point value, based on elapsed months
year=((data[...,0]-1850)*12+data[...,1])/12.0+1850
#plot the third,fourth and eighth data column
anomaly = data[...,2]
uncertainty = data[...,3]
glug = data[...,8]
pl.plot(year,anomaly,'r')
pl.plot(year,uncertainty,'g')
pl.plot(year,glug,'k')
# Set up the legend for the three data lines plotted
pl.legend(["Anomaly","Uncertainty","Glug"])
# set the label of the x-axis
pl.xlabel("years")
# set the label of the y-axis, using latex notation
pl.ylabel("${}^o$ C")
# show the plot
pl.show()
