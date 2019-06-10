#GAME OF LIFE
import copy
#import os
import pygame

#Display
BLACK = (0, 0, 0)
GREY=(50,50,50)
WHITE = (255, 255, 255)
WIDTH = 9
HEIGHT = 9
MARGIN = 1

pygame.init()
WINDOW_SIZE = [501, 501]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GameOfLife")
clock = pygame.time.Clock()
logo=pygame.image.load(".\logo.png")
fps=4


def display():
    global fps
    screen.fill(GREY)
    screen.blit(logo,(0,0))
    
    for row in range(7,n):
        for column in range(n):
            color = BLACK
            if m[row][column] == 1:
                color = WHITE
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
    if fps<=0.5:
        fps+=1
    clock.tick(fps) 
    pygame.display.flip()


m=[]
newm=[]
n=50
for n_rows in range(n):
    row_temp=[]
    for n_col in range(n):
        row_temp.append(0)
    m.append(row_temp)

display()

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RETURN:
                running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            m[row][column] = 1
            display()
        elif event.type==pygame.QUIT:
            running=False
            quit()

def check_n(x,y):
    global m
    global new_m
    sum_n=0
    try:
        sum_n=m[x-1][y]+m[(x+1)%n][y]+m[x][(y+1)%n]+m[x][y-1]+m[x-1][y-1]+m[x-1][(y+1)%n]+m[(x+1)%n][y-1]+m[(x+1)%n][(y+1)%n]
    except:
        sum_n=0

    if sum_n<2:
        new_m[x][y]=0
    elif sum_n==2 and m[x][y]:
        pass
    elif sum_n==3:
        new_m[x][y]=1
    else:
        new_m[x][y]=0

running=True
while running:
    new_m=copy.deepcopy(m)
    for i in range(n):
        if 1 not in m[i-1]+m[i]+m[(i+1)%n]:
                continue
        for j in range(n):
            
            check_n(i,j)
    m=new_m
    display()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fps+=0.5
            elif event.key == pygame.K_LEFT:
                fps+=-0.5
