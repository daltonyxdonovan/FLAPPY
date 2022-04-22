import pygame
import os, sys
import shelve
from pygame.locals import *
from grasstug import Grass
from hitbox import Hitbox
from pipesforbird import Pipewall
from bgmove import BGMove
import time
global counter

clock = pygame.time.Clock()
hicounter = 0
counter = 0
titlerun = True
running = False
pygame.mixer.init(48000, -16, 1, 1024)
pygame.init()
gameon = True
flap_sound = pygame.mixer.Sound("jump.wav")
music_sound = pygame.mixer.Sound("music4.wav")
goal_sound = pygame.mixer.Sound("coin.wav")
myfont = pygame.font.SysFont("monospace", 40, bold=True)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")

def logoimg():
	logof = pygame.image.load("logo.png")
	screen.blit(logof, (x-60, 150))

def title():
	global titlerun
	while titlerun == True:
		d = shelve.open('hiscore.txt')
		d['hiscore'] = hicounter  # the score is read from disk
		d.close()
		counter=0
		grass_movement.rect.x = 0
		grass_movement.rect.y = 650
		greenPipewall.rect.x = 700
		greenPipewall.rect.y = 100
		secondPipewall2.rect.x = 1150
		secondPipewall2.rect.y = 430
				
		screen.fill(BLACK)
		logoimg()
		startscore = myfont.render("HISCORE: " + str(hicounter), 60, (255,255,255))
		startscore_rect = startscore.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		screen.blit(startscore, startscore.get_rect(topleft = screen.get_rect().topleft))
		startthing = myfont.render("PRESS 'ENTER' TO START", 60, (255,255,255))
		startthing_rect = startthing.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		screen.blit(startthing, startthing.get_rect(center = screen.get_rect().center))
		
		pygame.display.flip()
		pygame.display.update()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			d = shelve.open('hiscore.txt')
			d['hiscore'] = hicounter          # thats all, now it is saved on disk.
			d.close()
			running = True
			titlerun = False
			
		if keys[pygame.K_ESCAPE]:
			d = shelve.open('hiscore.txt')
			d['hiscore'] = hicounter          # thats all, now it is saved on disk.
			d.close()
			exit()
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				d = shelve.open('hiscore.txt')
				d['hiscore'] = hicounter          # thats all, now it is saved on disk.
				d.close()
				exit()
	
def background(x, y):
	bg = pygame.image.load("pattern.png")
	screen.blit(bg, (x, y))

def flapnoise():
	pygame.mixer.Sound.play(flap_sound)
	
def player(x, y):
	playerimg = pygame.image.load('birdo3.png').convert_alpha()
	screen.blit(playerimg, ((playerHitbox.rect.x-70), (playerHitbox.rect.y-70)))
	
def goalnoise():
	pygame.mixer.Sound.play(goal_sound)
	
def toppipe_img(x, y):
	tp_img = pygame.image.load('toppipe2.png').convert_alpha()
	tp2_img = pygame.image.load('bottompipe2.png').convert_alpha()
	screen.blit(tp_img, (x, y))
	
def bottompipe_img(x, y):
	bt_img = pygame.image.load('bottompipe2.png').convert_alpha()
	screen.blit(bt_img, (x, y))
	
def grass_img(x, y):
	gr_img = pygame.image.load('floorblock.png').convert_alpha()
	screen.blit(gr_img, (x, y))
def grassroof_img(x, y):
	grr_img = pygame.image.load('floorblock.png').convert_alpha()
	screen.blit(grr_img, (x, y))
	
#variables
x = 160
y = 170
heigth = 60
width = 40
vel = 8

#colors
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)

#sprite shit
incomingpipes = pygame.sprite.Group()
hitboxer = pygame.sprite.Group()
floor = pygame.sprite.Group()
backgroundmovement = pygame.sprite.Group()
bgmove = BGMove(GREEN, 100, 350, -10)
bgmove.rect.x = 0
bgmove.rect.y = 0
grass_movement = Grass(GREEN, 100, 350, -10)
grass_movement.rect.x = 0
grass_movement.rect.y = 650
playerHitbox = Hitbox(WHITE,70,50,50)
playerHitbox.rect.x = 160
playerHitbox.rect.y = 170
greenPipewall = Pipewall(WHITE, 100, 210, 100)
greenPipewall.rect.x = 700
greenPipewall.rect.y = 100
secondPipewall2 = Pipewall(WHITE, 100, 350, -10)
secondPipewall2.rect.x = 1150
secondPipewall2.rect.y = 430
backgroundmovement.add(bgmove)
incomingpipes.add(greenPipewall)
incomingpipes.add(secondPipewall2)
floor.add(grass_movement)
hitboxer.add(playerHitbox)
pygame.mixer.music.load('music4.wav')
pygame.mixer.music.play(5)

