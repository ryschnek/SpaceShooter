import pygame
from os import path
import constants as con

def main_menu():
    global screen
    menu_song = pygame.mixer.music.load(path.join(con.sounds, "menu.ogg"))
    pygame.mixer.music.play(-1)
    main = pygame.image.load(path.join('objects', 'main2.png')).convert()
    main = pygame.transform.scale(main, (con.WIDTH, con.HEIGHT), con.screen)
    con.screen.blit(main, (0,0))
    pygame.display.update()

    while 1:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            put_text(con.screen, "Press ENTER To Start", 50, 550, 280)
            put_text(con.screen, "Q To Close To Desktop", 50, 550, 280+60)
            pygame.display.update()
            
    ready = pygame.mixer.Sound(path.join(con.sounds,'getready.ogg'))
    ready.play()
    con.screen.fill(con.BLUE)
    put_text(con.screen, "GET READY", 40, con.WIDTH/2, con.HEIGHT/2)
    pygame.display.update()

def game_over(newhighscore, highscore):
    global screen
    menu_song = pygame.mixer.music.load(path.join(con.sounds, "menu.ogg"))
    pygame.mixer.music.play(-1)
    main = pygame.image.load(path.join('objects', 'black.png')).convert()
    main = pygame.transform.scale(main, (con.WIDTH, con.HEIGHT), con.screen)
    con.screen.blit(main, (0,0))
    pygame.display.update()
    
    while 1:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            put_text(con.screen, "GAME OVER!", 60, con.WIDTH / 2, con.HEIGHT/4)
            put_text(con.screen, "Press R to Return to Menu", 60, con.WIDTH/2, con.HEIGHT/4 + 60)
            if newhighscore:
                put_text(con.screen, "New High Score: " + str(highscore), 60, con.WIDTH/2, con.HEIGHT/4 + 120)
            pygame.display.update()
            
def put_health_bar(surf, x, y, pct):
    pct = max(pct, 0) 
    fill = (pct / 100) * con.HEALTH_LENGTH 
    outline_rect = pygame.Rect(x, y, con.HEALTH_LENGTH, con.HEALTH_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, con.HEALTH_HEIGHT)
    pygame.draw.rect(surf, con.GREEN, fill_rect)
    pygame.draw.rect(surf, con.WHITE, outline_rect, 2)

def put_overheat_bar(surf, x, y, pct):
    pct = max(pct, 0)
    fill = (pct / 100) * con.OVERHEAT_LENGTH
    outline_rect = pygame.Rect(x, y, con.OVERHEAT_LENGTH, con.OVERHEAT_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, con.HEALTH_HEIGHT)
    pygame.draw.rect(surf, con.RED, fill_rect)
    pygame.draw.rect(surf, con.WHITE, outline_rect, 2)

def put_text(surf, text, size, x, y):
    font = pygame.font.Font(con.font_name, size)
    text_surface = font.render(text, True, con.WHITE) 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def put_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
