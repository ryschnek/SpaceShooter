import pygame
from os import path
import Animations as anim
import constants as con

#Takes in a sprite to destroy and creates a destroy object with the image
#Replaces the images with an explosion animation
class Destroy(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = con.explosion_animation[self.size][0]
        self.rect = self.image.get_rect()
        self.cur_frame = 0
        self.rect.center = center
        self.frames = 75
        self.updated = pygame.time.get_ticks()

#updates itself, and kills itself upon reaching end of animation
    def update(self):
        cur = pygame.time.get_ticks()
        if cur - self.updated > self.frames:
            self.updated = cur
            self.cur_frame += 1
            if self.cur_frame == len(con.explosion_animation[self.size]):
                self.kill()
            else:
                self.image = con.explosion_animation[self.size][self.cur_frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
