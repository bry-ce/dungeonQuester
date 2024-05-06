from pygame import *
from SpriteSheet import *

class Tile():
    def __init__(self, kind, pos) -> None:
<<<<<<< HEAD
        self.ss = SpriteSheet(pygame.image.load("tiles/indoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 10, (0,0,0))
=======
        self.ss = SpriteSheet(pygame.image.load("tiles\indoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 10, (0,0,0))
        self.rect = self.img.get_rect()
>>>>>>> 84c4757 (commit)
        self.pos = pos

        if kind == "Floor":
            self.img = self.ss.get_static_image(16, 16, 96, 1, 112, 17, 3, (0,0,0))
        elif kind == "T_Wall":
            self.img = self.ss.get_static_image(16, 16, 16, 65, 32, 81, 3, (0,0,0))
        elif kind == "L_Wall":
            self.img = self.ss.get_static_image(16, 16, 0, 81, 16, 97, 3, (0,0,0))
        elif kind == "R_Wall":
            self.img = self.ss.get_static_image(16, 16, 32, 81, 48, 97, 3, (0,0,0))
        elif kind == "TL_corner":
            self.img = self.ss.get_static_image(16, 16, 0, 65, 16, 81, 3, (0,0,0))
        elif kind == "TR_corner":
            self.img = self.ss.get_static_image(16, 16, 32, 65, 48, 81, 3, (0,0,0))
        elif kind == "BS":
            self.img = self.ss.get_static_image(20, 27, 54, 100, 74, 127, 4, (0,0,0))
        elif kind == "AS":
<<<<<<< HEAD
            self.img = self.ss.get_static_image(16, 21, 48, 76, 64, 97, 4, (0,0,0))
        elif kind == "BAR":
            self.img = self.ss.get_static_image(80, 52, 0, 139, 80, 191, 5, (0,0,0))
        elif kind == "CARPET":
            self.img = self.ss.get_static_image(48, 28, 0, 3, 48, 31, 3, (0,0,0))
        elif kind == "CHAIR_LEFT":
            self.img = self.ss.get_static_image(11, 22, 50, 43, 61, 65, 4, (0,0,0))
        elif kind == "CHAIR_RIGHT":
            self.img = self.ss.get_static_image(11, 22, 35, 43, 46, 65, 4, (0,0,0))
        elif kind == "TABLE":
            self.img = self.ss.get_static_image(19, 21, 71, 44, 90, 65, 4, (0,0,0))
        elif kind == "MUG":
            self.ss = SpriteSheet(pygame.image.load("tiles/mug.png"))
            self.img = self.ss.get_static_image(16, 16, 0, 0, 16, 16, 4, (0,0,0))
            self.ss = SpriteSheet(pygame.image.load("tiles/indoor_tiles.png"))
        elif kind == "CHAIR_DOWN":
            self.img = self.ss.get_static_image(11, 22, 18, 43, 29, 65, 4, (0,0,0))
        elif kind == "CHAIR_UP":
            self.img = self.ss.get_static_image(11, 17, 3, 48, 14, 65, 4, (0,0,0))
        self.rect = self.img.get_rect()
=======
            self.img = self.ss.get_static_image(16, 21, 48, 76, 64, 97, 4, (0,0,0))
>>>>>>> 84c4757 (commit)
