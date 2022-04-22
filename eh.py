import pygame
import random
from pygame.locals import *

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

class Square(pygame.sprite.Sprite):
    def __init__(self, width, height, speed, left_right_boolean):
        super().__init__()
        self.left_right_boolean = left_right_boolean
        self.color = (0,255,0)
        self.speed = speed
        self.height = height
        self.width = width
        self.image = pygame.Surface([width, height])
        self.image.fill(green)
        self.image.set_colorkey(green)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0,255,0), [0,0,width,height])
        self.rect = self.image.get_rect()

        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    
    def moveDown(self, pixels):
        self.rect.y += pixels
    
    def moveRight(self, pixels):
        self.rect.x += pixels
    
    def moveUp(self, pixels):
        self.rect.y -= pixels
    
    def spawn(self, x, y):
        self.rect.x = x
        self.rect.y = y

resolution = (1900,1200)
flags = FULLSCREEN | DOUBLEBUF | HWSURFACE
screen = pygame.display.set_mode(resolution, flags, display=1)
pygame.display.set_caption("simmy")
clock = pygame.time.Clock()

cell = Square(50, 50, 5, True)
cell.rect.x = 100
cell.rect.y = 100
cellgroup = pygame.sprite.Group()
cellgroup.add(cell)

running = True
cell_list = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                print(cell_list)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousepos = pygame.mouse.get_pos()
                x = mousepos[0]
                y = mousepos[1]
                cell_list.append([x, y])
    
    for cells in cell_list:
        cell = Square(50, 50, 5, True)
        cell.rect.x = cells[0]
        cell.rect.y = cells[1]
        cellgroup.add(cell)
    cellgroup.update()
    cellgroup.draw(screen)
    pygame.display.flip()
    clock.tick(60)