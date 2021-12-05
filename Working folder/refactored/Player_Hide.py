import pygame
from os import path
import constants as con
class hidden:
    
    def __init__(self):
        self.__off = False
        self.__hide_timer = pygame.time.get_ticks()

    def unhide(self, rect):
        if pygame.time.get_ticks() - self.__hide_timer > con.hidetime:
            self.__off = False
            rect.centerx = con.WIDTH / 2
            rect.bottom = con.HEIGHT - 30

    def hide(self, rect):
        self.__off = True
        self.__hide_timer = pygame.time.get_ticks()
        rect.center = (con.WIDTH / 2, con.HEIGHT + 200)

    def get_hide(self):
        return self.__off
