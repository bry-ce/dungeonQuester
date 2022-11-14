from SpriteSheet import *
import pygame
from Player import *
from Gui import *

class Button:

    def __init__(self, x, y, img) -> None: 
        self.x = x
        self.y = y
        self.image = img