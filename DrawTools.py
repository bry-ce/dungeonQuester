
from SpriteSheet import *

BLACK = (0, 0, 0)

def idleStance(player):
    player.up_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 0, 0)]
    player.left_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 1, 0)]
    player.down_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 2, 0)]
    player.right_idle_stance = [player.character_body_sprite_sheet.get_image(64, 64, 2, BLACK, 3, 0)]

def characterAnimations(player):

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

def attackAnimations(player):
    player.up_attack_list = []
    player.up_attack_frames = 9
    
    for i in range(player.up_attack_frames):
        player.up_attack_list.append(player.character_attack_sprite_sheet.get_image(64, 64, 2, BLACK, 0, i))

    player.down_attack_list = []
    player.down_attack_frames = 9

    for i in range(player.down_attack_frames):
        player.down_attack_list.append(player.character_attack_sprite_sheet.get_image(64, 64, 2, BLACK, 2, i))

    player.left_attack_list = []
    player.left_attack_frames = 9

    for i in range(player.left_attack_frames):
        player.left_attack_list.append(player.character_attack_sprite_sheet.get_image(64, 64, 2, BLACK, 1, i))

    player.right_attack_list = []
    player.right_attack_frames = 9

    for i in range(player.right_attack_frames):
        player.right_attack_list.append(player.character_attack_sprite_sheet.get_image(64, 64, 2, BLACK, 3, i))


def fade_object(img):
    for i in range(255):
        img.set_alpha(255-i)
        