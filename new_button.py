#Program for creating new Buttons

import pygame
pygame.init()

BLACK = (0, 0, 0)
GREY=(50,50,50)
WHITE = (255, 255, 255)
BLUE=(127,255,212)

WIDTH = 14
HEIGHT = 14
MARGIN = 1

r=int(input('Enter no. of rows: '))
c=int(input('Enter no. of cols: '))
name=input('Enter B_Name: ')
temp=WIDTH+MARGIN
WINDOW_SIZE = [temp*c, temp*r]
winlogo=pygame.image.load(".\winlogo.png")
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("NewButton")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()


m=[]
for n_rows in range(r):
	row_temp=[]
	for n_col in range(c):
		row_temp.append(0)
	m.append(row_temp)

def display():
	screen.fill(GREY)
	for row in range(r):
		for column in range(c):
			color = BLACK
			if m[row][column] == 1:
				color = WHITE
			pygame.draw.rect(screen,color,[(MARGIN + WIDTH)*(column)+MARGIN,(MARGIN + HEIGHT)*(row)+MARGIN,WIDTH,HEIGHT])
	clock.tick(60) 
	pygame.display.flip()

def m_coordinate():
	return pygame.mouse.get_pos()[0] // (WIDTH + MARGIN), pygame.mouse.get_pos()[1] // (HEIGHT + MARGIN)

#Reading the design from the user

running=True
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key== pygame.K_RETURN:
				running=False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				column,row=m_coordinate()
				if row<r:
					m[row][column] = 1
		display()

#Saving the design in a text file

f=open('design\\'+name+'.txt','w')
lines=[]
for i in m:
	line=''
	for j in i:
		if j==0:
			line=line+'.'
		if j==1:
			line=line+'*'
	lines.append(line+'\n')
f.writelines(lines)
f.close()
