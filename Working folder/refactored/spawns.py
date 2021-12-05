import pygame
from os import path
import random
import constants as con

powerup_image = {}
powerup_image['shield'] = pygame.image.load(path.join('objects', 'shield_gold.png')).convert()
powerup_image['levelup'] = pygame.image.load(path.join('objects', 'bolt_gold.png')).convert()

bullet_image = pygame.image.load(path.join('objects', 'laserRed16.png')).convert()
missile_image = pygame.image.load(path.join('objects', 'missile.png')).convert_alpha()

class spawn_bullet(pygame.sprite.Sprite):      ## defines the sprite for bullets
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)    ##load image for bullet
        self.image = bullet_image
        self.image.set_colorkey(con.BLACK)
        
        self.rect = self.image.get_rect()      ##rectangle created around the object represnting object in pygame that allows object to interact with other other in game objects
        self.rect.centerx = x
        self.rect.bottom = y      

        self.speed_y = -10                     ##set the speed of the bullet object

    def update(self):
        self.rect.y += self.speed_y            ##rectangle moves with the object as they both travel accross the screen
        if self.rect.bottom < 0:               ##if the rectangle representing the object travels past the top of the screen, it is upated 
            self.kill()                        ##object is destroyed past the height of the screen 


class spawn_missile(pygame.sprite.Sprite):     ## defines the sprite for missiles;
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)    ##load image for missile 
        self.image = missile_image
        self.image.set_colorkey(con.BLACK)

        self.rect = self.image.get_rect()      ##rectangle created around the object represnting object in pygame that allows object to interact with other other in game objectste
        self.rect.centerx = x
        self.rect.bottom = y

        self.speed_y = -10                     ##set the speed of the bullet object
 
    def update(self):
        self.rect.y += self.speed_y            ##rectangle moves with the object as they both travel accross the screen
        if self.rect.bottom < 0:               ##if the rectangle representing the object travels past the top of the screen, it is updated 
            self.kill()                        ##object is destroyed past the height of the screen 

class spawn_powerup(pygame.sprite.Sprite):     ## defines the sprite for powerups
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'levelup'])   ##spawns object randomly between shield or levelup
        self.image = powerup_image[self.type]
        self.image.set_colorkey(con.BLACK)

        self.rect = self.image.get_rect()       ##rectangle created around the object represnting object in pygame that allows object to interact with other other in game objects
        self.rect.center = center
        self.speed_y = 4

    def update(self):
        self.rect.y += self.speed_y             ##rectangle moves with the object as they both travel accross the screen

