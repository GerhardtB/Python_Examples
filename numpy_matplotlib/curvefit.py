import numpy as np
import matplotlib.pyplot as pl

#set up noisy data set based on quadratic
datax = np.arange(0,10,0.5)
datay =(0.8-0.4*np.random.rand(np.size(datax)))*datax**2
# generate fitted polynomial
pfit = np.polyfit(datax,datay,3)
#generate polynomial x-y data
fitx = np.linspace(np.min(datax),np.max(datax),100)
fity = np.polyval(pfit,fitx)
#plot everything
pl.plot(datax,datay,'r.')
pl.plot(fitx,fity,'g-')
pl.legend(["data","polyfit"])
pl.show()
