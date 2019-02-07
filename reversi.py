import Tkinter
from Tkinter import *
import Tkconstants
from Tkconstants import *
import time
from time import *
import sys

# set up a new board
def newboard():
	aboard = [[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,2,1,0,0,0],
		[0,0,0,1,2,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
	return aboard

def copyboard():
	global board
	a = []
	for row in range(len(board)):
		a.append([])
		for squ in board[row]:
			a[row].append(squ)
	return a

def move(player,row,col,brd):
	captures = 0
	if(player == 1):
		enemy = 2
	else:
		enemy = 1
	if(brd[row][col] == 0):

		#checking downward
		i = row+1
		j = col
		while((i < 7) and (brd[i][j] == enemy)):
			i = i + 1
		if((i != row+1) and (i <= 7) and (brd[i][j] == player)):
			for n in range(row,i):
				brd[n][j] = player
				captures = captures + 1
			brd[row][col] = player

		#checking upwards
		i = row-1
		j = col
		while((i > 0) and (brd[i][j] == enemy)):
			i = i - 1
		if((i != row-1) and (i >= 0) and (brd[i][j] == player)):
			for n in range(i,row):
				brd[n][j] = player
				captures = captures + 1
			brd[row][col] = player

		#checking right
		i = row
		j = col+1
		while((j < 7) and (board[i][j] == enemy)):
			j = j + 1
		if((j != col+1) and (j <= 7) and (board[i][j] == player)):
			for n in range(col,j):
				brd[i][n] = player
				captures = captures + 1
			brd[row][col] = player

		#checking left
		i = row
		j = col-1
		while((j > 0) and (brd[i][j] == enemy)):
			j = j - 1
		if((j != col-1) and (j >= 0) and (brd[i][j] == player)):
			for n in range(j,col):
				brd[i][n] = player
				captures = captures + 1
			brd[row][col] = player

		#checking down&left
		i = row+1
		j = col-1
		while((i < 7) and (j > 0) and (brd[i][j] == enemy)):
			i = i + 1
			j = j - 1
		if((i != row+1) and (i <= 7) and (j >= 0) and (brd[i][j] == player)):
			m = col
			for n in range(row,i):
				brd[n][m] = player
				captures = captures + 1
				m = m - 1
			brd[row][col] = player

		#checking down&right
		i = row+1
		j = col+1
		while((i < 7) and (j < 7) and (brd[i][j] == enemy)):
			i = i + 1
			j = j + 1
		if((i != row+1) and (i <= 7) and (j <= 7) and (brd[i][j] == player)):
			m = col
			for n in range(row,i):
				brd[n][m] = player
				captures = captures + 1
				m = m + 1
			brd[row][col] = player

		#checking up&left
		i = row-1
		j = col-1
		while((i > 0) and (j > 0) and (brd[i][j] == enemy)):
			i = i - 1
			j = j - 1
		if((i != row-1) and (i >= 0) and (j >= 0) and (brd[i][j] == player)):
			m = j
			for n in range(i,row):
				brd[n][m] = player
				captures = captures + 1
				m = m + 1
			brd[row][col] = player

		#checking up&right
		i = row-1
		j = col+1
		while((i > 0) and (j < 7) and (brd[i][j] == enemy)):
			i = i - 1
			j = j + 1
		if((i != row-1) and (i >= 0) and (j <= 7) and (brd[i][j] == player)):
			m = j
			for n in range(i,row):
				brd[n][m] = player
				captures = captures + 1
				m = m - 1
			brd[row][col] = player

	return captures
#find all the possible moves,and the number of captures associated with each move

def test(player,brd):
	moves = []
	if(player == 1):
		enemy = 2
	else:
		enemy = 1

	for row in range(8):
		for col in range(8):
			if(board[row][col] == 0):
				captures = 0
				#checking downward
				i = row+1
				j = col
				while((i < 7) and (brd[i][j] == enemy)):
					i = i + 1
				if((i != row+1) and (i <= 7) and (brd[i][j] == player)):
					for n in range(row,i):
						captures = captures + 1

				#checking upwards
				i = row-1
				j = col
				while((i > 0) and (brd[i][j] == enemy)):
					i = i - 1
				if((i != row-1) and (i >= 0) and (brd[i][j] == player)):
					for n in range(i,row):
						captures = captures + 1

				#checking right
				i = row
				j = col+1
				while((j < 7) and (brd[i][j] == enemy)):
					j = j + 1
				if((j != col+1) and (j <= 7) and (brd[i][j] == player)):
					for n in range(col,j):
						captures = captures + 1

				#checking left
				i = row
				j = col-1
				while((j > 0) and (brd[i][j] == enemy)):
					j = j - 1
				if((j != col-1) and (j >= 0) and (brd[i][j] == player)):
					for n in range(j,col):
						captures = captures + 1

				#checking down&left
				i = row+1
				j = col-1
				while((i < 7) and (j > 0) and (brd[i][j] == enemy)):
					i = i + 1
					j = j - 1
				if((i != row+1) and (i <= 7) and (j > 0) and (brd[i][j] == player)):
					m = col
					for n in range(row,i):
						captures = captures + 1
						m = m - 1

				#checking down&right
				i = row+1
				j = col+1
				while((i < 7) and (j < 7) and (brd[i][j] == enemy)):
					i = i + 1
					j = j + 1
				if((i != row+1) and (i <= 7) and (j <= 7) and (brd[i][j] == player)):
					m = j
					for n in range(row,i):
						captures = captures + 1
						m = m - 1

				#checking up&left
				i = row-1
				j = col-1
				while((i > 0) and (j > 0) and (brd[i][j] == enemy)):
					i = i - 1
					j = j - 1
				if((i != row-1) and (i >= 0) and (j >= 0) and (brd[i][j] == player)):
					m = j
					for n in range(i,row):
						captures = captures + 1
						m = m + 1

				#checking up&right
				i = row-1
				j = col+1
				while((i > 0) and (j < 7) and (brd[i][j] == enemy)):
					i = i - 1
					j = j + 1
				if((i != row-1) and (i >= 0) and (j <= 7) and (brd[i][j] == player)):
					m = j
					for n in range(i,row):
						captures = captures + 1
						m = m - 1
				if(captures > 0):
					moves.append([row,col,captures])
	
	return moves

#check if the game has ended
def check():
	count1 = 0
	count2 = 0
	for i in range(8):
		for j in range(8):
			if(board[i][j] == 1):
				count1 = count1+1
			elif(board[i][j] == 2):
				count2 = count2+1
	if(count1 == 0):
		print("Player 2 wins!")
		a = 1
	elif(count2 == 0):
		print("Player 1 wins!")
		a = 1
	elif(count1+count2 == 64):
		if(count1 > count2):
			a = 1
		elif(count1 < count2):
			a = 2
		else:
			a = 3
	else:
		a = 0
	return a

#translate the user's mouse-action into a move in the game.
def guimove(event):
	global board
	x = event.x/40
	y = event.y/40
	if(move(1,y,x,board)):
		# if player has made a valid move then computer must move, if it can
		repaint()
		sleep(0.1)
		a = test(2,board)
		if(len(a)>0):
			row = a[0][0]
			col = a[0][1]
			maxcaps = 0
			caps = []
			for b in a:
				if(((b[0]==0)and(b[1]==0))or((b[0]==0)and(b[1]==7))or
					((b[0]==7)and(b[1]==7))or((b[0]==7)and(b[1]==0))):
						row = b[0]
						col = b[1]
						break
				else:
					testboard = copyboard() 
					move(2,b[0],b[1],testboard)
					encaps = test(1,board)
					mx = 0
					for d in encaps:
						if(d[2] > mx):
							mx = d[2]
					caps.append(b[2]-mx)

				id = caps.index(max(caps))
				row = a[id][0]
				col = a[id][1]

			move(2,row,col,board)
			showmove(col,row)
		while(not len(test(1,board))and len(test(2,board))):
			a = test(2,board)
			row = a[0][0]
			col = a[0][1]
			maxcaps = -64
			for b in a:
				if(((b[0]==0)and(b[1]==0))or((b[0]==0)and(b[1]==7))or
					((b[0]==7)and(b[1]==7))or((b[0]==7)and(b[1]==0))):
						row = b[0]
						col = b[1]
						break
				if(maxcaps < b[2]):
					maxcaps = b[2]
					row = b[0]
					col = b[1]
			move(2,row,col,board)
			showmove(col,row)
	return

#procedure to make it easier to see the computer's move
def showmove(x,y):
	graphics = []
	graphics.append(canvas.create_oval(x*40+5,y*40+5,x*40+35,y*40+35,fill = "red"))
	canvas.update()
	sleep(0.1)
	graphics.append(canvas.create_oval(x*40+5,y*40+5,x*40+35,y*40+35,fill = "blue",outline = "blue"))
	canvas.update()
	if(not check()):
		while(len(graphics)>0):
			canvas.delete(graphics[len(graphics)-1])
			del(graphics[len(graphics)-1])
	return

def repaint():
	graphics = []
	for i in range(8):
		for j in range(8):
			if(board[i][j] == 0):
				colour = "blue"
			elif(board[i][j] == 1):
				colour = "black"
			elif(board[i][j] == 2):
				colour = "white"
			graphics.append(canvas.create_oval(j*40+10,i*40+10,j*40+30,i*40+30,fill = colour))
	canvas.update()
	if(not check()):
		while(len(graphics)>0):
			canvas.delete(graphics[len(graphics)-1])
			del(graphics[len(graphics)-1])
	return

#----------------------main---------------------
board = newboard()
tk = Tkinter.Tk()
tk.title("Reversi 1.1")
frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
canvas = Tkinter.Canvas(frame, width = 320,height = 320,background = "black")
canvas.pack(fill = BOTH,expand=1)

#bind mouse-clicks to the guimove function
tk.bind("<ButtonPress>",guimove)
canvas.create_rectangle(0,0,320,320,fill = "blue")
try:
	while(check() == 0):
		repaint()
except Tkinter.TclError:
	sys.exit(0)

#repaint the screen one last time to show the last move and display message
repaint()
canvas.create_rectangle(100,140,220,170,outline = "yellow",fill = "blue")
if(check() == 1):
	canvas.create_text(150,150,text = "Player 1 wins!",fill = "yellow")
elif(check() == 2):
	canvas.create_text(150,150,text = "Player 2 wins!",fill = "yellow")
if(check() == 3):
	canvas.create_text(150,150,text = "Game drawn",fill = "yellow")
canvas.update()
tk.mainloop()
