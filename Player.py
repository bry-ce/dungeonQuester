from SpriteSheet import *
import pygame

BG = (50, 50, 50)
BLACK =(0, 0, 0)



class Player():

    def __init__(self, clothing, maxSpeed):
        self.clothing = clothing
        self.speedx = 0
        self.speedy = 0
        self.maxSpeed = maxSpeed

        self.character_x_pos = 436
        self.character_y_pos = 336
        
        if self.clothing == 'chain':
            self.character_hands_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/HANDS_plate_armor_gloves.png").convert_alpha())
        elif self.clothing == 'plate':
            pass
        elif self.clothing == 'robe':
            self.character_head_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/HEAD_robe_hood.png").convert_alpha())
            self.character_belt_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/BELT_rope.png").convert_alpha())
            self.character_torso_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/TORSO_robe_shirt_brown.png").convert_alpha())
            self.character_legs_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/LEGS_robe_skirt.png").convert_alpha())
            self.character_feet_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/FEET_shoes_brown.png").convert_alpha())
            self.character_body_sprite_sheet = SpriteSheet(pygame.image.load("dungeonQuester/lpc_entry/png/walkcycle/BODY_male.png").convert_alpha())


        self.current_time = pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
        self.player_animation_cooldown = 75
        self.frame = 0

        self.direction = "down"

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
    
    def move_player(self):
            if self.current_time - self.last_update >= self.player_animation_cooldown:
                self.frame += 1
                self.character_y_pos -= self.speedy
                self.last_update = self.current_time
            if self.frame >= len(self.images):
                self.frame = 0
        if self.direction == "left":
            if self.current_time - self.last_update >= self.player_animation_cooldown:
                self.frame += 1
                self.character_x_pos -= self.speedx
                self.last_update = self.current_time
            if self.frame >= len(self.left_animation_list):
                self.frame = 0
        if self.direction == "right":
            if self.current_time - self.last_update >= self.player_animation_cooldown:
                self.frame += 1
                self.character_x_pos += self.speedx
                self.last_update = self.current_time
            if self.frame >= len(self.right_animation_list):
                self.frame = 0
        if self.direction == "down":
            if self.current_time - self.last_update >= self.player_animation_cooldown:
                self.frame += 1
                self.character_y_pos += self.speedy
                self.last_update = self.current_time
            if self.frame >= len(self.down_animation_list):
                self.frame = 0

        def go(self, direction):
            self.direction = direction
             if self.direction == "up":
                self.speedy = self.maxSpeed
                self.images = self.self.up_animation_list
                