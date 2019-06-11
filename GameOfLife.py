#GAME OF LIFE
import copy
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

logo=pygame.image.load(".\logo.png")
start=pygame.image.load(".\start.png")
winlogo=pygame.image.load(".\winlogo.png")
cover=pygame.image.load(".\cover.png")

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GameOfLife")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()


font = pygame.font.SysFont('freesansbold.ttf', 20)

#FUNCTIONS

fps=5
m=[]
new_m=[]
n=50

def reset_game():
    global fps, new_m, m
    fps=5
    m=[]
    new_m=[]
    n=50
    for n_rows in range(n):
        row_temp=[]
        for n_col in range(n):
            row_temp.append(0)
        m.append(row_temp)   
    screen.fill(WHITE)
    screen.blit(cover,(0,200))
    pygame.display.flip()
    pygame.time.delay(1000)
    
reset_game()

def display():
    global fps, n, m
    screen.fill(GREY)
    screen.blit(logo,(0,0))
    
    for row in range(7,n):
        for column in range(n):
            color = BLACK
            if m[row][column] == 1:
                color = WHITE
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
    
    text = font.render("fps:"+str(fps), True, BLACK)
    screen.blit(text,(445,53))
    #manual input of position
    
    if fps<=0.5:
        fps+=1
    clock.tick(fps) 
    pygame.display.flip()


# xth row and yth column
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
        
def preset(tup):
    for i in tup:
        m[i[0]][i[1]]=1
def main():    
    global m, fps, n,new_m
    
    display()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    running=False
                if event.key== pygame.K_1:
                    preset(((20,25),(21,24),(21,25),(21,26),(22,24),(22,26),(27,24),(27,26),(28,24),(28,26),(29,24),(29,25),(29,26),(30,25)))
                    display()
                if event.key== pygame.K_2:
                    preset(((24,19),(24,22),(24,23),(24,25),(24,26),(24,27),(24,28),(24,30),(25,19),(25,20),(25,21),(25,22),(25,23),(25,24),(25,26),(25,27),(25,30)))
                    display()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                m[row][column] = 1
                display()
            elif event.type==pygame.QUIT:
                running=False
                quit()
    
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
                elif event.key == pygame.K_ESCAPE:
                    reset_game()
                    main()

#intro
screen.fill(WHITE)
screen.blit(start,(0,0))
pygame.time.delay(1000)
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

main()
