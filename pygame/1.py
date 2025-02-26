import pygame 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("okno")

sky = pygame.image.load("pygame intro/graphics/Sky.png")

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky,(0,0))
    clock.tick(60)
    pygame.display.update()

    