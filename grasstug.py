import pygame
GREEN = (0,255,0)

class Grass(pygame.sprite.Sprite):
	def __init__ (self, color, width, height, speed):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(GREEN)
		self.image.set_colorkey(GREEN)
		self.width = width
		self.height = height
		self.color = color
		self.speed = speed
		pygame.draw.rect(self.image, color, [0,0,width,height])
		self.rect = self.image.get_rect()
		
	def moveLeft(self, pixels):
		self.rect.x -= pixels
