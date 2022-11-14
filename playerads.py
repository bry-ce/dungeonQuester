from spritesheet import *
from main import *
import pygame

BG = (50, 50, 50)
BLACK =(0, 0, 0)

current_time = pygame.time.get_ticks()

class Player():


    def __init__(self, clothing, speedx, speedy):
        self.clothing = clothing
        self.speedx = speedx
        self.speedy = speedy

        
        
        if self.clothing == 'chain':
            self.character_hands_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/HANDS_plate_armor_gloves.png").convert_alpha())
        elif self.clothing == 'plate':
            pass
        elif self.colthing == 'robe':
            self.character_head_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/HEAD_robe_hood.png").convert_alpha())
            self.character_belt_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/BELT_rope.png").convert_alpha())
            self.character_torso_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/TORSO_robe_shirt_brown.png").convert_alpha())
            self.character_legs_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/LEGS_robe_skirt.png").convert_alpha())
            self.character_feet_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/FEET_shoes_brown.png").convert_alpha())
            self.character_body_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/BODY_male.png").convert_alpha())

        self.last_update = pygame.time.get_ticks()
        self.player_animation_cooldown = 75
        self.frame = 0

        self.up_animation_list = []
        self.up_animation_frames = 9

        for i in range(self.up_animation_frames):
            self.up_animation_list.append(self.character_body_sprite_sheet.get_image(64, 64, 1.6, BLACK, 0, i))

        self.down_animation_list = []
        self.down_animation_frames = 9

        for i in range(self.down_animation_frames):
            self.down_animation_list.append(self.character_body_sprite_sheet.get_image(64, 64, 1.6, BLACK, 2, i))

        self.left_animation_list = []
        self.left_animation_frames = 9

        for i in range(self.left_animation_frames):
            self.left_animation_list.append(self.character_body_sprite_sheet.get_image(64, 64, 1.6, BLACK, 1, i))

        self.right_animation_list = []
        self.right_animation_frames = 9

        for i in range(self.right_animation_frames):
            self.right_animation_list.append(self.character_body_sprite_sheet.get_image(64, 64, 1.6, BLACK, 3, i))

    
    def get_armor(self, clothing):
        if self.clothing == 'chain':
            pass
        elif self.clothing == 'plate':
            pass
        elif self.colthing == 'robe':
            pass
    
    def move_player(self, direction, animationlist, x, y):
        if current_time - self.last_update >= self.player_animation_cooldown:
                self.frame += 1

                self.last_update = current_time
        if self.frame >= len(main_player.up_animation_list):
                self.frame = 0
    
    def set_animation_list(self, direction, frame):
        pass
    
    
    