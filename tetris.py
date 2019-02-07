# Tetris
import pygame
from pygame.locals import *
from random import *
from sys import *

red = pygame.color.Color("#ff0000")
orange = pygame.color.Color("#ff8800")
yellow = pygame.color.Color("#ffff00")
green = pygame.color.Color("#00ff00")
blue = pygame.color.Color("#0000ff")
purple = pygame.color.Color("#ff00ff")
white = pygame.color.Color("#ffffff")
grey = pygame.color.Color("#555555")
black = pygame.color.Color("#000000")

colours = [black,red,orange,yellow,green,blue,purple,white]

lose = 0
width = 10
height = 20
board = []
for i in range(width):
	board.append([])
	for j in range(height):
		board[i].append(0)

class shape:
	def __init__(self, type):
		self.type = type
		self.x = width/2
		self.y = 0
		self.blocks = []
		# line
		if(self.type==1):
			self.blocks = [[0,-1],[0,0],[0,1],[0,2]]
		# block
		elif(self.type==2):
			self.blocks = [[0,1],[0,2],[1,1],[1,2]]
		# left-L
		elif(self.type==3):
			self.blocks = [[0,-1],[0,0],[0,1],[1,1]]
		# right-L
		elif(self.type==4):
			self.blocks = [[0,-1],[0,0],[0,1],[-1,1]]
		# T
		elif(self.type==5):
			self.blocks = [[-1,0],[0,0],[1,0],[0,1]]
		# Z
		elif(self.type==6):
			self.blocks = [[-1,0],[0,0],[0,1],[1,1]]
		# S
		elif(self.type==7):
			self.blocks = [[1,0],[0,0],[0,1],[-1,1]]
		return

	def down(self):
		global lose
		for bl in self.blocks:
			bx = bl[0]+self.x
			by = bl[1]+self.y
			if((by==height-2)or(board[bx][by+1])):
				for b in self.blocks:
					board[b[0]+self.x][b[1]+self.y]=1
				return 1
		self.y += 1
		return 0

	def left(self):
		for bl in self.blocks:
			bx = bl[0]+self.x
			by = bl[1]+self.y
			if((bx<1)or(board[bx-1][by])):
				return
		self.x -= 1
		return

	def right(self):
		for bl in self.blocks:
			bx = bl[0]+self.x
			by = bl[1]+self.y
			if((bx>=width-1)or(board[bx+1][by])):
				return
		self.x += 1
		return

	def cwrot(self):
		if((self.x>0)and(self.x<width-1)):
			for bl in self.blocks:
				tx = bl[0]
				ty = bl[1]
				bl[0] = ty
				bl[1] = -tx
		return

	def ccwrot(self):
		if((self.x>0)and(self.x<width-1)):
			for bl in self.blocks:
				tx = bl[0]
				ty = bl[1]
				bl[0] = -ty
				bl[1] = tx
		return

a = shape(5)
def left():
	a.left()
	return

def right():
	a.right()
	return

def down():
	global a
	if(a.down()):
		if(a.y<2):
			lose = 1
		else:
			a = shape(int(random()*6+1))
	return

def cwrot():
	a.cwrot()
	return

def ccwrot(k):
	a.ccwrot()
	return

pygame.init()

screen = pygame.display.set_mode((300,500))
screen.fill((0,0,0))
clock = pygame.time.Clock()
score = 0
lines = 0
font = pygame.font.Font(None, 20)
delay = 400
step = 4
lvl = 1
count = 0
while(not lose):
	pygame.event.pump()
	keystate = pygame.key.get_pressed()
	if(keystate[K_LEFT]):
		left()
	if(keystate[K_RIGHT]):
		right()
	if(keystate[K_UP]):
		cwrot()
	if(keystate[K_DOWN]):
		down()
	if((keystate[K_ESCAPE])or(keystate[K_q])):
		lose=1
	delrows = []
	delrows = []
	screen.fill((0,0,0))
	screen.lock()
	pygame.draw.rect(screen,white,
		[10,10,20*width,20*(height-1)],1)
	for y in range(height):
		blcount = 0
		for x in range(width):
			if(board[x][y]==1):
				pygame.draw.rect(screen,grey,
					[10+x*20,10+20*y,20,20],0)
				blcount += 1
		if(blcount==width):
			delrows.append(y)
	
	if(lvl*10<lines+len(delrows)):
		delay -= 50
		lvl += 1
	lines += len(delrows)
	score += 20*len(delrows)*len(delrows)
	while(len(delrows)>0):
		y = delrows.pop()
		for x in range(width):
			del(board[x][y])
			board[x].insert(0,0)

	for bl in a.blocks:
		pygame.draw.rect(screen,colours[a.type],
			[10+a.x*20+bl[0]*20,10+20*a.y+bl[1]*20+i*step/20,20,20],0)
	screen.unlock()
	if(count==step):
		count = 0
		if(a.down()):
			if(a.y<2):
				lose = 1
			else:
				a = shape(int(random()*6+1))
	else:
		count += 1
	text = font.render("Level: "+str(lvl), 1,(150,150,10))
       	textpos = text.get_rect()
       	textpos.centerx = 250
       	textpos.centery = 270
       	screen.blit(text, textpos)
	text = font.render("Lines: "+str(lines), 1,(150,150,10))
       	textpos = text.get_rect()
       	textpos.centerx = 250
       	textpos.centery = 300
       	screen.blit(text, textpos)
	text = font.render("Score: "+str(score), 1,(150,150,10))
       	textpos = text.get_rect()
       	textpos.centerx = 250
       	textpos.centery = 330
       	screen.blit(text, textpos)
	pygame.display.flip()
	pygame.time.wait(delay/step)
