from pygame import *
from SpriteSheet import *

class Door():
    def __init__(self, kind):
        self.ss = SpriteSheet(pygame.image.load("dungeonQuester/tiles\indoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 80, 97, 96, 112, 2, (0,0,0))
        self.rect = self.img.get_rect()

        if kind == 1:
            self.img = self.ss.get_static_image(16, 16, 16, 81, 32, 97, 4, (0,0,0))
        elif kind == 2:
            self.img = self.ss.get_static_image(16, 16, 80, 97, 96, 112, 4, (0,0,0))
        else:
            self.img = self.ss.get_static_image(16, 16, 16, 81, 32, 97, 2, (0,0,0))
        
        
    