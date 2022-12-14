from pygame import *
from SpriteSheet import *

class Door():
    def __init__(self, kind, pos):
        self.ss = SpriteSheet(pygame.image.load("dungeonQuester/tiles\indoor_tiles.png"))
        self.img = self.ss.get_static_image(16, 16, 80, 97, 96, 112, 2, (0,0,0))
        self.rect = self.img.get_rect()
        self.pos = pos 
        
        if kind == 1:
            self.img = self.ss.get_static_image(16, 16, 16, 81, 32, 97, 4, (0,0,0))
            self.rect = self.img.get_rect()
        elif kind == 2:
            self.img = self.ss.get_static_image(16, 16, 80, 97, 96, 112, 4, (0,0,0))
            self.rect = self.img.get_rect()
        else:
            self.img = self.ss.get_static_image(16, 16, 16, 81, 32, 97, 2, (0,0,0))
            self.rect = self.img.get_rect()
        
        
        
    def moveTo(self, player, newpos = (436, 336)):
        if pygame.Rect.colliderect(player.subrect, self.rect):
            player.place(newpos)