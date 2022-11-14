from SpriteSheet import *
from Gui import *
from Button import *

class StartScreen():

    def __init__(self):
        self.gui = Gui()
        self.gui.gui_sprite_sheet.get_static_image(310, 80, 0, 110, 310, 190, 1, BLACK)
