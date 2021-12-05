#CONSTANTS module, used by a variety of other modules to clean up code

import pygame
from os import path
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =  (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
HEALTH_LENGTH = 100
HEALTH_HEIGHT = 10
OVERHEAT_LENGTH = 100
OVERHEAT_HEIGHT = 10
FPS = 60
SHOOT_DELAY = 250
poweruptime = 5000
hidetime = 1000
BAR_LENGTH = 100
BAR_HEIGHT = 10
images = path.join(path.dirname(__file__), 'objects')
sounds = path.join(path.dirname(__file__), 'sounds')
font_name = pygame.font.match_font('arial')
player_img = pygame.image.load(path.join('objects', 'playerShip1_orange.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
explosion_animation = {}
explosion_animation['big'] = []
explosion_animation['small'] = []
explosion_animation['play'] = []

for i in range(0, 9):
    file1 = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join('objects', file1)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_animation['big'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_animation['small'].append(img_sm)

    file2 = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join('objects', file2)).convert()
    img.set_colorkey(BLACK)
    explosion_animation['play'].append(img)
