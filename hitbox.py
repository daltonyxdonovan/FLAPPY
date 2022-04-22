import pygame
white = (255, 255, 255)
GREEN = (0,255,0)
BLUE = (100, 100, 255)

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        
        self.color = color
        self.speed = speed
        self.height = height
        self.width = width
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()
        
    def moveForward(self, pixels):
        self.rect.y -= pixels
    
    def moveBackward(self, pixels):
        self.rect.y += pixels
