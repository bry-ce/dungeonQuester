from xml.dom.minidom import CharacterData
import pygame, sys
import spritesheet
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

character_body_sprite_sheet = pygame.image.load(r"C:\Users\bwime\vscode\python\dungeon_game\lpc_entry\png\walkcycle\BODY_male.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(character_body_sprite_sheet)

BG = (50, 50, 50)
BLACK =(0, 0, 0)
character_speed_x= 8
character_speed_y= 8

character_x_pos = 436
character_y_pos = 336
direction = 2

#character_start = sprite_sheet.get_image(64, 64, 2, BLACK, 3, 0)

last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0


up_animation_list = []
up_animation_frames = 9

for i in range(up_animation_frames):
    up_animation_list.append(sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

down_animation_list = []
down_animation_frames = 9

for i in range(down_animation_frames):
    down_animation_list.append(sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

left_animation_list = []
left_animation_frames = 9

for i in range(left_animation_frames):
    left_animation_list.append(sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

right_animation_list = []
right_animation_frames = 9

for i in range(right_animation_frames):
    right_animation_list.append(sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        #fills background
        screen.fill(BG)
        #update character animation
        current_time = pygame.time.get_ticks()
        
        

        #event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

        #handles movement while using current key press.
        if keys[pygame.K_w]:
            direction = 0
            if current_time - last_update >= animation_cooldown:
                frame += 1
                character_y_pos -= character_speed_y
                last_update = current_time
            if frame >= len(up_animation_list):
                frame = 0
        elif keys[pygame.K_a]:
            direction = 1
            if current_time - last_update >= animation_cooldown:
                frame += 1
                character_x_pos -= character_speed_x
                last_update = current_time
            if frame >= len(left_animation_list):
                frame = 0
        elif keys[pygame.K_d]:
            direction = 3
            if current_time - last_update >= animation_cooldown:
                frame += 1
                character_x_pos += character_speed_x
                last_update = current_time
            if frame >= len(right_animation_list):
                frame = 0
        elif keys[pygame.K_s]:
            direction = 2
            if current_time - last_update >= animation_cooldown:
                frame += 1
                character_y_pos += character_speed_y
                last_update = current_time
            if frame >= len(down_animation_list):
                frame = 0
        
        #on movement key release player faces forwards at frame zero
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                frame = 0
                direction = 2
            elif event.key == K_a:
                frame = 0
                direction = 2
            elif event.key == K_s:
                frame = 0
                direction = 2
            elif event.key == K_d:
                frame = 0
                direction = 2

        if direction == 0:
            screen.blit(up_animation_list[frame], (character_x_pos, character_y_pos))
        elif direction == 1:
            screen.blit(left_animation_list[frame], (character_x_pos, character_y_pos))
        elif direction == 2:
            screen.blit(down_animation_list[frame], (character_x_pos, character_y_pos))
        elif direction == 3:
            screen.blit(right_animation_list[frame], (character_x_pos, character_y_pos))
        
        pygame.display.update()
        clock.tick(240)