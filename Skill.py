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
        self.maxLvl = len(self.requirements)
        self.currentXp = 0
        self.nextLvlXp = self.requirements.get(self.lvl) - self.currentXp
        
    def gainxp(self, amount):
        self.currentXp += amount
        if (self.currentXp >= self.requirements.get(self.lvl)):
            self.lvlUp
            self.currentXp -= self.requirements.get(self.lvl)
        else : pass

    def lvlUp(self):
        if (self.lvl < self.maxLvl):
            self.lvl += 1
        else : pass
