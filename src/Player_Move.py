import pygame
from os import path
class move:

    #initializes speed as zero
    def __init__(self):
        self.__speed_x = 0


    #Left and right movement functions that change speed

    def move_Left(self):
        self.__speed_x = -5

    def move_Right(self):
        self.__speed_x = 5

    #Moves the Player according to what the speed is
    def move_Player(self, rect):
        rect.x += self.__speed_x

    #Sets speed to zero
    def reset_Speed(self):
        self.__speed_x = 0

    #returns the speed value
    def get_Speed(self):
        return self.__speed_x
