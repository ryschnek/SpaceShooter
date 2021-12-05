import pygame
from os import path
import constants as con

class ability:
    
    def __init__(self):
        self.__power = 1
        self.__power_timer = pygame.time.get_ticks()

    def powerdown(self):
        if pygame.time.get_ticks() - self.__power_timer > con.poweruptime:
            self.__power -= 1
            self.__power_timer = pygame.time.get_ticks()
            
    def powerup(self):
        self.__power += 1
        self.__power_timer = pygame.time.get_ticks()

    def get_Power(self):
        return self.__power
