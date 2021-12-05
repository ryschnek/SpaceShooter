import pygame
from os import path
class move:
    def __init__(self):
        self.__speed_x = 0

    def move_Left(self):
        self.__speed_x = -5

    def move_Right(self):
        self.__speed_x = 5

    def move_Player(self, rect):
        rect.x += self.__speed_x

    def reset_Speed(self):
        self.__speed_x = 0

    def get_Speed(self):
        return self.__speed_x
