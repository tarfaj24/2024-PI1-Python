import pygame

pygame.init()

screen_width = 800
scree_height = 600

screen = pygame.display.set_mode((screen_width,scree_height))


player = pygame.Rect(300,300,50,50)



run = True
while run:

    pygame.draw.rect(screen,(255,0,255),player)


    key = pygame.key.get_pressed()

    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()