def game():
	global running
	global y
	global counter
	global hicounter
	global vel
	global x
	d = shelve.open('hiscore.txt')
	d['hiscore'] = hicounter  # the score is read from disk
	d.close()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			d = shelve.open('hiscore.txt')
			d['hiscore'] = hicounter          # thats all, now it is saved on disk.
			d.close()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				flapnoise()
				playerHitbox.rect.y = playerHitbox.rect.y - (vel * 10)
				y -= (vel * 10)
	y += vel
	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		running=False
		titlerun=True
		return
	if playerHitbox.rect.y <= 50:
		playerHitbox.rect.y = 50
	if playerHitbox.rect.y >= 565:
		playerHitbox.rect.y = 565
	for BGMove in backgroundmovement:
		BGMove.moveLeft(vel/8)
		while bgmove.rect.x<0:
			bgmove.rect.x=800
	for Grass in floor:
		Grass.moveLeft(vel)
		while grass_movement.rect.x < 0:
			grass_movement.rect.x = 800
	for Hitbox in hitboxer:
		Hitbox.moveBackward(vel)
		while playerHitbox.rect.y < 105:
			playerHitbox.rect.y = 105
		while playerHitbox.rect.y > 580:
			playerHitbox.rect.y = 580
	for Pipewall in incomingpipes:
		Pipewall.moveLeft(vel)
		if Pipewall.rect.x < -200:
			counter = counter + 1
			print("Your score is: " + str(counter))
			Pipewall.rect.x = 800
			vel = vel +.25
			print(int(vel))
			goalnoise()
	incomingpipes.update()
	floor.update()
	backgroundmovement.update()
	hitboxer.update()
	background(bgmove.rect.x,0)
	background(bgmove.rect.x-800,0)
	player((playerHitbox.rect.x - 100), (playerHitbox.rect.y-100))
	toppipe_img(greenPipewall.rect.x, 100)
	bottompipe_img(secondPipewall2.rect.x, 430)
	grass_img(grass_movement.rect.x, 635)
	grass_img((grass_movement.rect.x - 200), 635)
	grass_img((grass_movement.rect.x - 400), 635)
	grass_img((grass_movement.rect.x - 600), 635)
	grass_img((grass_movement.rect.x - 800), 635)
	grass_img((grass_movement.rect.x + 200), 635)
	grass_img((grass_movement.rect.x + 400), 635)
	grass_img((grass_movement.rect.x + 600), 635)
	grassroof_img((grass_movement.rect.x + 200), -100)
	grassroof_img((grass_movement.rect.x + 400), -100)
	grassroof_img((grass_movement.rect.x + 600), -100)
	grassroof_img((grass_movement.rect.x - 200), -100)
	grassroof_img((grass_movement.rect.x - 400), -100)
	grassroof_img((grass_movement.rect.x - 600), -100)
	grassroof_img((grass_movement.rect.x - 800), -100)
	grassroof_img(grass_movement.rect.x, -100)
	pygame.draw.rect(screen, BLACK, [0, 0, 800, 40], 0)
	hiscoretext = myfont.render("HISCORE: " + str(hicounter), 60, (255,255,255))
	hiscoretext_rect = hiscoretext.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(hiscoretext, hiscoretext.get_rect(topleft = screen.get_rect().topleft))
	scoretext = myfont.render("SCORE: " + str(counter), 80, (255,255,255))
	scoretext_rect = scoretext.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	screen.blit(scoretext, scoretext.get_rect(topright = screen.get_rect().topright))
	pygame.display.update()
	clock.tick(30)
	
while gameon:
	while titlerun == True:
		title()
	else:
		game()
	sprite_collision_list = pygame.sprite.spritecollide(playerHitbox,incomingpipes,False)
	for sprite in sprite_collision_list:
		if counter >= hicounter:
			hicounter = counter
		counter = 0
		vel = 8
		d = shelve.open('hiscore.txt')
		d['hiscore'] = hicounter          # thats all, now it is saved on disk.
		d.close()
		running=False
		titlerun=True
exit()
