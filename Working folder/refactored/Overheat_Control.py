import pygame
from os import path
import spawns
import constants as con

class Overheat:
    def __init__(self):
        self.__overheat = 0
        self.__hot = False
        
    def get_Overheat(self):
        return self.__overheat

    def reset_Overheat(self):
        self.__overheat = 0

    def cool(self):
        self.__hot = False

    def update_Overheat(self, dO):
        self.__overheat += dO
        if self.__overheat < 0:
            self.__overheat = 0
        if self.__overheat > 100:
            self.__overheat = 100

    def update_Hot(self, update):
        self.__hot = update

    def get_Hot(self):
        return self.__hot
        
