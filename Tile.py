from pygame import *
from SpriteSheet import *

class Tile():
    def __init__(self, kind, pos) -> None:
        self.ss = SpriteSheet(pygame.image.load("dungeonQuester/tiles\indoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 2, (0,0,0))
        self.rect = self.img.get_rect()
        self.pos = pos

        if kind == "Floor":
            self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 2, (0,0,0))
        elif kind == "T_Wall":
            self.img = self.ss.get_static_image(16, 16, 16, 65, 32, 81, 2, (0,0,0))
        elif kind == "L_Wall":
            self.img = self.ss.get_static_image(16, 16, 0, 81, 16, 97, 2, (0,0,0))
        elif kind == "R_Wall":
            self.img = self.ss.get_static_image(16, 16, 32, 81, 48, 97, 2, (0,0,0))
        elif kind == "TL_corner":
            self.img = self.ss.get_static_image(16, 16, 0, 65, 16, 81, 2, (0,0,0))
        elif kind == "TR_corner":
            self.img = self.ss.get_static_image(16, 16, 32, 65, 48, 81, 2, (0,0,0))
