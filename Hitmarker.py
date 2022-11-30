from pygame import *
from DrawTools import *
from SpriteSheet import *

class Hitmarker():

    def __init__(self, scale):
        self.img = pygame.image.load("dungeonQuester\slashmarks\slash.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (scale, scale))
        self.rect = self.img.get_rect()

    def slash(self):
        self.rect = pygame.mouse.get_pos()
        