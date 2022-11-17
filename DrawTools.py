
from SpriteSheet import *

BLACK = (0, 0, 0)

def idleStance(player):
    player.up_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 0, 0)]
    player.left_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 1, 0)]
    player.down_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 2, 0)]
    player.right_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 3, 0)]

def bodyAnimations(player):

    player.up_animation_list = []
    player.up_animation_frames = 9
    
    for i in range(player.up_animation_frames):
        player.up_animation_list.append(player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.down_animation_list = []
    player.down_animation_frames = 9

    for i in range(player.down_animation_frames):
        player.down_animation_list.append(player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.left_animation_list = []
    player.left_animation_frames = 9

    for i in range(player.left_animation_frames):
        player.left_animation_list.append(player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.right_animation_list = []
    player.right_animation_frames = 9

    for i in range(player.right_animation_frames):
        player.right_animation_list.append(player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def headAnimations(player):
    player.head_up_animation_list = []
    player.head_up_animation_frames = 9
    
    for i in range(player.head_up_animation_frames):
        player.head_up_animation_list.append(player.character_head_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.head_down_animation_list = []
    player.head_down_animation_frames = 9

    for i in range(player.head_down_animation_frames):
        player.head_down_animation_list.append(player.character_head_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.head_left_animation_list = []
    player.head_left_animation_frames = 9

    for i in range(player.head_left_animation_frames):
        player.head_left_animation_list.append(player.character_head_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.head_right_animation_list = []
    player.head_right_animation_frames = 9

    for i in range(player.head_right_animation_frames):
        player.head_right_animation_list.append(player.character_head_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def beltAnimations(player):
    player.belt_up_animation_list = []
    player.belt_up_animation_frames = 9
    
    for i in range(player.belt_up_animation_frames):
        player.belt_up_animation_list.append(player.character_belt_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.belt_down_animation_list = []
    player.belt_down_animation_frames = 9

    for i in range(player.belt_down_animation_frames):
        player.belt_down_animation_list.append(player.character_belt_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.belt_left_animation_list = []
    player.belt_left_animation_frames = 9

    for i in range(player.belt_left_animation_frames):
        player.belt_left_animation_list.append(player.character_belt_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.belt_right_animation_list = []
    player.belt_right_animation_frames = 9

    for i in range(player.belt_right_animation_frames):
        player.belt_right_animation_list.append(player.character_belt_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def torsoAnimations(player):
    player.torso_up_animation_list = []
    player.torso_up_animation_frames = 9
    
    for i in range(player.torso_up_animation_frames):
        player.torso_up_animation_list.append(player.character_torso_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.torso_down_animation_list = []
    player.torso_down_animation_frames = 9

    for i in range(player.torso_down_animation_frames):
        player.torso_down_animation_list.append(player.character_torso_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.torso_left_animation_list = []
    player.torso_left_animation_frames = 9

    for i in range(player.torso_left_animation_frames):
        player.torso_left_animation_list.append(player.character_torso_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.torso_right_animation_list = []
    player.torso_right_animation_frames = 9

    for i in range(player.torso_right_animation_frames):
        player.torso_right_animation_list.append(player.character_torso_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def legsAnimations(player):
    player.legs_up_animation_list = []
    player.legs_up_animation_frames = 9
    
    for i in range(player.legs_up_animation_frames):
        player.legs_up_animation_list.append(player.character_legs_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.legs_down_animation_list = []
    player.legs_down_animation_frames = 9

    for i in range(player.legs_down_animation_frames):
        player.legs_down_animation_list.append(player.character_legs_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.legs_left_animation_list = []
    player.legs_left_animation_frames = 9

    for i in range(player.legs_left_animation_frames):
        player.legs_left_animation_list.append(player.character_legs_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.legs_right_animation_list = []
    player.legs_right_animation_frames = 9

    for i in range(player.legs_right_animation_frames):
        player.legs_right_animation_list.append(player.character_legs_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def feetAnimations(player):
    player.feet_up_animation_list = []
    player.feet_up_animation_frames = 9
    
    for i in range(player.feet_up_animation_frames):
        player.feet_up_animation_list.append(player.character_feet_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.feet_down_animation_list = []
    player.feet_down_animation_frames = 9

    for i in range(player.feet_down_animation_frames):
        player.feet_down_animation_list.append(player.character_feet_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.feet_left_animation_list = []
    player.feet_left_animation_frames = 9

    for i in range(player.feet_left_animation_frames):
        player.feet_left_animation_list.append(player.character_feet_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.feet_right_animation_list = []
    player.feet_right_animation_frames = 9

    for i in range(player.feet_right_animation_frames):
        player.feet_right_animation_list.append(player.character_feet_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def armsAnimations(player):
    player.arms_up_animation_list = []
    player.arms_up_animation_frames = 9
    
    for i in range(player.arms_up_animation_frames):
        player.arms_up_animation_list.append(player.character_arms_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.arms_down_animation_list = []
    player.arms_down_animation_frames = 9

    for i in range(player.arms_down_animation_frames):
        player.arms_down_animation_list.append(player.character_arms_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.arms_left_animation_list = []
    player.arms_left_animation_frames = 9

    for i in range(player.arms_left_animation_frames):
        player.arms_left_animation_list.append(player.character_arms_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.arms_right_animation_list = []
    player.arms_right_animation_frames = 9

    for i in range(player.arms_right_animation_frames):
        player.arms_right_animation_list.append(player.character_arms_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def weaponAnimations(player):
    player.weapon_up_animation_list = []
    player.weapon_up_animation_frames = 9
    
    for i in range(player.weapon_up_animation_frames):
        player.weapon_up_animation_list.append(player.character_weapon_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.weapon_down_animation_list = []
    player.weapon_down_animation_frames = 9

    for i in range(player.weapon_down_animation_frames):
        player.weapon_down_animation_list.append(player.character_weapon_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.weapon_left_animation_list = []
    player.weapon_left_animation_frames = 9

    for i in range(player.weapon_left_animation_frames):
        player.weapon_left_animation_list.append(player.character_weapon_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.weapon_right_animation_list = []
    player.weapon_right_animation_frames = 9

    for i in range(player.weapon_right_animation_frames):
        player.weapon_right_animation_list.append(player.character_weapon_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))

def weaponHitAnimations(player):
    pass

def blitSprite(screen, sprite):
    if sprite.direction == "up":
        screen.blit(sprite.up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.feet_up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.legs_up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.torso_up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        if sprite.clothing == 1:
            screen.blit(sprite.arms_up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.belt_up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.head_up_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "left":
        screen.blit(sprite.left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.feet_left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.legs_left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.torso_left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        if sprite.clothing == 1:
            screen.blit(sprite.arms_left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.belt_left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.head_left_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "down":
        screen.blit(sprite.down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.feet_down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.legs_down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.torso_down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        if sprite.clothing == 1:
            screen.blit(sprite.arms_down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.belt_down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.head_down_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "right":
        screen.blit(sprite.right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.feet_right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.legs_right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.torso_right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        if sprite.clothing == 1:
            screen.blit(sprite.arms_right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.belt_right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
        screen.blit(sprite.head_right_animation_list[sprite.frame], (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "sup":
        screen.blit(sprite.up_idle_stance, (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "sleft":
        screen.blit(sprite.left_idle_stance, (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "sdown":
        screen.blit(sprite.down_idle_stance, (sprite.character_x_pos, sprite.character_y_pos))
    elif sprite.direction == "sright":
        screen.blit(sprite.right_idle_stance, (sprite.character_x_pos, sprite.character_y_pos))

