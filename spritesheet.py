import pygame, sys

class SpriteSheet():
    
    def __init__(self, image):
        self.sheet = image
        
    

    def get_image(self, width, height, scale, color, direction, frame):
        image = pygame.Surface((width, height)).convert_alpha()

        #frames are considered x posistion inside image
        #direction is considered y position inside image
        #up = 0, left = 1, down = 2, right = 3
        #frames and directions are zero indexed

        image.blit(self.sheet, (0,0), (64 * frame, 64 * direction, (frame+1) * 64, (direction+1)*64))

        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        
        return image
