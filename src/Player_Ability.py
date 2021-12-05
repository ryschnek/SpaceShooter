import pygame
from os import path
import constants as con

class ability:
    
    #Starts the powerup, and records what time it started
    def __init__(self):
        self.__power = 1
        self.__power_timer = pygame.time.get_ticks()


    #Removes one set of powerups, time for the powerup has expired
    def powerdown(self):
        if pygame.time.get_ticks() - self.__power_timer > con.poweruptime:
            self.__power -= 1
            self.__power_timer = pygame.time.get_ticks()
    
    #Adds a level of powerup to the plater      
    def powerup(self):
        self.__power += 1
        self.__power_timer = pygame.time.get_ticks()

    #Getter for the powerup level
    def get_Power(self):
        return self.__power
