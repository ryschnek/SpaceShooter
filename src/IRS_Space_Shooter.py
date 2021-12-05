
# @Author Ryan Schnekenburger Saad Khan Ibrahim Malik
# @Date: 2018/10/13

from __future__ import division
import pygame
import random
from os import path
import Animations as anim
import spawns 
import Asteroids as ast
import Player_Control as ply
import Destroy as des
from Player_Shoot import shoot
from Player_Move import move
from Player_Hide import hidden
from Overheat_Control import Overheat

#import sounds and images
images = path.join(path.dirname(__file__), 'objects')
sounds = path.join(path.dirname(__file__), 'sounds')


#constants used during runtime
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =  (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



#initializing the game
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) 
pygame.display.set_caption("IRS Space Shooter")



#loading game sprites and images
background = pygame.image.load(path.join('objects', 'starfield.png')).convert()
background_rect = background.get_rect()

player_img = pygame.image.load(path.join('objects', 'playerShip1_orange.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_image = pygame.image.load(path.join('objects', 'laserRed16.png')).convert()
missile_image= pygame.image.load(path.join('objects', 'missile.png')).convert_alpha()

#making array of meteor sizes
meteor_images = []
meteor_list = [
    'meteorBrown_big1.png',
    'meteorBrown_big2.png', 
    'meteorBrown_med1.png', 
    'meteorBrown_med3.png',
    'meteorBrown_small1.png',
    'meteorBrown_small2.png',
    'meteorBrown_tiny1.png'
]

for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join('objects', image)).convert())

#meteor explosion animations
explosion_animation = {}
explosion_animation['big'] = []
explosion_animation['small'] = []
explosion_animation['play'] = []

for i in range(9):
    temp = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join('objects', temp)).convert()
    img.set_colorkey(BLACK)

    #resizing the explosion
    img_large = pygame.transform.scale(img, (75, 75))
    explosion_animation['big'].append(img_large)
    img_small = pygame.transform.scale(img, (32, 32))
    explosion_animation['small'].append(img_small)

    #player death exposion
    temp2 = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join('objects', temp2)).convert()
    img.set_colorkey(BLACK)
    explosion_animation['play'].append(img)



player_die_sound = pygame.mixer.Sound(path.join('sounds', 'rumble1.ogg'))


#load all the game sounds
shooting_sound = pygame.mixer.Sound(path.join('sounds', 'pew.wav'))
missile_sound = pygame.mixer.Sound(path.join('sounds', 'rocket.ogg'))
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join('sounds', sound)))


#power ups
powerup_image = {}
powerup_image['shield'] = pygame.image.load(path.join('objects', 'shield_gold.png')).convert()
powerup_image['levelup'] = pygame.image.load(path.join('objects', 'bolt_gold.png')).convert()




#setting music volume
pygame.mixer.music.set_volume(0.3)

#main game loop
run = True
display_start = True
highscore = 0
newhighscore = False
Game_Over = False
Level = 1
while run:
    
    if Game_Over:
        anim.game_over(newhighscore, highscore)
        pygame.time.wait(0)
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path.join('sounds', 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
        pygame.mixer.music.play(-1)
        Game_Over = False
        display_start = True
        
    if display_start:
        anim.main_menu()
        pygame.time.wait(3000)

        #Stop menu music
        pygame.mixer.music.stop()
        
        #Play the gameplay music in an endless loop
        pygame.mixer.music.load(path.join('sounds', 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
        pygame.mixer.music.play(-1)
        display_start = False
        
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        
        # group all sprites together for ease of access
        sprites = pygame.sprite.Group()
        player = ply.Player(sprites, bullets)
        #player.update_Overheat(ovrht)
        sprites.add(player)

        #spawn some asteroids
        asteroids = pygame.sprite.Group()
        for i in range(8):      ## 8 asteroids
            #pass the allsprites group into the asteroids module
            ast.newobject(sprites,asteroids)


        #score variable keeps track of the score
        score = 0
        newhighscore = False
        Level = 1
    #processing events
    clock.tick(FPS)
    #gets all the events which have occured till now and keeps tab of them.
    for event in pygame.event.get():
        
        #Closes when X button is pressed
        if event.type == pygame.QUIT:
            run = False

        ##Closes when esc is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        
    #update the sprites
    sprites.update()

    #check hitboxes to see which asteroids to destroy
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    

    #asteroids will spawn again once they are killed, to keep a constant number of asteroids on screen
    for hit in hits:
        #different amount of points are given for hitting different size asteroids
        if not player.get_hide():
            score += 64 - hit.radius         
        random.choice(expl_sounds).play()

        expl = des.Destroy(hit.rect.center, 'big')
        sprites.add(expl)
        if random.random() > 0.9:
            pow = spawns.spawn_powerup(hit.rect.center)
            sprites.add(pow)
            powerups.add(pow)
        ast.newobject(sprites,asteroids)
    if score > highscore:
        highscore = score
        newhighscore = True

    #adds more asteroids past a score of 800, one for every level past 1
    if score > (800 * Level):
        Level+=1
        for i in range(Level):
            ast.newobject(sprites,asteroids)
    #Check if the player was hit by an asteroid
    #Creates a list of which asteroids hit the player
    hits = pygame.sprite.spritecollide(player, asteroids, True, pygame.sprite.collide_circle)

    #Player loses health based on asteroid size
    for hit in hits:
        player.update_Health(-hit.radius * 2)
        expl = des.Destroy(hit.rect.center, 'small')
        sprites.add(expl)
        ast.newobject(sprites,asteroids)
    
        #Death routine
    if player.get_Health() <= 0: 
            player_die_sound.play()
            death_explosion = des.Destroy(player.rect.center, 'play')
            sprites.add(death_explosion)

            player.die()


            #hide.hide(player.get_Rect())
            #player.update_hide(hide)
            #player.update_Lives(-1)
            #player.health = 100
            #player.reset_Health()
            #ovrht.reset_Overheat()
            #ovrht.cool()
            #player.update_Overheat(ovrht)

    #print(len(asteroids.sprites()))

    ##When hitting a powerup
    contact = pygame.sprite.spritecollide(player, powerups, True)
    for types in contact:
        if types.type == 'shield':
            shield = random.randrange(10, 30)
            player.update_Health(shield)
            if player.get_Health() >= 100:
                player.reset_Health()
        if types.type == 'levelup':
            player.ability()

    ##If the player is dead and the animation is finished, restart the game
    if player.get_Lives() == 0 and not death_explosion.alive():
        Game_Over = True

    #Draw the background image
    screen.blit(background, background_rect)

    #Drawing the health and overheat bars along with sprites
    sprites.draw(screen)
    anim.put_text(screen, "score: " + str(score), 18, WIDTH / 2, 10)     ## 10px down from the screen
    anim.put_text(screen, "highscore: " + str(highscore), 18, WIDTH / 2, 30)     ## 10px down from the screen
    anim.put_text(screen, "Level: " + str(Level), 30, 155, 0)
    anim.put_health_bar(screen, 5, 5, player.get_Health())
    anim.put_overheat_bar(screen, 5, 20, player.get_Overheat())

    #Drawing Lives
    anim.put_lives(screen, WIDTH - 100, 5, player.get_Lives(), player_mini_img)
    pygame.display.flip()       

pygame.quit()

