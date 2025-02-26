import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("pygame intro/font/pixeltype.ttf", 50)

test_surface = pygame.image.load("pygame intro/graphics/Sky.png").convert_alpha()
test_ground_surface = pygame.image.load("pygame intro/graphics/ground.png").convert_alpha()



player_surface = pygame.image.load("pygame intro/graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom =(80,300))
player_gravity = 0

snail_surface = pygame.image.load("pygame intro/graphics/snail/snail1.png").convert_alpha()
snail_rect= snail_surface.get_rect(bottomright= (600,300))

score_surface = test_font.render("My game",False,(64,64,64))
score_rect = score_surface.get_rect(center = (800/2,50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("kolizia")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")
        if event.type == pygame.KEYUP:
            print("keyup")



    screen.blit(test_surface,(0,0))
    screen.blit(test_ground_surface,(0,300))
    pygame.draw.rect(screen,"#c0e8ec",score_rect)
    pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
    screen.blit(score_surface,score_rect)
    
    
    screen.blit(snail_surface,snail_rect)

    #player
    player_gravity +=1
    player_rect.y += player_gravity
    screen.blit(player_surface,player_rect)


    # snail_rect.x-=4
    # if snail_rect.right <= 0:
    #     snail_rect.left = 800
    
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")
    
    
    # if player_rect.colliderect(snail_rect)== True:
    #     print("zrazka") 

    #mousemotion mozme aj v eventloope pomocou podmienky
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
    
    

    pygame.display.update()
    clock.tick(60)