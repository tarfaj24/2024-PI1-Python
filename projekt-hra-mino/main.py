import pygame
import random
from sys import exit

class Mino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        mino_walk_1 = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/mino-walk-1.png").convert_alpha(),(160,160))
        mino_walk_2 = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/mino-walk-2.png").convert_alpha(),(160,160))
        mino_walk_3 = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/mino-walk-3.png").convert_alpha(),(160,160))
        self.mino_jump = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/mino-jump.png").convert_alpha(),(160,160))
        self.mino_walk = [mino_walk_1,mino_walk_2,mino_walk_3]
        self.mino_walk_index = 0
        self.image = self.mino_walk[self.mino_walk_index]
        self.y_pozicia = 300
        self.rect = self.image.get_rect(midbottom = (200,self.y_pozicia))
        self.gravity = 0

    def animacia_mino_walk(self):
        if self.rect.bottom < self.y_pozicia:
            self.image = self.mino_jump
        else:

            self.mino_walk_index+= 0.1
            if self.mino_walk_index > len(self.mino_walk): 
                self.mino_walk_index=0
            self.image = self.mino_walk[int(self.mino_walk_index)]

        
    
    def input_skocenie(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >=self.y_pozicia:
                self.gravity=-20

    def gravitacia(self):
        self.gravity+= 1
        self.rect.y += self.gravity
        if self.rect.bottom > self.y_pozicia:
            self.rect.bottom = self.y_pozicia  

        

    def update(self):
        self.animacia_mino_walk()
        self.input_skocenie()
        self.gravitacia()
        
class Prasa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        prasa_walk_1 = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/kaja-walk-1-kopia.png").convert_alpha(),(55,55))
        prasa_walk_2 = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/kaja-walk-2-kopia.png").convert_alpha(),(55,55 ))
        self.prasa_walk = [prasa_walk_1,prasa_walk_2]
        self.prasa_index = 0
        self.image = self.prasa_walk[self.prasa_index]
        self.y_pozicia = 300
        self.rect = self.image.get_rect(midbottom = (800,self.y_pozicia))
        

    def animacia_prasa(self):
        self.prasa_index+=0.1
        if self.prasa_index > len(self.prasa_walk):
           self.prasa_index=0 
        self.image = self.prasa_walk[int(self.prasa_index)]
        
    
    def update(self):
        self.animacia_prasa()
        self.rect.x-=5
        self.destroy()
    def destroy(self):
        if self.rect.x < 0:
            self.kill()        
        

    

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("mino-RUNNER")
clock = pygame.time.Clock()
#background
background_surface = pygame.image.load("môj projekt-1/grafiky/testovaci-background-2.png").convert_alpha()
background_scaled = pygame.transform.scale(background_surface,(800,400))

prasa_timer = pygame.USEREVENT + 1
pygame.time.set_timer(prasa_timer,1500)

mino = pygame.sprite.GroupSingle()
mino.add(Mino())

prasa = pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == prasa_timer:
            prasa.add(Prasa())      

    screen.blit(background_scaled,(0,0))

    mino.draw(screen)
    mino.update()
    prasa.draw(screen)
    prasa.update()


    pygame.display.update()
    clock.tick(60)
