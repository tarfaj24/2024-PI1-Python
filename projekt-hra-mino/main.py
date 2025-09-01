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
        self.y_pozicia_hitboxy = 300
        self.rect = self.image.get_rect(midbottom = (200,self.y_pozicia))
        self.gravity = 0
        self.gravity_hitboxy = 0

        mino_walk_3_hitbox = pygame.transform.scale(pygame.image.load("môj projekt-1/grafiky/mino-walk-1_cropped.png").convert_alpha(),(50,142.5))
        self.mino_walk_3_hitbox_rect = mino_walk_3_hitbox.get_rect(midbottom = (200,self.y_pozicia_hitboxy))

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
        print(self.gravity)

    def gravitacia(self):
        self.gravity+= 1
        self.rect.y += self.gravity
        if self.rect.bottom > self.y_pozicia:
            self.rect.bottom = self.y_pozicia

    def input_skocenie_hitboxy(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.mino_walk_3_hitbox_rect.bottom >=self.y_pozicia_hitboxy:
                self.gravity_hitboxy=-20
        
    def gravitacia_hitboxy(self):
        self.gravity_hitboxy+= 1
        self.mino_walk_3_hitbox_rect.y += self.gravity_hitboxy
        if self.mino_walk_3_hitbox_rect.bottom > self.y_pozicia_hitboxy:
            self.mino_walk_3_hitbox_rect.bottom = self.y_pozicia_hitboxy 
            
        
    
   

    def get_hitbox(self):
        return self.mino_walk_3_hitbox_rect
        

 
        

    def update(self):
        self.animacia_mino_walk()
        self.input_skocenie()
        self.gravitacia()
        self.get_hitbox()
        self.gravitacia_hitboxy()
        self.input_skocenie_hitboxy()
        
        
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
        self.get_hitboxy()
    def destroy(self):
        if self.rect.x < 0:
            self.kill()
    def get_hitboxy(self):
        return self.rect    
    

        
def kolizia():

    for mino_index in mino:
        for prasa in prasa_group:
            if mino_index.get_hitbox().colliderect(prasa.get_hitboxy()):
                print("teraz")
            # print (mino_index.get_hitbox())
            # print(prasa.get_hitboxy())
        

    
    

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("mino-RUNNER")
clock = pygame.time.Clock()
#background
background_surface = pygame.image.load("môj projekt-1/grafiky/testovaci-background-2.png").convert_alpha()
background_scaled = pygame.transform.scale(background_surface,(800,400))

font = pygame.font.Font("pygame intro/font/Pixeltype.ttf",50)

prasa_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(prasa_timer,1500)



mino = pygame.sprite.GroupSingle()
mino.add(Mino())



prasa_group = pygame.sprite.Group()

nazov_hry = font.render("Runner Mino",False,(64,64,64))
nazov_hry_rect =nazov_hry.get_rect(center = (400,100))

instrukcia_text = font.render("Na zacatie hry stlac space",False,(64,64,64))
instrukcia_text_rect = instrukcia_text.get_rect(center = (400,200))

while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if kolizia() == True:
        if event.type == prasa_timer:
                prasa_group.add(Prasa())      
    # if kolizia()== True:
    screen.blit(background_scaled,(0,0))
    mino.draw(screen)
    mino.update()
    prasa_group.draw(screen)
    prasa_group.update()
    kolizia()
    # else:
    #     screen.fill("yellow")
    #     screen.blit(nazov_hry,nazov_hry_rect)
    #     screen.blit(instrukcia_text,instrukcia_text_rect)


    pygame.display.update()
    clock.tick(60)
