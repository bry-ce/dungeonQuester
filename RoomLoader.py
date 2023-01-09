import pygame, math
from Tile import *
from SpriteSheet import *
from Door import *
from outdoorTile import *
def loadOutdoor(room):
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
            if c == "_":
                pass
            elif c == "g":
                tiles += [outdoorTile('grass', [x*size, y*size])]
            elif c == 'f':
                tiles += [outdoorTile('f', [x*size, y*size])]
            elif c == 'p':
                tiles += [outdoorTile('p', [x*size, y*size])]
    return tiles
        
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
            if c == "_":
                pass
            elif c == "+":
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
            elif c == "b":
                tiles += [Tile("BS", [x*size, y*size])]
            elif c == "a":
                tiles += [Tile("AS", [(x*size)+7, (y*size)+20])]
            elif c == "p":
                tiles += [Tile("BAR", [x*size, y*size])]
            elif c == "c":
                tiles += [Tile("CARPET", [(x*size)-6, y*size])]
            elif c == "h":
                tiles += [Tile("CHAIR_LEFT", [x*size, y*size])]
            elif c == "j":
                tiles += [Tile("CHAIR_RIGHT", [(x*size)-16, y*size])]
            elif c == "d":
                tiles += [Tile("CHAIR_DOWN", [(x*size) + 16, (y*size) - 10])]
            elif c == "u":
                tiles += [Tile("CHAIR_UP", [(x*size) + 16, (y*size)])]
            elif c == "t":
                tiles += [Tile("TABLE", [x*size, y*size])]
            elif c == "m":
                tiles += [Tile("MUG", [x*size, y*size])]
    return tiles

def loadDoors(room):
    f = open(room, 'r')
    lines = f.readlines()
    f.close

    size = 48
    doors = []

    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if  c != "\n":
                newline += c
            newLines += [newline]


    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "s":
                doors += [Door(1, [x*size, y*size], 1)]
            if c == "x":
                doors += [Door(1, [x*size, y*size], -1)]
            else: pass
    return doors