""" Write a program which simulates the flight of a cannonball.
 The cannonball is fired at a 45 degree angle, at an initial speed of 50m/s. Ignore air-resistance, but take gravity into account. Write to file the height and ground-distance travelled (x and y-coordinates) of the cannonball every 0.1 seconds.
 Stop the simulation when the cannonball hits the ground (height = 0"""
 
import math
x = 0.0 # distance from cannon
y = 0.0 # height above ground
dt = 0.01 #time-step size
theta = math.pi/4 #45 degrees in radians
g = -9.81 # gravitational accelleration
u = 50.0 #initial velocity

def newposition(oldx,oldy,vx,vy):
    newx = oldx+vx*dt
    newy = oldy+vy*dt
    return [newx,newy]

outfile = open("trajectory.csv","w")
t = 0
vx = u*math.cos(theta)
vy = u*math.sin(theta)
while(y>=0):
    outfile.write(str(t)+","+str(x)+","+str(y)+"\n")
    [x,y]=newposition(x,y,vx,vy)
    vy += dt*g
    t+=dt

outfile.close()
