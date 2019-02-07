""" Write a program which simulates the flight of a cannonball.
 The cannonball is fired at a 45 degree angle, at an initial speed of 50m/s. Ignore air-resistance, but take gravity into account. Write to file the height and ground-distance travelled (x and y-coordinates) of the cannonball every 0.1 seconds.
 Stop the simulation when the cannonball hits the ground (height = 0"""
 
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


x = 0.0 # distance from cannon
y = 0.0 # height above ground
dt = 10.0 #time-step size
#theta = math.pi/4 #45 degrees in radians
G = 6.67e-11# gravitational accelleration
m1 = 1000 #satelite mass
m2 = 6.0e24 # mass of the earth

def newvel(x,y,vx,vy):
    """
    ax = -x/math.sqrt(x*x+y*y)*G*m1*m2/(x*x+y*y)
    ay = -y/math.sqrt(x*x+y*y)*G*m1*m2/(x*x+y*y)
    """
    ax = -x/math.sqrt(x*x+y*y)*G*m2/(x*x+y*y)
    ay = -y/math.sqrt(x*x+y*y)*G*m2/(x*x+y*y)
    return [vx+dt*ax,vy+dt*ay]

def newposition(oldx,oldy,vx,vy):
    newx = oldx+vx*dt
    newy = oldy+vy*dt
    return [newx,newy]

t = 0
"""
x = 400000.0
y = 0.0
vx=  0.0
vy = 1000000.0
"""
x = 0.0
y = 9000000
vx = 7400.0
vy = 0.0
timedata= []

fig, axis = plt.subplots()
axis.autoscale_on=True
#line1, = axis.plot(x, y,"r*")
line1, = axis.plot([0,2.0e7,2.0e7,-2.0e7,-2.0e7], [0,2.0e7,2.0e7,-2.0e7,-2.0e7],"r*")
#line2, = axis.plot(x, y,"y")
deg = np.arange(361)
earthx=6500e3*np.sin(deg*np.pi/180.0)
earthy=6500e3*np.cos(deg*np.pi/180.0)
#lineearth, = axis.plot([0,1.0e10,1.0e10,-1.0e10,-1.0e10], [0,1.0e10,1.0e10,-1.0e10,-1.0e10],"b")
lineearth, = axis.plot(earthx,earthy,"b")

def animate(i):
    global x,y,vx,vy,t,timedata
    lineearth.set_xdata(earthx)  # update the data
    lineearth.set_ydata(earthy)  # update the data
    timedata.append(t)
    [vx,vy]=newvel(x,y,vx,vy)
    [x,y]=newposition(x,y,vx,vy)
    t+=dt
    line1.set_xdata(x)  # update the data
    line1.set_ydata(y)  # update the data
    return line1,


# Init only required for blitting to give a clean slate.
def init():
    line1.set_xdata(np.ma.array(x, mask=True))
    line1.set_ydata(np.ma.array(y, mask=True))
    return line1,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 20000), init_func=init,
                              interval=20, blit=True)
plt.show()
