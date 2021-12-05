import pygame
from os import path
import spawns
import constants as con
from Player_Shoot import shoot
from Player_Move import move
from Player_Hide import hidden
from Overheat_Control import Overheat
from Player_Ability import ability

class Player(pygame.sprite.Sprite):
    
    #initalizing the player with values for health, lives, and other values usch as position and powerups
    def __init__(self, sprites, bullets):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(con.player_img, (50, 38))
        self.image.set_colorkey(con.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = con.WIDTH / 2
        self.rect.bottom = con.HEIGHT - 10
        self.__health = 100
        self.__lives = 3
        self.__sprites = sprites
        self.__bullets = bullets
        self.__pos = move()
        self.__hide = hidden()
        self.__ovrht = Overheat()
        self.__shot = shoot()
        self.__power = ability()
        

    #Checks updates on the player for powerlevels and whether the player is hidden or not, along with movement and shooting if the relevant keys were pressed.
    def update(self):

        if self.__power.get_Power() >= 2:
            self.__power.powerdown()

        if self.__hide.get_hide():
            self.__hide.unhide(self.rect)
            #self.__shot.update_hide(False)
            

        self.__pos.reset_Speed()
        
        keystate = pygame.key.get_pressed()
        mousestate = pygame.mouse.get_pressed()
        
        if mousestate[0]:
            self.__shot.det_shoot_T(self.__sprites, self.__bullets, self.rect, self.__hide, self.__ovrht, self.__power.get_Power())
        else:
            self.__shot.det_shoot_F(self.__ovrht)
        if keystate[pygame.K_a]:
            self.__pos.move_Left()
        elif keystate[pygame.K_d]:
            self.__pos.move_Right()
        
            
        #if keystate[pygame.K_SPACE]:
            
        #    if not self.space_down:
        #       self.shoot()
        #       self.space_down = True
        #elif not keystate[pygame.K_SPACE]:
        #    self.space_down = False
                
        ## check for the borders at the left and right

        if self.rect.right > con.WIDTH:
            self.rect.right = con.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.__pos.move_Player(self.rect)
                   

    ##Accessors and mutators for values in the module

    def ability(self):
        self.__power.powerup()

##    def update_Pos(self, pos):
##        self.__pos = pos

##    def update_Overheat(self, ovrht):
##        self.__ovrht = ovrht
##        self.__shot.update_Overheat(ovrht)
        
    def update_Health(self, health):
        self.__health += health

    def reset_Health(self):
        self.__health = 100
        
##    def update_Shield(self, shield):
##        self.__shield = shield

    def update_Lives(self, lives):
        self.__lives += lives
        
    def get_Overheat(self):
        return self.__ovrht.get_Overheat()
        
    def get_Health(self):
        return self.__health

    def get_hide(self):
        return self.__hide.get_hide()
    
    def get_Lives(self):
        return self.__lives

##    def get_Rect(self):
##        return self.rect

    #Routine for when a player loses a life
    def die(self):
        self.__hide.hide(self.rect)
        self.__lives -= 1
        self.__health = 100
        self.__ovrht.reset_Overheat()
        self.__ovrht.cool()
        
##    #Resets players values after a death
##    def reset(self):
##        self.__health = 100
##        self.__ovrht.reset_Overheat()
##        self.__ovrht.cool()
