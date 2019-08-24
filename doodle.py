
import pygame
import time
vector = pygame.math.Vector2

BLACK = (0, 0, 0)
GREEN= (10,250,10)
WHITE = (255, 255, 255)


#char = pygame.transform.scale(char, (50, 50))
pygame.init()
pygame.mixer.init()
WIDTH=500
HEIGHT=500
WINDOW_SIZE = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Menu")

#char_right=pygame.transform.scale(pygame.image.load(".\\char_right.png"),(50,50))
#char_left=pygame.transform.scale(pygame.image.load(".\\char_left.png"),(50,50))
#char_up=pygame.transform.scale(pygame.image.load(".\\char_up.png"),(50,55))

friction = -0.05
acceleration = 1
gravity = 1

clock = pygame.time.Clock()

def display():
    global land

    screen.fill(BLACK)
    #screen.blit(char,(coord_x,coord_y))
    clock.tick(30) 
    
    all_sprites.draw(screen)
    platforms.draw(screen)
    pygame.display.flip()

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = char_up.convert()
        #self.image.set_colorkey(BLACK)
        self.image = pygame.Surface((20,30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom=400
        self.pos = vector(250,250)
        self.vel = vector(0,0)
        self.acc = vector(0,0)

    def update(self):
        #self.image = char_up.convert()
        #self.image.set_colorkey(WHITE)
        self.acc = vector(0,gravity)

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            #self.image = char_right.convert()
            #self.image.set_colorkey(WHITE)
            self.acc.x += acceleration
        if keystate[pygame.K_LEFT]:
            #self.image = char_left.convert()
            #self.image.set_colorkey(WHITE)
            self.acc.x += -acceleration

        if keystate[pygame.K_UP]:
            self.vel.y += -5
            '''
            while not(self.rect.colliderect(land)) or i<10:
                i+=1
                
                self.vel
                time.sleep(0.02)
                display()
                self.speedy += (5 - (i*0.5))
             '''   
        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        self.rect.midbottom = self.pos

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        
        
        if self.rect.colliderect(land.rect):
            self.pos.y = land.rect.top
            self.vel.y = 0
        
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
land = Platform(0,HEIGHT-40,WIDTH,40)
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
    display()
        
