import pygame, sys
from  SpriteSheet import *
from pygame.locals import *
from Player import *
from Button import *
from DrawTools import *
from StartScreen import *

pygame.init()
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

BG = (50, 50, 50)
BLACK =(0, 0, 0)
character_speed_x= 8
character_speed_y= 8

current_time = pygame.time.get_ticks()

direction = "up"

main_player = Player(1, 4)
gui = Gui()
start_screen_picker = gui.gui_sprite_sheet.get_static_image(310, 80, 0, 110, 310, 190, 1, BLACK)


last_update = pygame.time.get_ticks()
player_animation_cooldown = 100
frame = 0

start = True

while True:
    for event in pygame.event.get():

        main_player.current_time = pygame.time.get_ticks()
        pygame.key.set_repeat(75, main_player.player_animation_cooldown)
        mousepos = pygame.mouse.get_pos()

        #event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                    

        #handles movement while using current key press.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                main_player.go("up")
                main_player.update_frame()
            elif event.key == pygame.K_a:
                main_player.go("left")
                main_player.update_frame()
            elif event.key == pygame.K_s:
                main_player.go("down")
                main_player.update_frame()
            elif event.key == pygame.K_d:
                main_player.go("right")
                main_player.update_frame()
            elif event.key == pygame.K_SPACE:
                if main_player.weapon_out == False:
                    main_player.weapon_out = True
                elif main_player.weapon_out == True:
                    main_player.weapon_out = False
        elif event.type == pygame.KEYUP:
            if event.key == K_w:
                main_player.stop()
            elif event.key == K_a:
                main_player.stop()
            elif event.key == K_s:
                main_player.stop()
            elif event.key == K_d:
                main_player.stop()


        #draws player to screen based on direction, and handles animations
        screen.fill(BG)
        blitSprite(screen, main_player)
        screen.blit(start_screen_picker, (310,720))
        pygame.display.update()
        clock.tick(60)
