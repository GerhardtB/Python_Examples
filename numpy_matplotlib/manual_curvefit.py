import numpy as np
import matplotlib.pyplot as pl

#set up noisy data set based on quadratic
datax = np.arange(0,5,1)
datay = datax**4+datax**3-datax**2+datax-5.0

porder = 5

# generate fitted polynomial manually using numpy's matrix manipulation tools
xpolymat = np.ones((porder,np.size(datax)))
for ii in range(np.size(datax)):
    xpolymat[ii,...] = datax**ii

# solve the system of linear equations to calculate the curve-fit polynomial constants
pfit = -1*np.linalg.inv(np.transpose(xpolymat).dot(xpolymat)).dot(np.transpose(xpolymat)).dot(np.transpose(datay))


#generate polynomial x-y data
fitx = np.linspace(np.min(datax),np.max(datax),100)
fity = np.polyval(pfit,fitx)

#plot everything
pl.plot(datax,datay,'r.')
pl.plot(fitx,fity,'g-')
pl.legend(["data","polyfit"])
pl.show()
