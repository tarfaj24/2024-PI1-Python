import pygame
import random
import math
import os
import time

class Taiga(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        taiga_width = 48
        taiga_length = 90
        self.taiga_color = "normal"

        #pred scalom
        taiga_pred_1 = pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_1.png").convert_alpha()
        taiga_pred_2 = pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_2.png").convert_alpha()
        taiga_pred_3 = pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_3.png").convert_alpha()
        taiga_pred_4 = pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_4.png").convert_alpha()

        #po scale
        taiga_walk_1 = pygame.transform.scale(taiga_pred_1,(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_2 = pygame.transform.scale(taiga_pred_2,(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_3 = pygame.transform.scale(taiga_pred_3,(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_4 = pygame.transform.scale(taiga_pred_4,(taiga_width,taiga_length)).convert_alpha()

        taiga_walk_1_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-walk_1_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_2_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_2_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_3_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-walk_3_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_4_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_4_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        
        self.taiga_walk_green = [taiga_walk_1_green,taiga_walk_2_green,taiga_walk_3_green,taiga_walk_4_green]

        taiga_walk_1_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-walk_1_brown.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_2_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_2_brown.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_3_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-walk_3_brown.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_4_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_4_brown.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        
        self.taiga_walk_brown = [taiga_walk_1_brown,taiga_walk_2_brown,taiga_walk_3_brown,taiga_walk_4_brown]

        taiga_walk_1_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_1_dark_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_2_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_2_dark_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_3_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_3_dark_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_4_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_4_dark_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()

        self.taiga_walk_dark_green = [taiga_walk_1_dark_green,taiga_walk_2_dark_green,taiga_walk_3_dark_green,taiga_walk_4_dark_green]

        taiga_walk_1_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_1_orange.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_2_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_2_orange.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_3_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_3_orange.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        taiga_walk_4_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_walk_4_orange.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()

        self.taiga_walk_orange = [taiga_walk_1_orange,taiga_walk_2_orange,taiga_walk_3_orange,taiga_walk_4_orange]

        #dashes
        self.taiga_dash = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga_dash.png").convert_alpha(),(taiga_width+40,taiga_length+40)).convert_alpha()
        
        self.taiga_dash_charge_0 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-0.png").convert_alpha()
        self.taiga_dash_charge_1 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-1.png").convert_alpha()
        self.taiga_dash_charge_2 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-2.png").convert_alpha()
        self.taiga_dash_charge_3 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-3.png").convert_alpha()
        self.taiga_dash_charge_4 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-4.png").convert_alpha()
        self.taiga_dash_charge_5 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-5.png").convert_alpha()
        self.taiga_dash_charge_6 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-6.png").convert_alpha()
        self.taiga_dash_charge_7 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-dashes/taiga-dash-7.png").convert_alpha()
        self.taiga_dash_charge_8 = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga-dashes/taiga-dash-8-final.png").convert_alpha(),(60,60)).convert_alpha()

        self.taiga_dashes = [self.taiga_dash_charge_0,self.taiga_dash_charge_1,self.taiga_dash_charge_2,self.taiga_dash_charge_3,self.taiga_dash_charge_4,self.taiga_dash_charge_5,
                             self.taiga_dash_charge_6,self.taiga_dash_charge_7]
        self.taiga_dash_animation = [pygame.transform.scale(taiga_dash,(60,60)).convert_alpha() for taiga_dash in self.taiga_dashes]

        self.taiga_fire = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire.png").convert_alpha(),(147,167)).convert_alpha()
        self.taiga_fire_2 = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_fire_2.png").convert_alpha(),(147,167)).convert_alpha()
        self.taiga_fire_jump_1 = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-1.png").convert_alpha(),(105,130)).convert_alpha()
        self.taiga_fire_jump_2 = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-2.png").convert_alpha(),(120,130)).convert_alpha()
        taiga_jump = pygame.image.load("Taiga-game/grafiky-taiga/taiga-jump.png").convert_alpha()
        self.taiga_jump_scaled = pygame.transform.scale(taiga_jump,(taiga_width,taiga_length)).convert_alpha()
        
        self.taiga_jump_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_jump_brown.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        self.taiga_jump_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_jump_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        self.taiga_jump_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_jump_orange.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()
        self.taiga_jump_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga_jump_dark_green.png").convert_alpha(),(taiga_width,taiga_length)).convert_alpha()

        self.fire_on_frame = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/fire-on.png"),(60,60)).convert_alpha()
        self.fire_off_frame = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/fire-off.png"),(60,60)).convert_alpha()

        self.taiga_fire_jump_1_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-1_green.png"),(105,130)).convert_alpha()
        self.taiga_fire_jump_1_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-1_brown.png"),(105,130)).convert_alpha()
        self.taiga_fire_jump_1_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-1_orange.png"),(105,130)).convert_alpha()
        self.taiga_fire_jump_1_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-1_dark_green.png"),(105,130)).convert_alpha()

        self.taiga_fire_jump_2_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-2_green.png"),(120,130)).convert_alpha()
        self.taiga_fire_jump_2_brown = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-2_brown.png"),(120,130)).convert_alpha()
        self.taiga_fire_jump_2_orange = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-2_orange.png"),(120,130)).convert_alpha()
        self.taiga_fire_jump_2_dark_green = pygame.transform.scale(pygame.image.load("Taiga-game/grafiky-taiga/taiga-fire-jump-2_dark_green.png"),(120,130)).convert_alpha()

        self.taiga_walk = [taiga_walk_1,taiga_walk_2,taiga_walk_3,taiga_walk_4]

        self.ground_y_position = 300
        self.index = 0
        self.gravity = 0

        self.fire_index = 0
        self.fire_animation_var = 0
        self.fire_y_pos = 173
        self.fire_time = 0
        self.fire_can_run = False
        self.can_start_fire = True
        self.dash_y_pos = 170
        self.dash_index = 1
        self.dash_time_index = 0
        self.can_dash = False
        self.can_press_dash = True
        self.time_till_another_dash = 0
        self.taiga_dash_animation_index = 0
        self.fire_gravity = 0
        self.taiga_dash_animation_index_while_fire = 0
        self.image = self.taiga_walk[self.index]
    
        self.rect = self.image.get_rect(midbottom = (200,self.ground_y_position))

        self.headhitbox = pygame.Rect(170,100,60,27)
        self.bodyhitbox = pygame.Rect(190,270,20,90)
    
    def animacia(self):
        self.index += index_speed_var
        if self.index >= len(self.taiga_walk):
            self.index = 0
        if self.taiga_color == "normal":
            self.image = self.taiga_walk[int(self.index)]
        elif self.taiga_color == "green":
            self.image = self.taiga_walk_green[int(self.index)]
        elif self.taiga_color == "orange":
            self.image = self.taiga_walk_orange[int(self.index)]
        elif self.taiga_color == "dark_green":
            self.image = self.taiga_walk_dark_green[int(self.index)]
        elif self.taiga_color == "brown":
            self.image = self.taiga_walk_brown[int(self.index)]



        if self.rect.bottom < self.ground_y_position:
                if self.taiga_color == "normal":
                    self.image = self.taiga_jump_scaled
                elif self.taiga_color == "green":
                    self.image = self.taiga_jump_green
                elif self.taiga_color == "orange":
                    self.image = self.taiga_jump_orange
                elif self.taiga_color == "dark_green":
                    self.image = self.taiga_jump_dark_green
                elif self.taiga_color == "brown":
                    self.image = self.taiga_jump_brown
                

    def input_skocenie(self):
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.ground_y_position:
            self.fire_gravity =-19.57
            self.gravity=-20
            

        
    def gravitacia(self):
        
        self.gravity+=1 
        self.fire_gravity+=0.95
        self.fire_y_pos+= self.fire_gravity
        self.rect.y+=self.gravity
        self.headhitbox.y+=self.gravity
        self.bodyhitbox.y+= self.gravity
        self.dash_y_pos+=self.gravity
       
        if self.rect.bottom >= self.ground_y_position:
            self.rect.bottom = self.ground_y_position 
            self.headhitbox.top = 243
            self.bodyhitbox.top = 215
            self.fire_y_pos = 173
            self.dash_y_pos = 170
            
         
    
    def fire(self):
        keys = pygame.key.get_pressed()
        
        if self.fire_index == 0:
            if self.can_start_fire == True:
                screen.blit(self.fire_on_frame,(860,20))
                if keys[pygame.K_f]:
                    self.fire_can_run = True
            else:
                screen.blit(self.fire_off_frame,(860,20))

            if self.fire_can_run == True:
                screen.blit(self.taiga_dash_animation[int(self.taiga_dash_animation_index_while_fire)],(800,20))
                self.taiga_dash_animation_index_while_fire+= 0.0133

                self.can_press_dash = False
                self.can_start_fire = False
                self.fire_time += (1/60)
                self.fire_animation_var+=0.1
                if self.rect.bottom >= self.ground_y_position:
                    if int(self.fire_animation_var) == 0:
                        screen.blit(self.taiga_fire,(126,self.fire_y_pos))
                        

                    if int(self.fire_animation_var) == 1:
                        screen.blit(self.taiga_fire_2,(126,self.fire_y_pos))
                    if int(self.fire_animation_var) > 1:
                        self.fire_animation_var = 0
                    
                else:  
                    if int(self.fire_animation_var) == 0:
                        if self.taiga_color == "normal":
                            screen.blit(self.taiga_fire_jump_1,(147,self.fire_y_pos))
                        elif self.taiga_color == "green":
                            screen.blit(self.taiga_fire_jump_1_green,(147,self.fire_y_pos))
                        elif self.taiga_color == "orange":
                            screen.blit(self.taiga_fire_jump_1_orange,(147,self.fire_y_pos))
                        elif self.taiga_color == "dark_green":
                            screen.blit(self.taiga_fire_jump_1_dark_green,(147,self.fire_y_pos))
                        elif self.taiga_color == "brown":
                            screen.blit(self.taiga_fire_jump_1_brown,(147,self.fire_y_pos))
                    
                        

                    if int(self.fire_animation_var) == 1:
                        if self.taiga_color == "normal":
                            screen.blit(self.taiga_fire_jump_2,(142,self.fire_y_pos))
                        elif self.taiga_color == "green":
                            screen.blit(self.taiga_fire_jump_2_green,(142,self.fire_y_pos))
                        elif self.taiga_color == "orange":
                            screen.blit(self.taiga_fire_jump_2_orange,(142,self.fire_y_pos))
                        elif self.taiga_color == "dark_green":
                            screen.blit(self.taiga_fire_jump_2_dark_green,(142,self.fire_y_pos))
                        elif self.taiga_color == "brown":
                            screen.blit(self.taiga_fire_jump_2_brown,(142,self.fire_y_pos))
                    if int(self.fire_animation_var) > 1:
                        self.fire_animation_var = 0

                if self.fire_time > 10:
                        self.fire_can_run = False

            else: 
                self.taiga_dash_animation_index_while_fire = 0
                
    def dash(self):
        keys = pygame.key.get_pressed()
        if self.can_press_dash == True:
            self.time_till_another_dash = 0
            if keys[pygame.K_d]:
                self.can_dash = True
        if self.can_dash == True:
            self.image = self.taiga_dash 
            if self.dash_y_pos > 170:
                self.rect.y = 170
                
            else:
                self.rect.y = self.dash_y_pos
            for obstacle in obstacles:
                obstacle.pos_x -= 20
            self.dash_time_index+= 1/60
            if self.dash_time_index > 0.15:
                self.can_dash = False
                self.can_press_dash = False
        if self.can_press_dash == False:
            self.time_till_another_dash+=1/60
            if self.time_till_another_dash > 10:
                self.can_press_dash = True
                self.dash_time_index = 0
      
          
        
       

    def draw_rect(self):
        pygame.draw.rect(screen,"yellow",self.headhitbox)
        pygame.draw.rect(screen,"yellow",self.bodyhitbox)

    def dash_animation(self):
        if self.fire_can_run == False:
            if self.can_press_dash == True:
                self.taiga_dash_animation_index = 0
                screen.blit(self.taiga_dash_charge_8,(800,20))
            else:
                screen.blit(self.taiga_dash_animation[int(self.taiga_dash_animation_index)],(800,20))
                self.taiga_dash_animation_index+= 0.0133
            
    
    
    def update(self):
        self.input_skocenie()
        self.gravitacia()
        self.animacia()
        self.fire()
        self.dash()
        self.dash_animation()
        
        #self.draw_rect()    
        
    



class Obstacles(pygame.sprite.Sprite):
    obstacle_update_variable = 0
    def __init__(self,type):
        super().__init__()
       

        if type == "kaktus":
            self.type = "kaktus"
            kaktus = pygame.image.load("Taiga-game\grafiky-taiga\kaktus_normalny.png").convert_alpha()
            kaktus_scaled = pygame.transform.scale(kaktus,(57.4,93.8)).convert_alpha()
            self.y_pos = 300
            self.frames = [kaktus_scaled]

        
        if type == "maly_kaktus":
            self.type = "maly_kaktus"
            maly_kaktus = pygame.image.load("Taiga-game\grafiky-taiga\maly_kaktus_normalny.png").convert_alpha()
            maly_kaktus_scaled = pygame.transform.scale(maly_kaktus,(44.2,47.6)).convert_alpha()
            self.y_pos = 300
            self.frames = [maly_kaktus_scaled]
          
        
        if type == "kaktus_bodky":
            self.type = "kaktus_bodky"
            kaktus_bodky = pygame.image.load("Taiga-game\grafiky-taiga\kaktus_bodky.png").convert_alpha()
            kaktus_bodky_scaled = pygame.transform.scale(kaktus_bodky,(57.4,93.8)).convert_alpha()
            self.y_pos = 300
            self.frames = [kaktus_bodky_scaled]
         

        if type == "maly_kaktus_bodky":
            self.type = "maly_kaktus_bodky"
            maly_kaktus_bodky = pygame.image.load("Taiga-game\grafiky-taiga\maly_kaktus_bodky.png").convert_alpha()
            maly_kaktus_bodky_scaled = pygame.transform.scale(maly_kaktus_bodky,(44.2,47.6)).convert_alpha()
            self.y_pos = 300
            self.frames = [maly_kaktus_bodky_scaled]
          

        if type == "flying_dog":
            self.type = "flying_dog"
            flying_dog_1 = pygame.image.load("Taiga-game/grafiky-taiga/flying_dog.png").convert_alpha()
            flying_dog_1_scaled = pygame.transform.scale(flying_dog_1,(90,55.5)).convert_alpha()

            flying_dog_2 = pygame.image.load("Taiga-game\grafiky-taiga/flying_dog_2.png").convert_alpha()
            flying_dog_2_scaled_ = pygame.transform.scale(flying_dog_2,(90,55.5)).convert_alpha()

            self.y_pos = 190
            self.frames = [flying_dog_1_scaled,flying_dog_2_scaled_]

        if type == "taiga_cow":
            self.type = "taiga-cow"
            taiga_cow_1 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-cow-1.png").convert_alpha()
            taiga_cow_scaled = pygame.transform.scale(taiga_cow_1,(130,110)).convert_alpha()

            taiga_cow_2 = pygame.image.load("Taiga-game\grafiky-taiga/taiga-cow-2.png").convert_alpha()
            taiga_cow_2_scaled = pygame.transform.scale(taiga_cow_2,(130,110)).convert_alpha()

            self.y_pos = 190
            self.frames = [taiga_cow_scaled,taiga_cow_2_scaled]

        if type == "taiga_cow_lower":
            self.type = "taiga-cow_lower"
            taiga_cow_1 = pygame.image.load("Taiga-game/grafiky-taiga/taiga-cow-1.png").convert_alpha()
            taiga_cow_scaled = pygame.transform.scale(taiga_cow_1,(130,110)).convert_alpha()

            taiga_cow_2 = pygame.image.load("Taiga-game\grafiky-taiga/taiga-cow-2.png").convert_alpha()
            taiga_cow_2_scaled = pygame.transform.scale(taiga_cow_2,(130,110)).convert_alpha()

            self.y_pos = 280
            self.frames = [taiga_cow_scaled,taiga_cow_2_scaled]
        
        if type == "flying_dog_lower":
            self.type = "flying_dog_lower"
            flying_dog_1 = pygame.image.load("Taiga-game/grafiky-taiga/flying_dog.png").convert_alpha()
            flying_dog_1_scaled = pygame.transform.scale(flying_dog_1,(90,55.5)).convert_alpha()

            flying_dog_2 = pygame.image.load("Taiga-game\grafiky-taiga/flying_dog_2.png").convert_alpha()
            flying_dog_2_scaled_ = pygame.transform.scale(flying_dog_2,(90,55.5)).convert_alpha()

            self.y_pos = 270

            self.frames = [flying_dog_1_scaled,flying_dog_2_scaled_]
        
        if type == "double_small_cactus":
            self.type = "double_small_cactus"
            double_small_cactus = pygame.image.load("Taiga-game\grafiky-taiga\double_maly_kaktus.png").convert_alpha()
            double_small_cactus_scaled = pygame.transform.scale(double_small_cactus,(90,47.6)).convert_alpha()
            self.y_pos = 300
            self.frames = [double_small_cactus_scaled]

        if type == "triple_small_cactus":
            self.type = "triple_small_cactus"
            triple_small_cactus = pygame.image.load("Taiga-game\grafiky-taiga/triple_maly_kaktus.png").convert_alpha()
            triple_small_cactus_scaled = pygame.transform.scale(triple_small_cactus,(145,47.6)).convert_alpha()
            self.y_pos = 300
            self.frames = [triple_small_cactus_scaled]
        
        if type == "double_big_kaktus":
            self.type = "double_big_kaktus"
            double_big_cactus = pygame.image.load("Taiga-game\grafiky-taiga\double_big_kaktus.png").convert_alpha()
            double_big_cactus_scaled = pygame.transform.scale(double_big_cactus,(125,93.8)).convert_alpha()
            self.y_pos = 300
            self.frames = [double_big_cactus_scaled]
        
        if type == "triple_big_kaktus":
            self.type = "triple_big_kaktus"
            triple_big_cactus = pygame.image.load("Taiga-game\grafiky-taiga/triple_big_kaktus.png").convert_alpha()
            triple_big_cactus_scaled = pygame.transform.scale(triple_big_cactus,(180,93.8)).convert_alpha()
            self.y_pos = 300
            self.frames = [triple_big_cactus_scaled]
            
        if type == "alien":
            self.type = "alien"
            alien_blue = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/alien_blue.png").convert_alpha(),(100,100)).convert_alpha()
            alien_orange = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/alien_orange.png").convert_alpha(),(100,100)).convert_alpha()
            alien_red = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/alien_red.png").convert_alpha(),(100,100)).convert_alpha()
            self.y_pos = 300
            self.frames =[alien_blue,alien_orange,alien_red]
        if type == "wall":
            self.type = "wall"
            wall = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga-wall.png").convert_alpha(),(65,135)).convert_alpha()
            self.y_pos = 300
            self.frames =[wall]
        if type == "taiga-shirt":
            self.type = "taiga-shirt"
            shirt_1 = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga-shirts-1.png").convert_alpha(),(100,105)).convert_alpha()
            shirt_2 = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga-shirts-2.png").convert_alpha(),(100,105)).convert_alpha()
            shirt_3 = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga-shirts-3.png").convert_alpha(),(100,105)).convert_alpha()
            shirt_4 = pygame.transform.scale(pygame.image.load("Taiga-game\grafiky-taiga/taiga-shirts-4.png").convert_alpha(),(100,105)).convert_alpha()
            self.y_pos = random.randint(100,300)
            shirts = [("shirt_green",shirt_1),("shirt_orange",shirt_2),("shirt_brown",shirt_3),("shirt_dark_green",shirt_4)]
            self.shirt_name,self.taiga_shirt_frame = random.choice(shirts)
            self.frames = [self.taiga_shirt_frame]
        
        if type == "4_kaktusy":
            self.type = "4_kaktusy"
            styri_kaktusy = pygame.image.load("Taiga-game\grafiky-taiga/4_kaktusy.png").convert_alpha()
            styri_kaktusy_scaled = pygame.transform.scale(styri_kaktusy,(260,106)).convert_alpha()
            self.y_pos = 300
            self.frames = [styri_kaktusy_scaled]

        
        self.index = 0
        self.image = self.frames[self.index]
        self.obstacle_distance = random.randint(1100,1300)
        self.rect = self.image.get_rect(midbottom = (self.obstacle_distance,self.y_pos))
        self.pos_x = int(self.rect.x)
    def animation(self):
        self.index+=0.1
        if self.index <=2:
            try:
                self.image = self.frames[int(self.index)]
            except IndexError:
                self.image = self.frames[0]

        
        else:
            self.index = 0
    
    
        
    def update(self):
        self.animation()
        self.pos_x -=int(obstacle_speed_up_var)
        self.rect.x = self.pos_x
        
        
        
        if self.rect.right < 0:
            self.kill()
       
        
        
        

        
        

def kolizia():
    
    
    if taiga_sprite.can_dash == False:
        if taiga_sprite.fire_can_run != True:
            
            for obstacle in obstacles:
                # print(f"meno je :{obstacle.type}, x je {obstacle.rect.x}")
                if obstacle.type != "taiga-shirt":
                
                    if taiga_sprite.headhitbox.colliderect(obstacle.rect):
                        obstacles.empty()
                        return False
                else:
                    if taiga_sprite.headhitbox.colliderect(obstacle.rect):
                        if obstacle.shirt_name == "shirt_brown":
                            taiga_sprite.taiga_color = "brown"
                        elif obstacle.shirt_name == "shirt_green":
                            taiga_sprite.taiga_color = "green"
                        elif obstacle.shirt_name == "shirt_dark_green":
                            taiga_sprite.taiga_color = "dark_green"
                        elif obstacle.shirt_name == "shirt_orange":
                            taiga_sprite.taiga_color = "orange"

                        
                        taiga_sprite.can_start_fire = True
                        taiga_sprite.fire_time = 0 
                        taiga_sprite.fire_can_run = False
                        
                        

                        obstacle.kill()
                    
            for obstacle in obstacles:
                # if obstacle.type == "kaktus":
                    # print(int(obstacle.pos_x))
                if obstacle.type != "taiga-shirt":
                    if taiga_sprite.bodyhitbox.colliderect(obstacle.rect):
                        obstacles.empty()
                        return False
                else:
                    if taiga_sprite.bodyhitbox.colliderect(obstacle.rect):
                        if obstacle.shirt_name == "shirt_brown":
                            taiga_sprite.taiga_color = "brown"
                        elif obstacle.shirt_name == "shirt_green":
                            taiga_sprite.taiga_color = "green"
                        elif obstacle.shirt_name == "shirt_dark_green":
                            taiga_sprite.taiga_color = "dark_green"
                        elif obstacle.shirt_name == "shirt_orange":
                            taiga_sprite.taiga_color = "orange"
                        taiga_sprite.can_start_fire = True
                        taiga_sprite.fire_time = 0
                        taiga_sprite.fire_can_run = False
                        
                        
                        obstacle.kill()
        else:
            for obstacle in obstacles:
                if taiga_sprite.bodyhitbox.colliderect(obstacle.rect):
                    obstacle.kill()
                if taiga_sprite.headhitbox.colliderect(obstacle.rect):
                    obstacle.kill()
                
                
        
                    
                
        
    return True

def score_displaying():
    current_time = int(pygame.time.get_ticks() / 100) - start_time - pause_time
    score_surf = font.render(f'Your score is: {current_time}',False,(1,1,1)).convert_alpha()
    score_rect = score_surf.get_rect(center = (500,30))
    screen.blit(score_surf,score_rect)                                                                               
    return current_time
    


def highest_score():
    list_with_scores = [high_score]
    list_with_scores.append(score)
    max_score = max(list_with_scores)
    return max_score
    




    


    
def you_died_animacia():
    
    


    you_died_animacia = [you_died_1_scaled,you_died_2_scaled,you_died_3_scaled,you_died_snimka_scaled]
    you_died_animacia = you_died_animacia[index_hlavny]
    you_died_snimka_rect = you_died_animacia.get_rect()

    screen.blit(you_died_animacia,you_died_snimka_rect)
    
   
def alien_control():
    
    for obstacle in obstacles:
        if obstacle.type == "alien":
            
            if int(alien_y_pos_index) == 0:
                screen.blit(alien_indicator_down,(750,22))
                obstacle.rect.y = 100
                obstacle.image= obstacle.frames[int(alien_index)]
                
                
            elif int(alien_y_pos_index) == 1:
                screen.blit(alien_indicator_up,(750,22))
                obstacle.image= obstacle.frames[int(alien_index)]
                obstacle.rect.y = 600
            elif int(alien_y_pos_index) == 2:
                screen.blit(alien_indicator_up,(750,22))
                obstacle.image= obstacle.frames[int(alien_index)]
                obstacle.rect.y = 200
            else:
                screen.blit(alien_indicator_down,(750,22))
                obstacle.image= obstacle.frames[int(alien_index)]
                obstacle.rect.y = 600

def fireeee_napis():
    fire_napis = font_fire_napis.render("FIREEEE!!!",False,(255, 69, 0))
    screen.blit(fire_napis,(60,60))




pygame.init()

clock = pygame.time.Clock()



#screen
screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

#background surface
bg_pred_scalom = pygame.image.load("Taiga-game/grafiky-taiga/background.png").convert()
bg_width = 800
bg_height = 300
bg = pygame.transform.scale(bg_pred_scalom,(bg_width,bg_height)).convert()



bg_bottom_width = 800
bg_bottom_height = 400
bg_bottom = pygame.image.load("Taiga-game\grafiky-taiga/background-ground.png").convert()
bg_bottom_scaled = pygame.transform.scale(bg_bottom,(bg_bottom_width,100)).convert()


#timers
cas_obstacle_timer = 950

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,cas_obstacle_timer)

pause_timer = pygame.USEREVENT + 2
pygame.time.set_timer(pause_timer,1000)

obstacle_unpause_fix_timer = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_unpause_fix_timer,int(cas_obstacle_timer/100))




taiga = pygame.sprite.GroupSingle()
taiga.add(Taiga())
taiga_sprite = taiga.sprite

obstacles = pygame.sprite.Group()

font = pygame.font.Font("pygame intro/font/Pixeltype.ttf",50)
font_big = pygame.font.Font("pygame intro/font/Pixeltype.ttf",85)
font_fire_napis = pygame.font.Font("pygame intro/font/Pixeltype.ttf",300)
#texty
instrukcia_text = font.render("Press SPACE to play",False,(0,0,0))
instrukcia_text_rect = instrukcia_text.get_rect()

#fire

#you_died_images
you_died_snimka = pygame.image.load("Taiga-game\grafiky-taiga\you_died_hlavna_snimka.png").convert_alpha()
you_died_snimka_scaled = pygame.transform.scale(you_died_snimka,(1000,400)).convert_alpha()

you_died_animacia_1 = pygame.image.load("Taiga-game\grafiky-taiga\you_died_snimka_1.png").convert_alpha()
you_died_animacia_2 = pygame.image.load("Taiga-game\grafiky-taiga\you_died_snimka_2.png").convert_alpha()
you_died_animacia_3 = pygame.image.load("Taiga-game\grafiky-taiga\you_died_snimka_3.png").convert_alpha()

you_died_1_scaled = pygame.transform.scale(you_died_animacia_1,(1000,400)).convert_alpha()
you_died_2_scaled = pygame.transform.scale(you_died_animacia_2,(1000,400)).convert_alpha()
you_died_3_scaled = pygame.transform.scale(you_died_animacia_3,(1000,400)).convert_alpha()

#alien_images
alien_indicator_up = pygame.image.load("Taiga-game\grafiky-taiga/alien_indicator_up.png").convert_alpha()
alien_indicator_down = pygame.image.load("Taiga-game\grafiky-taiga/alien_indicator_down.png").convert_alpha()


#game variables
start_time = 0
index = 0
index_hlavny = 0
you_died_variable = 0
list_with_scores = []
you_died_text_index = 0
score = 0
obstacle_speed_up_var = 7
cas_obstacle_timer_speed_up_var=0.1
index_speed_var = 0.1
pause_time = 0
obstacle_timer_wait = 0
cislo = -7
obstacle_can_run = True
time_to_wait = 0
obstacle_timer_one_run_variable = 0
pause_only_once_variable=0
alien_index = 0
alien_y_pos_index = 0
can_start_fire_nadpis = False
fire_napis_start = False
fire_napis_time = 0
#subory
score_read_subor = open("Taiga-game/highest_score_taiga.txt","r")
if os.path.getsize("Taiga-game\highest_score_taiga.txt") == 0:
    high_score = 0
else:
    score_list_2 = []
    high_score_lines = score_read_subor.readlines()
    for line in high_score_lines:
        score_list_2.append(int(line.strip()))
    high_score = max(score_list_2)
    
 


score_subor = open("Taiga-game/highest_score_taiga.txt","w")
print(f"{high_score}",file=score_subor)



tiles = math.ceil(screen_width / bg_width) + 1
scroll = 0
scroll_bg_bottom = 0
game_active = "game_start_surf"

prev_time = time.perf_counter()

while True:
    
   
       
    #ZACIATOK EVENT LOOPU
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            score_subor.close()
            score_read_subor.close()
            pygame.quit()
            exit()
        
        if game_active == True:
            
            if event.type == obstacle_unpause_fix_timer:
                cislo+=1
               
                if cislo > time_to_wait:
                    obstacle_can_run = True
         
            
            if obstacle_can_run == True:
                obstacle_timer_one_run_variable+=1
                if obstacle_timer_one_run_variable < 2:
                    pygame.time.set_timer(obstacle_timer,10)
                elif obstacle_timer_one_run_variable < 3:
                    
                    pygame.time.set_timer(obstacle_timer,int(cas_obstacle_timer))
                
                if event.type == obstacle_timer:
                    taiga_shirt_randint = random.randint(0,100)
                    if taiga_sprite.can_start_fire == False and taiga_sprite.fire_can_run == False:
                        if taiga_shirt_randint == 1:
                            obstacles.add(Obstacles("taiga-shirt"))
                  

                    if taiga_shirt_randint != 1 or taiga_sprite.can_start_fire == True or taiga_sprite.fire_can_run == True:
                        if score < 150:
                            obstacles.add(Obstacles(random.choice(["flying_dog_lower","maly_kaktus","maly_kaktus_bodky",
                            "kaktus","kaktus_bodky","flying_dog","kaktus"])))
                        if 150 <= score < 300:
                            obstacles.add(Obstacles(random.choice(["flying_dog_lower","maly_kaktus","maly_kaktus_bodky",
                            "kaktus","kaktus_bodky","flying_dog","double_small_cactus","alien","wall","kaktus"])))
                        if 300 <= score < 450:
                            obstacles.add(Obstacles(random.choice(["flying_dog_lower","maly_kaktus","maly_kaktus_bodky","kaktus","kaktus_bodky",
                            "flying_dog","double_small_cactus","triple_small_cactus","alien","wall"])))
                        if 450 <= score < 1000:
                            obstacles.add(Obstacles(random.choice(["flying_dog_lower","maly_kaktus","maly_kaktus_bodky",
                            "kaktus","kaktus_bodky","flying_dog","double_small_cactus","triple_small_cactus","double_big_kaktus","alien","wall","taiga_cow"])))
                        if 1000 <= score < 1300:
                            obstacles.add(Obstacles(random.choice(["flying_dog_lower","maly_kaktus","maly_kaktus_bodky",
                            "kaktus","kaktus_bodky","flying_dog","double_small_cactus","triple_small_cactus","double_big_kaktus",
                            "triple_big_kaktus","flying_dog","flying_dog_lower","alien","triple_big_kaktus","wall","taiga_cow","taiga_cow_lower"])))
                        if score >= 1300:
                            obstacles.add(Obstacles(random.choice(["flying_dog_lower","maly_kaktus","maly_kaktus_bodky",
                            "kaktus","kaktus_bodky","flying_dog","double_small_cactus","triple_small_cactus","double_big_kaktus",
                            "triple_big_kaktus","flying_dog","flying_dog_lower","alien","triple_big_kaktus","wall","taiga_cow","taiga_cow_lower","4_kaktusy"])))


                    
                
  
            
            
            
        if game_active == "pause_game":
            if event.type == pause_timer:
                pause_time+=1
                
                
                
            
            

        if game_active != True:
            if you_died_variable>1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    start_time = int(pygame.time.get_ticks() / 100)
                    game_active = True
                    you_died_variable = 0 
                    you_died_text_index = 0
                    obstacle_speed_up_var = 7
                    cas_obstacle_timer_speed_up_var=0.1
                    cas_obstacle_timer = 950
                    
    #KONIEC EVENT LOOPU
    if game_active == True:

        for i in range(0,tiles):
            screen.blit(bg,(i * bg_width+scroll,0))
            screen.blit(bg_bottom_scaled,(i * bg_bottom_width+scroll_bg_bottom,300))
            
            
            
        #scroll background
        scroll -=4
        scroll_bg_bottom-= int(obstacle_speed_up_var)
        
            

        if abs(scroll) > bg_width:
            scroll += bg_width
        if abs(scroll_bg_bottom) > bg_bottom_width:
            scroll_bg_bottom += bg_bottom_width
            
        cas_obstacle_timer-= cas_obstacle_timer_speed_up_var
                    
        if score < 1300  :
            cas_obstacle_timer_speed_up_var+=0.0003
        else:
            cas_obstacle_timer_speed_up_var+=0.03
            cislo = 0

        if score < 1300:
                obstacle_speed_up_var+=0.04 / 60
                index_speed_var+=0.0005 / 60
        else:
            obstacle_speed_up_var+= 0.03 / 60
            index_speed_var+= 0.0003 / 60

        

        
        taiga.draw(screen)
        taiga.update()
       


        obstacles.draw(screen)
        obstacles.update()
        
        if taiga_sprite.can_dash == False:
            if taiga_sprite.fire_can_run != True:
                for obstacle in obstacles:
                    if obstacle.type == "taiga-shirt":
                        if taiga_sprite.headhitbox.colliderect(obstacle.rect):
                            can_start_fire_nadpis = True
                        
                for obstacle in obstacles:
                    if obstacle.type == "taiga-shirt":
                        if taiga_sprite.bodyhitbox.colliderect(obstacle.rect):
                            can_start_fire_nadpis = True
                        
        if can_start_fire_nadpis == True:
            fireeee_napis()
            fire_napis_time += 1/60
            if fire_napis_time > 1:
                can_start_fire_nadpis = False
                fire_napis_time = 0

        alien_y_pos_index+= 0.03
        if alien_y_pos_index > 4:
            alien_y_pos_index = 0
        if alien_index < 3:
            alien_control()
            if 0< alien_y_pos_index < 1 or 2 < alien_y_pos_index < 3:
                alien_index+=0.08
            else:
                alien_index = 0

        else:
            alien_index = 0
        game_active = kolizia()
       
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and index == 3:
                index = 0
        if keys[pygame.K_p] and pause_only_once_variable<=1:
            game_active = "pause_game"
            pause_only_once_variable=2
        

        if taiga_sprite.can_dash == True:
            scroll -=10
            scroll_bg_bottom -= 20
       
       
        score = score_displaying()
        
        
    elif game_active == "pause_game":
        obstacle_timer_one_run_variable = 0
        obstacle_can_run = False
        keys = pygame.key.get_pressed()
        time_to_wait = 100-cislo
        # print(f"time to wait is:{time_to_wait} ")
        
        if keys[pygame.K_u]:
            game_active = True
            
            
        
            
                
    elif game_active == "game_start_surf":
            you_died_variable+=0.0166
            you_died_text_index+=0.5
            pygame.Surface.fill(screen,(90,90,90))

        
    #death
    else:
        taiga_sprite.taiga_color = "normal"
        taiga_sprite.taiga_dash_animation_index = 0
        taiga_sprite.dash_index = 1
        taiga_sprite.dash_time_index = 0
        taiga_sprite.can_dash = False
        taiga_sprite.can_press_dash = True
        taiga_sprite.time_till_another_dash = 0
        index_speed_var = 0.1
        taiga_sprite.fire_time = 0
        taiga_sprite.fire_can_run = False
        taiga_sprite.can_start_fire = True
        fire_index = 0
        pause_only_once_variable = 0
        ciso = -7
        time_to_wait = 0
        pause_time = 0
        you_died_variable+=0.0166
        you_died_text_index+=0.5

        if index < 3:
            index+=0.1
            index_hlavny = int(index)
            you_died_animacia()
        else:
            index = 3
            you_died_animacia()

        if you_died_text_index > 11:
            you_died_text = font_big.render(f"Your current score is: {score}",False,(173,216,230))
            you_died_text_rect = you_died_text.get_rect(center = (500,50))

    
    
            print(f"{score}",file = score_subor)
            highest_score()

            max_score_text = font_big.render(f"Your highest score is: {f"{highest_score()}"}",False,(173,216,230))
            max_score_text_rect = max_score_text.get_rect(center =(500,110))



            screen.blit(you_died_text,you_died_text_rect)
            screen.blit(max_score_text,max_score_text_rect)
            
            
    # current_time_1 = time.perf_counter()
    # frame_time = current_time_1 - prev_time  # in seconds
    # prev_time = current_time_1

    # frame_time_ms = frame_time * 1000
    # print(f"Frame time: {frame_time_ms:.2f} ms")    
        
    
    

    pygame.display.update()
    clock.tick_busy_loop(60)
    
   
    
    