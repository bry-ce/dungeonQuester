from pygame import *
from SpriteSheet import *

class outdoorTile():
    def __init__(self, kind, pos) -> None:
        self.ss = SpriteSheet(pygame.image.load("tiles/outdoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 10, (0,0,0))
        self.pos = pos

        if kind == 'grass':
            self.img = self.ss.get_static_image(32, 32, 288, 128, 320, 160, 2, (0,0,0))
        elif kind == 'f':
            self.img = self.ss.get_static_image(24, 16, 220, 112, 242, 128, 3, (0,0,0))
        elif kind == 'top_path':
            self.img = self.ss.get_static_image(16, 16, 288, 160, 304, 176, 2, (0,0,0))
        elif kind == 'bottom_path':
            self.img = self.ss.get_static_image(16, 16, 288, 112, 304, 128, 2, (0,0,0))
        elif kind == 'left_path':
            self.img = self.ss.get_static_image(16, 16, 272, 128, 288, 144, 2, (0,0,0))
        elif kind == 'right_path':
            self.img = self.ss.get_static_image(16, 16, 320, 128, 336, 144, 2, (0,0,0))
        elif kind == 'br_corner':
            self.img = self.ss.get_static_image(16, 16, 320, 160, 336, 176, 2, (0,0,0))
        elif kind == 'bl_corner':
            self.img = self.ss.get_static_image(16, 16, 272, 160, 288, 176, 2, (0,0,0))
        elif kind == 'tr_corner':
            self.img = self.ss.get_static_image(16, 16, 320, 112, 336, 128, 2, (0,0,0))
        elif kind == 'tl_corner':
            self.img = self.ss.get_static_image(16, 16, 272, 112, 288, 128, 2, (0,0,0))

        self.rect = self.img.get_rect() 