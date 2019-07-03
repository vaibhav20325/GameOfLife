#GAME OF LIFE
import copy
import pygame
import module_button

#Display
BLACK = (0, 0, 0)
GREY=(50,50,50)
WHITE = (255, 255, 255)
DULLW=(127,255,212)
WIDTH = 9
HEIGHT = 9
MARGIN = 1

pygame.init()
WINDOW_SIZE = [501, 522]

logo=pygame.image.load(".\logo.png")
start=pygame.image.load(".\start.png")
winlogo=pygame.image.load(".\winlogo.png")
cover=pygame.image.load(".\cover.png")

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GameOfLife")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()


font1 = pygame.font.SysFont('freesansbold.ttf', 20)
font2 = pygame.font.SysFont('freesansbold.ttf', 15)
#FUNCTIONS




fps=60
m=[]
new_m=[]
n=50


def glider(x,y):
    return ((y-1,x-1),(y-1,x),(y-1,(x+1)%n),(y,x-1),((y+1)%n,x))

def spaceship(x,y):
    return ((y-1,x-1),(y,x-2),((y+1)%n,x-2),((y+2)%n,x-2),((y+2)%n,x-1),((y+2)%n,x),((y+2)%n,(x+1)%n),((y+1)%n,(x+2)%n),(y-1,(x+2)%n))

def m_coordinate():
    return pygame.mouse.get_pos()[0] // (WIDTH + MARGIN), pygame.mouse.get_pos()[1] // (HEIGHT + MARGIN)

def reset_game():
    global fps, new_m, m
    fps=60
    m=[]
    new_m=[]
    n=50
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

def display(l):
    global fps, n, m, button1, button2
    screen.fill(GREY)
    screen.blit(logo,(0,0))
    
    for row in range(7,n):
        for column in range(n):
            color = BLACK
            if l[row][column] == 1:
                color = WHITE
            elif l[row][column] == 2:
                color = DULLW
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
    
    text = font1.render("fps:"+str(fps), True, BLACK)
    screen.blit(text,(445,53))
    #manual input of position
    button1=pygame.rect.Rect((MARGIN + WIDTH) * 0 + MARGIN*1,(MARGIN + HEIGHT) * 50 + MARGIN*2,WIDTH*5,HEIGHT*2)
    pygame.draw.rect(screen, WHITE ,button1)
    screen.blit(font2.render("GLIDER", True, BLACK),(MARGIN*3,(MARGIN + HEIGHT) * 50 + MARGIN*6))
    
    button2=pygame.rect.Rect((MARGIN + WIDTH) * 5 + MARGIN*3,(MARGIN + HEIGHT) * 50 + MARGIN*2,WIDTH*7,HEIGHT*2)
    pygame.draw.rect(screen, WHITE ,button2)
    screen.blit(font2.render("SPACESHIP", True, BLACK),(WIDTH*5+MARGIN*8,(MARGIN + HEIGHT) * 50 + MARGIN*6))
    
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
        
def preset(tupl,l,n=1):
    for i in tupl:
        l[i[0]][i[1]]=n
        
def button_click(desn):
    global m, new_m
    hover=True
    while hover:
        for event in pygame.event.get():
            new_m=copy.deepcopy(m)
            x,y=m_coordinate()
            try:
                preset(desn(x,y),new_m,2)
                display(new_m)
            except:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    x,y=m_coordinate()
                    preset(desn(x,y),m)
                    hover=False
            elif event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        hover=False
                        break        



def main():    
    global m, fps, n,new_m, button1, button2
    
    display(m)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    running=False
                if event.key== pygame.K_1:
                    preset(((20,25),(21,24),(21,25),(21,26),(22,24),(22,26),(27,24),(27,26),(28,24),(28,26),(29,24),(29,25),(29,26),(30,25)),m)
                    display(m)
                if event.key== pygame.K_2:
                    preset(((24,19),(24,22),(24,23),(24,25),(24,26),(24,27),(24,28),(24,30),(25,19),(25,20),(25,21),(25,22),(25,23),(25,24),(25,26),(25,27),(25,30)),m)
                    display(m)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    column,row=m_coordinate()
                    if row<n:
                        m[row][column] = 1
                        display(m)
                    elif button1.collidepoint(event.pos):
                        button_click(glider)
                        display(m)
                    elif button2.collidepoint(event.pos):
                        button_click(spaceship)
                        display(m)     
            elif event.type==pygame.QUIT:
                running=False
                quit()        
             
    running=True
    fps=5
    while running:
        
        new_m=copy.deepcopy(m)
        for i in range(n):
            if 1 not in m[i-1]+m[i]+m[(i+1)%n]:
                    continue
            for j in range(n):
                check_n(i,j)
        m=new_m
        display(m)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    fps+=0.5
                elif event.key == pygame.K_LEFT:
                    fps+=-0.5
                #TEMP
                elif event.key == pygame.K_UP:
                    fps=30
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
