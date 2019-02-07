"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

minx=0
miny=0
maxx=1
maxy=1
n=10
x = np.random.rand(n)
y = np.random.rand(n)
dx = (np.random.rand(n)-0.5)*0.01
dy = (np.random.rand(n)-0.5)*0.01
line, = ax.plot(x, y,"k*")


def animate(i):
    #line.set_ydata(np.sin(x + i/10.0))  # update the data
    for i in range(n):
        x[i]+=dx[i]
        if((x[i]<minx)or(x[i]>maxx)):
            dx[i]*=-1.0
        y[i]+=dy[i]
        if((y[i]<miny)or(y[i]>maxy)):
            dy[i]*=-1.0
    line.set_xdata(x)  # update the data
    line.set_ydata(y)  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    #line.set_ydata(np.ma.array(x, mask=True))
    line.set_xdata(np.ma.array(x, mask=True))
    line.set_ydata(np.ma.array(y, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)
plt.show()

