#GAME OF LIFE
import os
import copy
import pygame
import module_button
#Display
#Colors
BLACK = (0, 0, 0)
GREY=(50,50,50)
WHITE = (255, 255, 255)
BLUE=(127,255,212)
#Box Dimensions
WIDTH = 9
HEIGHT = 9
MARGIN = 1
#Button Dimensions
B_MARGIN=2
B_WIDTH=60
B_HEIGHT=18

#To read the design names present in the designs folder
names = []
# r=root, d=directories, f = files
for r, d, f in os.walk('design\\'):
	for file in f:
		if '.txt' in file:
			names.append(file.split('.')[0])

button={}        
b_color=[]
T=0
pygame.init()
WINDOW_SIZE = [501, 542]
#Loading the assets
logo=pygame.image.load(".\logo.png")
start=pygame.image.load(".\start.png")
info=pygame.image.load(".\info.png")
winlogo=pygame.image.load(".\winlogo.png")
cover=pygame.image.load(".\cover.png")

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GameOfLife")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()

#Fonts
font1 = pygame.font.SysFont('freesansbold.ttf', 20)
font2 = pygame.font.SysFont('freesansbold.ttf', 16)
#FUNCTIONS


infinite_grid=False
fps=60
#m is the main matrix
m=[]
#new_m is the temporary matrix
new_m=[]
#extra_size is not visible to user
extra_size=10
grid_size=50
n=grid_size+2*extra_size

#Function to get the position of the box over which mouse is hovering
def m_coordinate():
	return pygame.mouse.get_pos()[0] // (WIDTH + MARGIN)+extra_size, pygame.mouse.get_pos()[1] // (HEIGHT + MARGIN)

#Function to render text
def textfunc(text,textcolour, coordinate):
	textsurface=font2.render(text, True, textcolour)
	textrect=textsurface.get_rect()
	textrect.center=(coordinate[0]+B_WIDTH/2,coordinate[1]+B_HEIGHT/2)
	screen.blit(textsurface,textrect)
	
#Function to reset the grid
def reset_game():
	global fps, new_m, m, BLACK, WHITE, infinite_grid, b_color,T
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	fps=60
	T=0
	infinite_grid=False
	m=[]
	new_m=[]
	b_color=[WHITE]*len(names)
	for n_rows in range(n):
		row_temp=[]
		for n_col in range(n):
			row_temp.append(0)
		m.append(row_temp)   

	new_m=copy.deepcopy(m)
	screen.fill(WHITE)
	screen.blit(cover,(0,200))
	pygame.display.flip()
	pygame.time.delay(1000)
	
reset_game()
#Function to display the grid
def display(l):
	#l refers to the matrix
	global fps, n, m, button, button_grid, button_info, b_color, T
	screen.fill(GREY)
	screen.blit(logo,(0,0))
	
	for row in range(7,grid_size):
		for column in range(extra_size,grid_size+extra_size):
			color = BLACK
			if l[row][column] == 1:
				color = WHITE
			elif l[row][column] == 2:
				color = BLUE
			pygame.draw.rect(screen,color,[(MARGIN + WIDTH)*(column-extra_size)+MARGIN,(MARGIN + HEIGHT)*row+MARGIN,WIDTH,HEIGHT])
	
	#fps bar
	text = font1.render("fps", True, (0,0,0))
	fps_bar_back=pygame.rect.Rect(434,53,64,10)
	fps_bar=pygame.rect.Rect(436,55,fps,6)
	pygame.draw.rect(screen, (0,0,0) ,fps_bar_back)
	pygame.draw.rect(screen, BLUE ,fps_bar)
	screen.blit(text,(411,52))
	#Manual input of position
	textT = font1.render("T:"+str(T), True, (0,0,0))
	screen.blit(textT,(360,52))
	for i in range(len(names)):
		if i<=7:
			coord=((B_MARGIN + B_WIDTH)* i + B_MARGIN*1,500 + B_MARGIN*1)
		else:
			coord=((B_MARGIN + B_WIDTH)* (i-8) + B_MARGIN*1,500 + B_HEIGHT + B_MARGIN*2)
		button[names[i]]=pygame.rect.Rect(coord[0],coord[1],B_WIDTH,B_HEIGHT)
		pygame.draw.rect(screen, b_color[i] ,button[names[i]])
		textfunc(names[i],BLACK,coord)
	
	#Grid_Button
	coord=((B_MARGIN + B_WIDTH)* 7 + B_MARGIN*1,520 + B_MARGIN*1)
	button_grid=pygame.rect.Rect(coord[0],coord[1],B_WIDTH,B_HEIGHT)
	pygame.draw.rect(screen, WHITE ,button_grid)
	textfunc('GRID',BLACK,coord)
	
	#Info_Button
	coord=(485,40)
	button_info=pygame.rect.Rect(coord[0],coord[1],10,10)
	pygame.draw.rect(screen, (0,0,0) ,button_info)
	textsurface=font2.render('i', True, (255,255,255))
	textrect=textsurface.get_rect()
	textrect.center=(coord[0]+4,coord[1]+6)
	screen.blit(textsurface,textrect)

	if fps<=0.5:
		fps+=1
	if fps>60:
		fps=60
	clock.tick(fps) 
	pygame.display.flip()
	b_color=[WHITE]*len(names)

