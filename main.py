import pygame, sys
from  SpriteSheet import *
from pygame.locals import *
from Player import *

pygame.init()
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

BG = (50, 50, 50)
BLACK =(0, 0, 0)
character_speed_x= 8
character_speed_y= 8


direction = 2

main_player = Player('robe', 8, 8)

#character_start = sprite_sheet.get_image(64, 64, 2, BLACK, 3, 0)

last_update = pygame.time.get_ticks()
player_animation_cooldown = 75
frame = 0



while True:
    for event in pygame.event.get():

        main_player.current_time = pygame.time.get_ticks()
        
        #event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

        #handles movement while using current key press.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                main_player.move_player("up")
            elif event.key == pygame.K_a:
                main_player.move_player("left")
            elif event.key == pygame.K_s:
                main_player.move_player("down")
            elif event.key == pygame.K_d:
                main_player.move_player("right")
        
        #on movement key release player faces forwards at frame zero
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                frame = 0
            elif event.key == K_a:
                frame = 0
            elif event.key == K_s:
                frame = 0
            elif event.key == K_d:
                frame = 0

        #draws player to screen based on direction, and handles animations
        screen.fill(BG)

        if direction == 0:
            screen.blit(main_player.up_animation_list[frame], (main_player.character_x_pos, main_player.character_y_pos))
        elif direction == 1:
            screen.blit(main_player.left_animation_list[frame], (main_player.character_x_pos, main_player.character_y_pos))
        elif direction == 2:
            screen.blit(main_player.down_animation_list[frame], (main_player.character_x_pos, main_player.character_y_pos))
        elif direction == 3:
            screen.blit(main_player.right_animation_list[frame], (main_player.character_x_pos, main_player.character_y_pos))
        
        pygame.display.update()
        clock.tick(240)
