from pygame import *
from SpriteSheet import *

class outdoorTile():
    def __init__(self, kind, pos) -> None:
        self.ss = SpriteSheet(pygame.image.load("tiles/outdoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 10, (0,0,0))
        self.pos = pos

        if kind == 'grass':
            self.img = self.ss.get_static_image(32, 32, 288, 128, 320, 160, 2, (0,0,0))
        elif kind == 'p':
            self.img = self.ss.get_static_image(32,32, )
        elif kind == 'f':
            self.img = self.ss.get_static_image(24, 16, 220, 112, 242, 128, 3, (0,0,0) )
        


        self.rect = self.img.get_rect()