#Function to check the neighbours of a cell
#xth row and yth column
def check_n(x,y):
	global m
	global new_m
	sum_n=0
	try:
		sum_n=m[x-1][y]+m[(x+1)%n][y]+m[x][(y+1)%n]+m[x][y-1]+m[x-1][y-1]+m[x-1][(y+1)%n]+m[(x+1)%n][y-1]+m[(x+1)%n][(y+1)%n]
	except:
		pass
	if sum_n<2:
		new_m[x][y]=0
	elif sum_n==2 and m[x][y]:
		pass
	elif sum_n==3:
		new_m[x][y]=1
	else:
		new_m[x][y]=0  
#Function to simulate infinite grid
def infinite_func():
	global new_m
	
	if sum(new_m[grid_size-1]+new_m[grid_size-2])==0 and infinite_grid:
		for i in range(extra_size*2):
			new_m[grid_size+i]=[0]*n
	if sum(new_m[7]+new_m[8])==0 and infinite_grid:
		for i in range(7):
			new_m[i]=[0]*n
	for i in range(7,7+grid_size):
		if new_m[i][extra_size]==0 and new_m[i][extra_size+1]==0:
			pass
		else:
			break
	else:
		for i in range(7,7+grid_size):
			for j in range(extra_size):
				new_m[i][j]=0
	for i in range(7,7+grid_size):
		if new_m[i][grid_size+extra_size-2]==0 and new_m[i][grid_size+extra_size-1]==0:
			pass
		else:
			break
	else:
		for i in range(7,7+grid_size):
			for j in range(grid_size+extra_size,n):
				new_m[i][j]=0

#Function which when given a tuple of coordinates assigns a suitable value to the corresponding postions of matrix
def preset(tupl,l,n=1):
	for i in tupl:
		l[i[0]][i[1]]=n

#Function which handles the event between clicking on a button and clicking on the grid		
def button_click(desn,file_name):
	global m, new_m,inv
	hover=True
	inv=[False,False,False]
	#inverse=(x_inv, y_inv, rot_inv)
	while hover:
		for event in pygame.event.get():
			new_m=copy.deepcopy(m)
			x,y=m_coordinate()
			
			try:
				#new_m is a temporary matrix
				preset(desn(file_name,x,y,inverse=inv),new_m,2)
				display(new_m)
			except:
				pass
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					x,y=m_coordinate()
					preset(desn(file_name,x,y,inverse=inv),m)
					inv=[False,False, False]
					hover=False
			elif event.type== pygame.KEYDOWN:
					if event.key== pygame.K_ESCAPE:
						hover=False
						break  
					if event.key== pygame.K_RIGHT:
						inv[2]= not(inv[2])
					if event.key== pygame.K_LEFT:
						inv[0]= not(inv[0])    
					if event.key== pygame.K_UP:
						inv[1]= False
					if event.key== pygame.K_DOWN:
						inv[1]= True

#main function
def main():    
	global m, fps, n,new_m, WIDTH, HEIGHT, MARGIN, infinite_grid, WHITE, BLACK,T
	display(m)

	#Allowing the user to fill in the grid
	running=True
	while running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key== pygame.K_RETURN:
					running=False
				if event.key== pygame.K_q:
					infinite_grid=True
					pass
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					column,row=m_coordinate()
					if row<grid_size:
						m[row][column] = 1
					
					elif button_grid.collidepoint(event.pos):
						MARGIN=1-MARGIN
						if WIDTH==9:
							WIDTH+=1
							HEIGHT+=1
						else:
							WIDTH-=1
							HEIGHT-=1
					if button_info.collidepoint(event.pos):
						screen.fill(WHITE)
						screen.blit(info,(0,0))
						pygame.display.flip()
						pygame.time.delay(3000)

					for i in range(len(names)):
						if button[names[i]].collidepoint(event.pos):
							button_click(module_button.new_button,names[i])
			display(m)
			for i in range(len(names)):
						if button[names[i]].collidepoint(pygame.mouse.get_pos()):
							b_color[i]=BLUE
						else:
							b_color[i]=WHITE
					
	#Running the GOL Algorithm on the given grid		 
	running=True
	fps=5
	while running:
		T+=1
		new_m=copy.deepcopy(m)
		for i in range(n):
			if 1 not in m[i-1]+m[i]+m[(i+1)%n]:
					continue
			for j in range(n):
				check_n(i,j)
		if infinite_grid:
			infinite_func()
		m=new_m
		display(m)
		
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_RIGHT]:
			fps+=0.5
		if keystate[pygame.K_LEFT]:
			fps-=0.5

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					fps=30
				elif event.key == pygame.K_DOWN:
					fps=5
				elif event.key == pygame.K_ESCAPE:
					reset_game()
					main()
				elif event.key == pygame.K_c:
					if BLACK[0]>WHITE[0]:
						change=5
					else:
						change=-5
					old_fps=fps
					fps=60
					for i in range (51):
						BLACK = ((BLACK[0]-change),)*3
						WHITE = ((WHITE[0]+change),)*3
						display(m)
					fps=old_fps
					
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					if button_grid.collidepoint(event.pos):
						MARGIN=1-MARGIN
						if WIDTH==9:
							WIDTH+=1
							HEIGHT+=1
						else:
							WIDTH-=1
							HEIGHT-=1
					elif button_info.collidepoint(event.pos):
						screen.fill(WHITE)
						screen.blit(info,(0,0))
						pygame.display.flip()
						pygame.time.delay(3000)
					
				
#Intro screen
screen.fill(WHITE)
screen.blit(start,(0,0))
pygame.time.delay(2600)
pygame.display.flip()

running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key== pygame.K_RETURN:
				running=False
		elif event.type==pygame.QUIT:
			running=False
			quit()   
#Running the main function
main()

