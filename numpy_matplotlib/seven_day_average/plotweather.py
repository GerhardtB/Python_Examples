import numpy as np
import matplotlib.pyplot as pl

# make a list of the body of the filenames, without the common .csv extension
files=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

#create an empty list to store the data read from files
data = []
# loop over the list of filenames, and use loadtxt to load the data into a numpy array,
#...which gets appended to the data list
for fname in files:
    data.append(np.loadtxt(fname+".csv",delimiter=",",skiprows=1,usecols=(tuple(range(1,5)))))

# set up some empty 2-D numpy arrays to store max, min and average data for each of four data columns over seven days
dailyavg=np.zeros(shape=(7,4))
dailymax=np.zeros(shape=(7,4))
dailymin=np.zeros(shape=(7,4))
# now use nested loops to calculate each minimum, maximum and average for column for each day
for day in range(7):
    for col in range(4):
        dailyavg[day,col]=np.mean(data[day][:,col])
        dailymax[day,col]=np.max(data[day][:,col])
        dailymin[day,col]=np.min(data[day][:,col])

# create a 7-element time array to plot against
days=np.arange(7)
#print out the daily average array
print(dailyavg)
# plot the first column averages as a function of time in the first figure window
pl.figure(1)
pl.plot(np.array(days),dailyavg[:,0],"r-")
# plot the second column averages, maxes and mins as a function of time in the second figure window
pl.figure(2)
pl.plot(np.array(days),dailyavg[:,1],"g-")
pl.plot(np.array(days),dailymin[:,1],"g.")
pl.plot(np.array(days),dailymax[:,1],"g.-")
# plot the third and fourth column averages as a function of time each in its own subplot in the third figure window
pl.figure(3)
pl.subplot(1,2,1)
pl.plot(np.array(days),dailyavg[:,2],"b-")
pl.subplot(1,2,2)
pl.plot(np.array(days),dailyavg[:,3],"y-")
# instruct matplotlib to show us all the figures
pl.show()
