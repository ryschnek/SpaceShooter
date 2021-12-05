import pygame
from os import path
import spawns
import constants as con

class Player(pygame.sprite.Sprite):
    
    def __init__(self, sprites, bullets):
        pygame.sprite.Sprite.__init__(self)
        ## scale the player img down
        self.image = pygame.transform.scale(con.player_img, (50, 38))
        self.image.set_colorkey(con.BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = con.WIDTH / 2
        self.rect.bottom = con.HEIGHT - 10
        self.speed_x = 0
        self.hot = False
        self.health = 100
        self.overheat = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()
        self.space_down = False
        self.sprites = sprites
        self.bullets = bullets

    def update(self):
        ## time out for bulletups
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > con.poweruptime:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        ## unhide 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = con.WIDTH / 2
            self.rect.bottom = con.HEIGHT - 30

        self.speed_x = 0     ## makes the player static in the screen by default. 
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 

        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()
        mousestate = pygame.mouse.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        elif keystate[pygame.K_RIGHT]:
            self.speed_x = 5

        if self.hot:
            self.overheat -= 1
            if self.overheat == 0:
                self.hot = False
        elif mousestate[0]:
            if not self.space_down and self.overheat < 90 and not self.hidden:
                self.shoot()
                self.space_down = True
                self.overheat += 20
                if self.overheat > 90:
                    self.hot = True
        elif not mousestate[0]:
                self.space_down = False
                if self.overheat != 0:
                    self.overheat -= 1
                    if self.overheat == 0:
                        self.hot = False

        
        #if keystate[pygame.K_SPACE]:
        #    if not self.space_down:
        #       self.shoot()
        #       self.space_down = True
        #elif not keystate[pygame.K_SPACE]:
        #    self.space_down = False
                
        ## check for the borders at the left and right
        if self.rect.right > con.WIDTH:
            self.rect.right = con.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speed_x

    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = spawns.spawn_bullet(self.rect.centerx, self.rect.top)
                self.sprites.add(bullet)
                self.bullets.add(bullet)
                
            if self.power == 2:
                bullet1 = spawns.spawn_bullet(self.rect.left, self.rect.centery)
                bullet2 = spawns.spawn_bullet(self.rect.right, self.rect.centery)
                self.sprites.add(bullet1)
                self.sprites.add(bullet2)
                self.bullets.add(bullet1)
                self.bullets.add(bullet2)
                
            if self.power >= 3:
                bullet1 = spawns.spawn_bullet(self.rect.left, self.rect.centery)
                bullet2 = spawns.spawn_bullet(self.rect.right, self.rect.centery)
                missile1 = spawns.spawn_missile(self.rect.centerx, self.rect.top) # spawn_missile shoots from center of ship
                self.sprites.add(bullet1)
                self.sprites.add(bullet2)
                self.sprites.add(missile1)
                self.bullets.add(bullet1)
                self.bullets.add(bullet2)
                self.bullets.add(missile1)
                #shooting_sound.play()
                #missile_sound.play()

            if self.power >= 4:
                missile1 = spawns.spawn_missile(self.rect.left, self.rect.centery) # spawn_missile shoots from center of ship
                missile2 = spawns.spawn_missile(self.rect.right, self.rect.centery) # spawn_missile shoots from center of ship
                missile3 = spawns.spawn_missile(self.rect.centerx, self.rect.top) # spawn_missile shoots from center of ship
                self.sprites.add(missile1)
                self.sprites.add(missile2)
                self.sprites.add(missile3)
                self.bullets.add(missile1)
                self.bullets.add(missile2)
                self.bullets.add(missile3)
                #shooting_sound.play()
                #missile_sound.play()


    def ability(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (con.WIDTH / 2, con.HEIGHT + 200)
