from SpriteSheet import *
import pygame
from Button import *

class Gui():

    def __init__(self) -> None:
        self.gui_sprite_sheet = SpriteSheet(pygame.image.load('gui_sprites/RPG_GUI_v1.png'))
        self.status = 'closed'
        
        
    def open(self):
        self.status = 'opened'

    def close(self):
        self.status = 'closed'