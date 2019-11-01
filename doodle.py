import pygame
import time
import random
vector = pygame.math.Vector2

BLACK = (0, 0, 0)
GREEN= (20,150,100)
WHITE = (255, 255, 255)
BLUE=(0,0,30)
YELLOW=(255,255,0)
RED=(250,0,10)
#winlogo=pygame.image.load(".\\char_left.png")
#char = pygame.transform.scale(char, (50, 50))
pygame.init()
font1 = pygame.font.SysFont('freesansbold.ttf', 19)
font2 = pygame.font.SysFont('freesansbold.ttf', 40)
pygame.mixer.init()
WIDTH=500
HEIGHT=500
WINDOW_SIZE = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Menu")
#pygame.display.set_icon(winlogo)
snow_img=pygame.transform.scale(pygame.image.load(".\\snow.png"),(15,15))
level_img=pygame.transform.scale(pygame.image.load(".\\level.png"),(70,8))
#char_right=pygame.transform.scale(pygame.image.load(".\\char_right.png"),(50,50))
#char_left=pygame.transform.scale(pygame.image.load(".\\char_left.png"),(50,50))
#char_up=pygame.transform.scale(pygame.image.load(".\\char_up.png"),(50,55))
counter={'health':0}
friction = -0.05
acceleration = 1
gravity = 1
clock = pygame.time.Clock()
game_time=0
hit=False
hit_time=0
def display():
    global game_time
    screen.fill(BLUE)
    #screen.blit(char,(coord_x,coord_y))
    clock.tick(30) 
    
    all_sprites.draw(screen)
    platforms.draw(screen)
    flakes.draw(screen)
    if power_up[0].visible:
        shields.draw(screen)


    text1 = font1.render("Health", True, WHITE)

    health_bar_back=pygame.rect.Rect(434,10,64,10)
    health_bar=pygame.rect.Rect(436,12,doodle.health,6)
    pygame.draw.rect(screen, WHITE ,health_bar_back)
    pygame.draw.rect(screen, GREEN ,health_bar)
    screen.blit(text1,(393,10))
    game_time+=1/30
    text2 = font1.render("Time:"+str(int(game_time)), True, WHITE)
    
    screen.blit(text2,(393,25))

    pygame.display.flip()

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w=0,h=0):
        pygame.sprite.Sprite.__init__(self)
        if w==0:
            self.image=level_img.convert()
        else:
            self.image = pygame.Surface((w,h))
            self.image.fill(WHITE)   
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Flakes(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3,3))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x+=random.randrange(-5,5)*random.random()
        self.rect.y+=5*random.random()
        if self.rect.x > WIDTH:
            self.rect.x -=500
        if self.rect.y > HEIGHT:
            self.rect.y -=500
        if self.rect.x <3:
            self.rect.x +=500
        if self.rect.y <3:
            self.rect.y +=500

class Shield(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((7,7))
        self.image=snow_img.convert()
        self.image.set_colorkey(WHITE)
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.visible=True
        self.hit_time=0
    def update(self):
        if int(game_time-self.hit_time)%5==0 or game_time<10:
            self.visible=False
            self.rect.y=random.randrange(0,300,30)
            self.rect.x=random.randrange(0,500,30)
        elif game_time-self.hit_time>0.5:
            self.visible=True    
    '''        
        self.rect.x+=random.randrange(-5,5)*random.random()
        self.rect.y+=5*random.random()
        if self.rect.x > WIDTH:
            self.rect.x -=500
        if self.rect.y > HEIGHT:
            self.rect.y -=500
        if self.rect.x <3:
            self.rect.x +=500
        if self.rect.y <3:
            self.rect.y +=500
    '''
class character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = char_up.convert()
        #self.image.set_colorkey(BLACK)
        self.image = pygame.Surface((20,30))
        self.rect = self.image.get_rect()
        self.rect.bottom=400
        self.pos = vector(250,250)
        self.vel = vector(0,0)
        self.acc = vector(0,0)
        self.health=60

    def update(self):
        global hit
        if hit:
            self.image.fill(RED)    
        else:
            self.image.fill(YELLOW)

        
        #self.image = char_up.convert()
        #self.image.set_colorkey(WHITE)
        self.acc = vector(0,gravity)

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            #self.image = char_right.convert()
            #self.image.set_colorkey(WHITE)
            self.acc.x += acceleration
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            #self.image = char_left.convert()
            #self.image.set_colorkey(WHITE)
            self.acc.x += -acceleration
        '''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.vel.y += -20
                    self.pos.y-=5
        '''
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            if self.vel.y in (-3,0):
                self.vel.y += -30
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.pos.y += 10
        if keystate[pygame.K_h]:
            self.health+=2
            
        '''
            while not(self.rect.colliderect(land)) or i<10:
                i+=1
                
                self.vel
                time.sleep(0.02)
                display()
                self.speedy += (5 - (i*0.5))
        '''   
        

        self.acc += self.vel * friction
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        self.rect.midbottom = self.pos

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        '''
        hit = pygame.sprite.spritecollide(self, platforms, False)
        if hit:
            self.vel.y = 0

        '''
        '''
        if pygame.sprite.spritecollide(self, land,False):
            self.pos.y = land.rect.top
            self.vel.y = 0
        '''
        
        global hit_time
        for i in flakes:
            if self.rect.colliderect(i.rect):
                self.health-=1.5
                hit=True
                hit_time=game_time
                i.rect.y=0
                if self.health<=0:
                    running=False
                    print(game_time)
                    print(counter)
                    print('YOUR SCORE:',counter['health']*10+int(game_time))
                    screen.fill(WHITE)
                    text2 = font2.render('YOUR SCORE:'+str(counter['health']*10+int(game_time)), True, BLACK)
                    screen.blit(text2,(150,200))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    quit()

        if game_time-hit_time>0.3:        
            hit=False
        for i in shields:
            if self.rect.colliderect(i.rect):
                if i.visible:
                    i.hit_time=game_time
                    i.visible=False
                    self.health+=10
                    counter['health']+=1
                    i.rect.y=random.randrange(0,300,10)
                    i.rect.x=random.randrange(0,500,10)
                if self.health>60:
                    self.health=60
        for i in platforms:
            if self.rect.colliderect(i.rect):
                    if self.rect.midtop[1] == i.rect.bottom:
                        self.vel.y=-1*(self.vel.y)
                    else:
                        self.pos.y = i.rect.top
                        self.vel.y = 0

        
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
flakes = pygame.sprite.Group()
shields = pygame.sprite.Group()

snow={}

for i in range (100):
    snow[i]=Flakes(random.randrange(0,500,5),random.randrange(0,450,5))
    flakes.add(snow[i])
land = Platform(0,HEIGHT-40,WIDTH,40)
levels={}
for i in range (12):
    
    levels[i]=Platform(random.randrange(0,450,40),random.randrange(50,450,30))
    platforms.add(levels[i])

power_up={}
for i in range (1):
    power_up[i]=Shield(random.randrange(0,500),random.randrange(0,450))
    shields.add(power_up[i])

platforms.add(land)

doodle = character()
all_sprites.add(doodle)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            quit()
    all_sprites.update()
    flakes.update()
    shields.update()
    display()
        
