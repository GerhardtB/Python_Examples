import Tkinter
from Tkconstants import *
import math
from math import *
from time import *
import sys

sine = []
cose = []
for i in range(360):
	sine.append(sin(i*pi/180.0))
	cose.append(cos(i*pi/180.0))

grav = 900.0
cenx = 350
ceny = 350
inship = 1

def togglein(ex):
	global inship, trail,canvas
	inship = not inship
	while(len(trail)>0):
		canvas.delete(trail.pop())
	return

class Ship:
	x = 0.0
	y = 0.0
	dx = 0.0
	dy = 0.0
	theta = 0.0

	def __init__(self,start_x,start_y):
		self.x = start_x
		self.y = start_y
		return

	def move(self):
		di = ((self.x-cenx)**2+(self.y-ceny)**2)
		sgnx = (cenx-self.x)/sqrt((cenx-self.x)**2+(ceny-self.y)**2)
		sgny = (ceny-self.y)/sqrt((cenx-self.x)**2+(ceny-self.y)**2)
		self.accxy(sgnx*grav/di,sgny*grav/di)
		if((self.x-cenx)**2+(self.y-ceny)**2 < 50):
			self.dx = -0.8*self.dx
			self.dy = -0.8*self.dy
		self.x += self.dx
		self.y += self.dy
		if(self.x<5):
			self.x = 2*cenx-10
		elif(self.x>2*cenx-5):
			self.x = 10
		if(self.y<5):
			self.y = 2*ceny-10
		elif(self.y>2*ceny-5):
			self.y = 10
		return

	def left(self,dtheta):
		self.theta -= dtheta
		if(abs(self.theta)<= 360):
			self.theta = self.theta%360
		if(self.theta<0):
			self.theta = 360+self.theta
		return

	def right(self,dtheta):
		self.theta += dtheta
		if(abs(self.theta)<= 360):
			self.theta = self.theta%360
		if(self.theta<0):
			self.theta = 360+self.theta
		return

	def acc(self,dv):
		self.dx = self.dx + cose[int(self.theta)]
		self.dy = self.dy + sine[int(self.theta)]
		if((self.dx*self.dx)+(self.dy*self.dy)> 225):
			self.dx = self.dx - cose[int(self.theta)]
			self.dy = self.dy - sine[int(self.theta)]
		return

	def accxy(self,ddx,ddy):
		self.dx = self.dx+ddx
		self.dy = self.dy+ddy
		if((self.dx*self.dx)+(self.dy*self.dy)> 225):
			self.dx = self.dx - ddx
			self.dy = self.dy - ddy
		return

def left(n):
	ship.left(5)
	return

def right(n):
	ship.right(5)
	return

def acc(n):
	ship.acc(1)
	return

def drawship(c):
	global cenx, ceny,inship
	a = []
	if(inship):
		if((abs(ship.x-cenx)<cenx)and(abs(ship.y-ceny)<ceny)):
			a.append(c.create_oval(2*cenx-ship.x-5,2*ceny-ship.y-5,
				2*cenx-ship.x+5,2*ceny-ship.y+5,fill = "orange"))
		a.append(c.create_line(
			cenx-5*cos(ship.theta*pi/180),
			ceny-5*sin(ship.theta*pi/180),
			cenx+5*cos(ship.theta*pi/180),
			ceny+5*sin(ship.theta*pi/180),fill = "green"))
		a.append(c.create_line(cenx-10*sin(ship.theta*pi/180),
			ceny+10*cos(ship.theta*pi/180),
			cenx+5*cos(ship.theta*pi/180),
			ceny+5*sin(ship.theta*pi/180),fill = "green"))
		a.append(c.create_line(cenx+10*sin(ship.theta*pi/180),
			ceny-10*cos(ship.theta*pi/180),
			cenx+5*cos(ship.theta*pi/180),
			ceny+5*sin(ship.theta*pi/180),fill = "green"))
		a.append(c.create_oval(430,430,470,470,outline = "blue"))
		dist = sqrt((ship.x-cenx)*(ship.x-cenx)+(ship.y-ceny)*(ship.y-ceny))
		a.append(c.create_line(
			450,450,
			450+(cenx-ship.x)*20/dist,450+(ceny-ship.y)*20/dist,
			fill = "green"))
		a.append(c.create_oval(448,448,452,452,outline = "maroon",fill = "magenta"))
		a.append(c.create_text(451,481,text = str(round(dist,3)),fill = "green"))
		a.append(c.create_text(450,480,text = str(round(dist,3)),fill = "#117711"))
	else:
		a.append(c.create_line(
			ship.x-5*cos(ship.theta*pi/180),
			ship.y-5*sin(ship.theta*pi/180),
			ship.x+5*cos(ship.theta*pi/180),
			ship.y+5*sin(ship.theta*pi/180),fill = "green"))
		a.append(c.create_line(ship.x-10*sin(ship.theta*pi/180),
			ship.y+10*cos(ship.theta*pi/180),
			ship.x+5*cos(ship.theta*pi/180),
			ship.y+5*sin(ship.theta*pi/180),fill = "green"))
		a.append(c.create_line(ship.x+10*sin(ship.theta*pi/180),
			ship.y-10*cos(ship.theta*pi/180),
			ship.x+5*cos(ship.theta*pi/180),
			ship.y+5*sin(ship.theta*pi/180),fill = "green"))
		a.append(c.create_oval(cenx-10,ceny-10,cenx+10,ceny+10,fill="orange"))
		trail.append(c.create_oval(ship.x-1,ship.y-1,ship.x+1,ship.y+1,
			fill="#eecc22",outline="#ffee22"));
		if(len(trail)>300):
			p = trail[0];
			c.delete(p)
			del(trail[0])
	c.update()
	while(len(a)>0):
		pp = a.pop();
		c.delete(pp)
	return

trail = []
ship = Ship(100,100)
tk = Tkinter.Tk()
frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
canvas = Tkinter.Canvas(frame, width = 700,height = 700,background = "black")
canvas.pack(fill = BOTH,expand=1)

tk.bind("<Left>",left)
tk.bind("<Right>",right)
tk.bind("<Up>",acc)
tk.bind("<Down>",togglein)

while(1):
	try:
		ship.move()
		drawship(canvas)
		sleep(0.02)
	except Tkinter.TclError:
		sys.exit(0)
tk.mainloop()
