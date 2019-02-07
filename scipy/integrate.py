import numpy as np
import scipy.integrate as integrate

def fn(x):
    return np.sin(x)-x*np.cos(x/2.0)-x**2

print(integrate.quad(fn,0,10))
