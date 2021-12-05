import pygame
from os import path
import spawns
import constants as con
from Overheat_Control import Overheat
from Player_Hide import hidden

class shoot:
    def __init__(self):
        self.last_shot = pygame.time.get_ticks()
        self.mouse_down = False
        
    def det_shoot_T(self, sprites, bullets, rect, hide, ovrht, power):
        if ovrht.get_Hot():
            ovrht.update_Overheat(-1)
            if ovrht.get_Overheat() == 0:
                ovrht.update_Hot(False)
        elif not self.mouse_down and ovrht.get_Overheat() < 90 and not hide.get_hide():
            self.mouse_down = True
            ovrht.update_Overheat(20)
            if ovrht.get_Overheat() > 90:
                ovrht.update_Hot(True)
            self.__fire(rect, sprites, bullets, power)
        elif hide.get_hide():
            self.__fire(rect, sprites, bullets, power)
        else:
            ovrht.update_Overheat(-1)
            
                        
    def det_shoot_F(self, ovrht):
        self.mouse_down = False
        if ovrht.get_Overheat() != 0:
            ovrht.update_Overheat(-1)
        else:
            ovrht.update_Hot(False)
                        
    def __fire(self, rect, sprites, bullets, power):
            #now = pygame.time.get_ticks()
            #if now - self.last_shot > con.SHOOT_DELAY:
                #self.last_shot = now
                if power == 1:
                    bullet = spawns.spawn_bullet(rect.centerx, rect.top)
                    sprites.add(bullet)
                    bullets.add(bullet)
                
                if power == 2:
                    bullet1 = spawns.spawn_bullet(rect.left, rect.centery)
                    bullet2 = spawns.spawn_bullet(rect.right, rect.centery)
                    sprites.add(bullet1)
                    sprites.add(bullet2)
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                
                if power >= 3:
                    bullet1 = spawns.spawn_bullet(rect.left, rect.centery)
                    bullet2 = spawns.spawn_bullet(rect.right, rect.centery)
                    missile1 = spawns.spawn_missile(rect.centerx, rect.top) 
                    sprites.add(bullet1)
                    sprites.add(bullet2)
                    sprites.add(missile1)
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                    bullets.add(missile1)

                if power >= 4:
                    missile1 = spawns.spawn_missile(rect.left, rect.centery) 
                    missile2 = spawns.spawn_missile(rect.right, rect.centery) 
                    missile3 = spawns.spawn_missile(rect.centerx, rect.top) 
                    sprites.add(missile1)
                    sprites.add(missile2)
                    sprites.add(missile3)
                    bullets.add(missile1)
                    bullets.add(missile2)
                    bullets.add(missile3)

##    def update_power(self, power):
##        self.power = power
##
##    def update_hide(self, hide):
##        self.hide = hide
