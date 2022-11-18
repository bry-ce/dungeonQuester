from SpriteSheet import *
from DrawTools import *
import pygame

print("import")
BG = (50, 50, 50)
BLACK =(0, 0, 0)



class Player():
    def __init__(self, clothing, maxSpeed):
        print("player")
        self.clothing = clothing
        
        self.set_clothing(1)
        idleStance(self)
        characterAnimations(self)

        self.speed = [0, 0]
        self.maxSpeed = maxSpeed 
        self.character_pos = (436, 336)

        self.heading = ''
        self.direction = 'sdown'
        self.idling = True
        self.current_time = pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
        self.player_animation_cooldown = 75

        self.weapon_out = False

        self.images = self.down_animation_list
        self.frame = 0
        self.maxFrame = len(self.images)
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(topleft = self.character_pos)

    def update_frame(self):
        print(self.current_time - self.last_update)
        if not (self.idling):
            if self.current_time - self.last_update >= self.player_animation_cooldown:
                self.frame += 1
                print(self.frame, self.maxFrame)
                self.last_update = self.current_time
                if self.frame >= self.maxFrame:
                    self.frame = 0
                self.image = self.images[self.frame]

    def go(self, direction):
        self.direction = direction
        if direction == "up":
            self.speed[1] = -self.maxSpeed
            self.images = self.up_animation_list
            self.idling = False
        elif direction == "down":
            self.speed[1] = self.maxSpeed
            self.images = self.down_animation_list
            self.idling = False
        elif direction == "left":
            self.speed[0] = -self.maxSpeed
            self.images = self.left_animation_list
            self.idling = False
        elif direction == "right":
            self.speed[0] = self.maxSpeed
            self.images = self.right_animation_list
            self.idling = False
        if direction == "sup":
            self.speed[1] = 0
            self.images = self.up_idle_stance
            self.idling = True
        elif direction == "sdown":
            self.speed[1] = 0
            self.images = self.down_idle_stance
            self.idling = True
        elif direction == "sleft":
            self.speed[0] = 0
            self.images = self.left_idle_stance
            self.idling = True
        elif direction == "sright":
            self.speed[0] = 0
            self.images = self.right_idle_stance
            self.idling = True
        
        print(self.images)

        self.frame = 0
        self.maxFrame = len(self.images)
        self.image = self.images[self.frame]
        
    def set_clothing(self, index):
        self.clothing = index
        if self.clothing == 0:
            self.character_head_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/HEAD_chain_armor_helmet.png").convert_alpha())
            self.character_belt_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/BELT_leather.png").convert_alpha())
            self.character_torso_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/TORSO_chain_armor_torso.png").convert_alpha())
            self.character_legs_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/LEGS_plate_armor_pants.png").convert_alpha())
            self.character_feet_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/FEET_shoes_brown.png").convert_alpha())
            self.character_body_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/BODY_male.png").convert_alpha())
        elif self.clothing == 1:
            self.character_body_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry\png\walkcycle\BODY_male_plate.png").convert_alpha())
        elif self.clothing == 2:
            self.character_head_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry\png\walkcycle\HEAD_robe_hood.png").convert_alpha())
            self.character_belt_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/BELT_rope.png").convert_alpha())
            self.character_torso_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/TORSO_robe_shirt_brown.png").convert_alpha())
            self.character_legs_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/LEGS_robe_skirt.png").convert_alpha())
            self.character_feet_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/FEET_shoes_brown.png").convert_alpha())
            self.character_body_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester\lpc_entry/png/walkcycle/BODY_male.png").convert_alpha())

    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.move()
        self.update_frame()
