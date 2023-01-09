from pygame import *
from math import *

class Skill():
    def __init__(self, attribute) -> None:

        self.requirements = {
            1: 50,
            2: 80,
            3: 100,
            4: 150,
            5: 200,
            6: 250,
            7: 300,
            8: 370,
            9: 450,
            10: 500
        }    

        self.lvl = 0
        self.currentXp = 0
        self.nextLvlXp = self.requirements
        
        