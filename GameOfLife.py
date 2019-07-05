#GAME OF LIFE
import copy
import pygame
import module_button
#Display
BLACK = (0, 0, 0)
GREY=(50,50,50)
WHITE = (255, 255, 255)
BLUE=(127,255,212)
WIDTH = 9
HEIGHT = 9
MARGIN = 1
B_MARGIN=2
B_WIDTH=60
B_HEIGHT=18


button1,button2,button3=0,0,0
button=[button1,button2,button3]
names=['GLIDER','SAPCESHIP','CUSTOM']

pygame.init()
WINDOW_SIZE = [501, 542]

logo=pygame.image.load(".\logo.png")
start=pygame.image.load(".\start.png")
winlogo=pygame.image.load(".\winlogo.png")
cover=pygame.image.load(".\cover.png")

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GameOfLife")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()


font1 = pygame.font.SysFont('freesansbold.ttf', 20)
font2 = pygame.font.SysFont('freesansbold.ttf', 16)
#FUNCTIONS



infinite_grid=False
fps=60
m=[]
new_m=[]
n=50


def m_coordinate():
    return pygame.mouse.get_pos()[0] // (WIDTH + MARGIN), pygame.mouse.get_pos()[1] // (HEIGHT + MARGIN)

def textfunc(text,textcolour, coordinate):
    textsurface=font2.render(text, True, textcolour)
    textrect=textsurface.get_rect()
    textrect.center=(coordinate[0]+B_WIDTH/2,coordinate[1]+B_HEIGHT/2)
    screen.blit(textsurface,textrect)
    

def reset_game():
    global fps, new_m, m, BLACK, WHITE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
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
    global fps, n, m, button, button_grid, B_COLOUR
    screen.fill(GREY)
    screen.blit(logo,(0,0))
    
    for row in range(7,n):
        for column in range(n):
            color = BLACK
            if l[row][column] == 1:
                color = WHITE
            elif l[row][column] == 2:
                color = BLUE
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
    
    text = font1.render("fps:"+str(fps), True, (0,0,0))
    # Manual Color
    
    screen.blit(text,(445,53))
    #manual input of position
    
    for i in range(3):
        coord=((B_MARGIN + B_WIDTH)* i + B_MARGIN*1,500 + B_MARGIN*1)
        button[i]=pygame.rect.Rect(coord[0],coord[1],B_WIDTH,B_HEIGHT)
        pygame.draw.rect(screen, WHITE ,button[i])
        textfunc(names[i],BLACK,coord)
    
    
    coord=((B_MARGIN + B_WIDTH)* 6 + B_MARGIN*1,500 + B_MARGIN*1)
    button_grid=pygame.rect.Rect(coord[0],coord[1],B_WIDTH,B_HEIGHT)
    pygame.draw.rect(screen, WHITE ,button_grid)
    textfunc('GRID',BLACK,coord)
    
    
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
        if not(infinite_grid):
            sum_n=m[x-1][y]+m[(x+1)%n][y]+m[x][(y+1)%n]+m[x][y-1]+m[x-1][y-1]+m[x-1][(y+1)%n]+m[(x+1)%n][y-1]+m[(x+1)%n][(y+1)%n]
        else:
            sum_n=m[x-1][y]+m[x+1][y]+m[x][y+1]+m[x][y-1]+m[x-1][y-1]+m[x-1][y+1]+m[x+1][y-1]+m[x+1][y+1]
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
        
def preset(tupl,l,n=1):
    for i in tupl:
        l[i[0]][i[1]]=n
        
def button_click(desn,file_name):
    global m, new_m
    hover=True
    while hover:
        for event in pygame.event.get():
            new_m=copy.deepcopy(m)
            x,y=m_coordinate()
            try:
                preset(desn(file_name,x,y),new_m,2)
                display(new_m)
            except:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    x,y=m_coordinate()
                    preset(desn(file_name,x,y),m)
                    hover=False
            elif event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        hover=False
                        break        



def main():    
    global m, fps, n,new_m, WIDTH, HEIGHT, MARGIN, infinite_grid, WHITE, BLACK
    
    display(m)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    running=False
                if event.key== pygame.K_q:
                    infinite_grid=True
                    display(m)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    column,row=m_coordinate()
                    if row<n:
                        m[row][column] = 1

                    elif button[0].collidepoint(event.pos):
                        button_click(module_button.new_button,'glider')
                    elif button[1].collidepoint(event.pos):
                        button_click(module_button.new_button,'spaceship')
                    elif button[2].collidepoint(event.pos):
                        button_click(module_button.new_button,'custom')
                    elif button_grid.collidepoint(event.pos):
                        MARGIN=1-MARGIN
                        if WIDTH==9:
                            WIDTH+=1
                            HEIGHT+=1
                        else:
                            WIDTH-=1
                            HEIGHT-=1
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
                elif event.key == pygame.K_UP:
                    fps=30
                elif event.key == pygame.K_ESCAPE:
                    reset_game()
                    main()
                elif event.key == pygame.K_g:
                    MARGIN=1-MARGIN
                    if WIDTH==9:
                        WIDTH+=1
                        HEIGHT+=1
                    else:
                        WIDTH-=1
                        HEIGHT-=1
                elif event.key == pygame.K_c:
                    BLACK,WHITE=WHITE,BLACK
                    

#intro
'''
screen.fill(WHITE)
screen.blit(start,(0,0))
pygame.time.delay(3000)
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
'''
main()
