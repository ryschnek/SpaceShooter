import pygame
from os import path
import constants as con
class hidden:
    
    #inializes as on, so the player is visible
    def __init__(self):
        self.__off = False
        self.__hidden_timer = pygame.time.get_ticks()


    #Unhides the player and places the ship at the start position
    def unhide(self, rect):
        if pygame.time.get_ticks() - self.__hide_timer > con.hidetime:
            self.__off = False
            rect.centerx = con.WIDTH / 2
            rect.bottom = con.HEIGHT - 30

    #hides the player
    def hide(self, rect):
        self.__off = True
        self.__hide_timer = pygame.time.get_ticks()
        rect.center = (con.WIDTH / 2, con.HEIGHT + 200)

    #returns whether the player is hidden
    def get_hide(self):
        return self.__off
