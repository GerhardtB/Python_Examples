import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as pl

samplerate=0.01
max_t=10

x = np.arange(0,max_t,samplerate)
y = np.sin(x*2*np.pi)+2.5*np.sin(x*3*2*np.pi)+0.8*np.sin(x*7*2*np.pi)+1.2*np.random.ranf(len(x))

freqdom=2*abs(fft(y,n=len(y)))/len(y)
freqrange=np.linspace(0,1/samplerate,len(x))

pl.subplot(2,1,1)
pl.plot(x,y,"b-")
pl.xlabel("Time (sec)")
pl.ylabel("Signal")
pl.subplot(2,1,2)
pl.plot(freqrange[:int(len(x)/2)],freqdom[:int(len(x)/2)],"k-")
pl.xlabel("Frequency (hz)")
pl.ylabel("Energy")
pl.show()
