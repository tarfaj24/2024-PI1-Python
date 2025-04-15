import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int((pygame.time.get_ticks() / 1000)) - start_time
    score_surface = test_font.render(f"Score: {current_time}",False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=5

            screen.blit(snail_surface,obstacle_rect)

        return obstacle_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("pygame intro/font/pixeltype.ttf", 50)
game_active = False
start_time = 0

test_surface = pygame.image.load("pygame intro/graphics/Sky.png").convert_alpha()
test_ground_surface = pygame.image.load("pygame intro/graphics/ground.png").convert_alpha()

gamenametext = test_font.render("HRA...", False, (64,64,64))
gamenametext_rect = gamenametext.get_rect(center = (400,70))

instrukciatext = test_font.render("Na zacatie hry stlac SPACE", False, (64,64,64))
instrukciatext_rect = instrukciatext.get_rect(center = (400,120))

score = 0

player_surface = pygame.image.load("pygame intro/graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom =(80,300))
player_gravity = 0
player_stand = pygame.image.load("pygame intro/graphics/player/player_stand.png").convert_alpha()
player_stand_scaled = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (375,180))

#obstacles
snail_surface = pygame.image.load("pygame intro/graphics/snail/snail1.png").convert_alpha()
snail_rect= snail_surface.get_rect(bottomright= (600,300))

obstacle_rect_list = []

# score_surface = test_font.render("My game",False,(64,64,64))
# score_rect = score_surface.get_rect(center = (800/2,50))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity= -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity= -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int((pygame.time.get_ticks()) / 1000)
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(bottomright= (randint(900,1100),300)))

    if game_active:


        screen.blit(test_surface,(0,0))
        screen.blit(test_ground_surface,(0,300))
        # pygame.draw.rect(screen,"#c0e8ec",score_rect)
        # pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
        # screen.blit(score_surface,score_rect)
        score = display_score()

        
        

        # snail_rect.x -=4
        # if snail_rect.right<=0:
        #     snail_rect.left =800
        # screen.blit(snail_surface,snail_rect)

        #player
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface,player_rect)

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #kolizia
        if snail_rect.colliderect(player_rect):
            game_active=False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand_scaled,player_stand_rect)
        screen.blit(gamenametext,gamenametext_rect)
        
        score_message = test_font.render(f"your score: {score}",False, (64,64,64))
        score_message_rect = score_message.get_rect(center=(400,330))

        if score == 0:
            screen.blit(instrukciatext,instrukciatext_rect)
            
        else:
            screen.blit(score_message,score_message_rect)

    

    pygame.display.update()
    clock.tick(60)