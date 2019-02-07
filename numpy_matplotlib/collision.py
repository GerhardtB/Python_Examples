"""
Example of an animated plot - bouncing balls with inter-ball collisions
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import itertools

fig, ax = plt.subplots()

# boundaries of domain
minx=0
miny=0
maxx=1
maxy=1

n=20 # number of particles

# initialize random starting positions for particles
"""
x = np.random.rand(n)*(maxx-minx)+minx
y = np.random.rand(n)*(maxy-miny)+miny
"""
x = np.random.rand(n+2)*(maxx-minx)+minx
y = np.random.rand(n+2)*(maxy-miny)+miny
x[n]=minx
x[n+1]=maxx
y[n]=miny
y[n+1]=maxy

#initialize uniform particle radii
r = np.ones(n+2)*0.1

# initialize random starting velocities
dx = (np.random.rand(n+2)-0.5)*0.001
dy = (np.random.rand(n+2)-0.5)*0.001
dx[n]=0.0
dx[n+1]=0.0
dy[n]=0.0
dy[n+1]=0.0

gx = 0.0    #gravity field x-component
gy = -0.005  #gravity field y-component

e_wall = 0.65 #coeff of restitution between ball and wall
e_ball = 0.40 #coeff of restitution of ball and ball

line, = ax.plot(x, y,"ko") #create initial plot
"""
colours=np.random.rand(n)
area=[]
for i in range(n):
    area.append(np.pi*r[i]*r[i])
line, = ax.scatter(x, y,s=area,c=colours) #create initial plot
"""

def animate(aaa):
    for i in range(n):

        x[i]+=dx[i]
        y[i]+=dy[i]
        # deal with ball-ball collisions
        """
        for j in range(i+1,n):
            dist=np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            if(dist<(r[i]+r[j])):
                colx=(x[i]-x[j])/dist
                coly=(y[i]-y[j])/dist
                coldx=-(dx[i]-dx[j])*colx
                coldy=-(dy[i]-dy[j])*colx

                dx[i]+=coldx*e_ball
                dy[i]+=coldy*e_ball
                dx[j]-=coldx*e_ball
                dy[j]-=coldy*e_ball
        """

        # deal with wall-ball collisions
        bouncex=True
        if((x[i]<=minx)):
            dx[i]=abs(dx[i])*e_wall
        elif(x[i]>=maxx):
            dx[i]=-abs(dx[i])*e_wall
        else:
            dx[i]+=gx
            bouncex=False
        bouncey=True
        if(y[i]<=miny):
            dy[i]=abs(dy[i])*e_wall
        elif(y[i]>=maxy):
            dy[i]=-abs(dy[i])*e_wall
        else:
            dy[i]+=gy
            bouncey=False
        # deal with ball-ball collisions
        for j in range(i+1,n):
            dist=np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            if(dist<(r[i]+r[j])):
                colx=(x[i]-x[j])/dist
                coly=(y[i]-y[j])/dist
                coldx=-(dx[i]-dx[j])*colx
                coldy=-(dy[i]-dy[j])*colx

                if(not bouncex):
                    dx[i]+=coldx*e_ball
                    dx[j]-=coldx*e_ball
                if(not bouncey):
                    dy[i]+=coldy*e_ball
                    dy[j]-=coldy*e_ball
 
    # update the animation frame
    line.set_xdata(x)
    line.set_ydata(y)
    """
    for l in range(len(colours)):
        line[l].set_xdata(x[l:n:len(colours)])
        line[l].set_ydata(y[l:n:len(colours)])
    """
    return line,

# Init only required for blitting to give a clean slate.
def init():
    #line.set_ydata(np.ma.array(x, mask=True))
    line.set_xdata(np.ma.array(x, mask=True))
    line.set_ydata(np.ma.array(y, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=50, blit=True)
plt.show()

