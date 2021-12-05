import pygame
from os import path
import spawns
import constants as con


class Overheat:

    #initalizes the overheat and hot values
    #hot being true prevents the player from shooting
    def __init__(self):
        self.__overheat = 0
        self.__hot = False
        

    #Getter for oveheat value
    def get_Overheat(self):
        return self.__overheat

    #reset once the overheat timeout if finished
    def reset_Overheat(self):
        self.__overheat = 0

    #reset the hot value
    def cool(self):
        self.__hot = False

    #update the overheat value upon shooting
    def update_Overheat(self, dO):
        self.__overheat += dO
        if self.__overheat < 0:
            self.__overheat = 0
        if self.__overheat > 100:
            self.__overheat = 100

    #Update the hot value
    def update_Hot(self, update):
        self.__hot = update

    #Getter for the hot value
    def get_Hot(self):
        return self.__hot
        
