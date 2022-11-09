from heapq import heappush
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



character_start = sprite_sheet.get_image(64, 64, 2, BLACK, 3, 0)

while True:
    for event in pygame.event.get():
        
        #fills background
        screen.fill(BG)
        
        #displays character
        screen.blit(character_start, (0,0))

        #event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
 

        


        pygame.display.update()
        clock.tick(60)