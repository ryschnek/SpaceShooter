import pygame
from os import path
import random
import constants as con

asteroidtype = ['meteorBrown_big1.png','meteorBrown_big2.png','meteorBrown_med1.png', 'meteorBrown_med3.png','meteorBrown_small1.png','meteorBrown_small2.png','meteorBrown_tiny1.png']
pics = []

for image in asteroidtype:
    pics.append(pygame.image.load(path.join('objects', image)).convert())


def newobject(sprites,asteroids):                        ##adds movement element to the asteroids and sprites 
    movement = movingobject()
    sprites.add(movement)
    asteroids.add(movement)


class movingobject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original = random.choice(pics)             ##randomly assign the choice of asteorid object from pics array
        self.original.set_colorkey(con.BLACK)
        self.image = self.original.copy()

        self.spin = 0                                     ## for adding spin        
        self.rotspeed = random.randrange(-10,10)

        self.speed_y = random.randrange(0,12)             ## randomize the y axis speed of object
        self.speed_x = random.randrange(-4,4)             ## randomize the x axis speed of object

        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, con.WIDTH - self.rect.width)  ##these 2 lines create a rectangle around the object representing the asteroid and its properties using pygame library
        self.rect.y = random.randrange(-150, -100)

    def rotate(self):
        self.spin = (self.spin + self.rotspeed) 

        lastposition = self.rect.center                     ##generates a new image of the object, rotated by a random amount in the exact place of the current object
        newposition = pygame.transform.rotate(self.original, self.spin)

        self.image = newposition
        self.rect = self.image.get_rect()   
        self.rect.center = lastposition                    ##position center of rectangle by the last position of the object before its update

    def update(self):
        self.rotate()
        self.rect.x += self.speed_x                        ##update rectangle to move at the speed that was declared earlier, allowing asteroid and rectangle to move together
        self.rect.y += self.speed_y

        if (self.rect.top > con.HEIGHT + 25) or (self.rect.left < -25) or (self.rect.right > con.WIDTH + 25):     ## creates new objects once asteroids travel outside the screen dimensions
            self.rect.y = random.randrange(-120, -30)       ##randomize generation of speed and position for new objects
            self.rect.x = random.randrange(0, con.WIDTH - self.rect.width)
            self.speed_y = random.randrange(0,12)                       
