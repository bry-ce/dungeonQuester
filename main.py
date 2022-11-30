import sys

import pygame, math, random
from Button import *
from DrawTools import *
from Player import *
from pygame.locals import *
from SpriteSheet import *
from StartScreen import *
from Hitmarker import *

pygame.init()
screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()

BG = (50, 50, 50)
BLACK =(0, 0, 0)
character_speed_x= 8
character_speed_y= 8
current_time = pygame.time.get_ticks()
hit = False
direction = "up"

main_player = Player(1, 4)

#gui = Gui()
#start_screen_picker = gui.gui_sprite_sheet.get_static_image(310, 80, 0, 110, 310, 190, 1, BLACK)


last_update = pygame.time.get_ticks()
player_animation_cooldown = 200
frame = 0

start = True

while True:
    for event in pygame.event.get():
        
        pressed = pygame.key.get_pressed()
        mousepos = pygame.mouse.get_pos()

        #event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                    
        #handles movement while using current key press.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                main_player.go("up")
            elif event.key == pygame.K_a:
                main_player.go("left")
            elif event.key == pygame.K_s:
                main_player.go("down")
            elif event.key == pygame.K_d:
                main_player.go("right")
        elif event.type == pygame.KEYUP:
            if event.key == K_w:
                main_player.go("sup")
            elif event.key == K_a:
                 main_player.go("sleft")
            elif event.key == K_s:
                 main_player.go("sdown")
            elif event.key == K_d:
                 main_player.go("sright")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                main_player.attack()

                

    main_player.update()

    #draws player to screen based on direction, and handles animations
    screen.fill(BG)
    screen.blit(main_player.image, main_player.rect)

    pygame.display.update() 
    clock.tick(30)
  