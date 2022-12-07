import pygame, math
from Tile import *
from SpriteSheet import *
from Door import *

def loadRoom(room):
    f = open(room, 'r')
    lines = f.readlines()
    f.close

    size = 48
    tiles =[]

    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if  c != "\n":
                newline += c
            newLines += [newline]

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "+":
                tiles += [Tile("Floor", [x*size, y*size])]
            elif c == "-":
                tiles += [Tile("T_Wall", [x*size, y*size])]
            elif c == "{":
                tiles += [Tile("TL_corner", [x*size, y*size])]
            elif c == "}":
                tiles += [Tile("TR_corner", [x*size, y*size])]
            elif c == ":":
                tiles += [Tile("L_Wall", [x*size, y*size])]
            elif c == ";":
                tiles += [Tile("R_Wall", [x*size, y*size])]
            
    return tiles
    
    lines = newLines