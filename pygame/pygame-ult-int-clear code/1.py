import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("pygame intro/font/pixeltype.ttf", 50)

test_surface = pygame.image.load("pygame intro/graphics/Sky.png").convert_alpha()
test_ground_surface = pygame.image.load("pygame intro/graphics/ground.png").convert_alpha()
text_surface = test_font.render("moja hra",False, "black")
snail_surface = pygame.image.load("pygame intro/graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("pygame intro/graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom =(80,300))
snail_rect= snail_surface.get_rect(bottomright= (600,300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(0,0))
    screen.blit(test_ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)
    
    snail_rect.x-=4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    
    
    if player_rect.colliderect(snail_rect)== True:
        print("zrazka") 

    
    
    
    
    

    pygame.display.update()
    clock.tick(60)