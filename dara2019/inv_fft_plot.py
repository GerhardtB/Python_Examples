import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

data=np.loadtxt("fft_experiment_data.csv",delimiter=",",skiprows=3)
#print(data)
freq=data[:,0]
realdat=data[:,1]
imagdat=data[:,2]
fftdata=realdat+1j*imagdat
#print(fftdata)
timedata=ifft(fftdata)
xdata = np.arange(len(timedata))

plt.subplot(2,1,1)
plt.plot(xdata,timedata,"b-")
plt.xlabel("Time (sec)")
plt.ylabel("Signal")
plt.subplot(2,1,2)
plt.plot(freq,np.abs(fftdata),"k-")
plt.xlabel("Frequency (hz)")
plt.ylabel("Energy")
plt.show()
