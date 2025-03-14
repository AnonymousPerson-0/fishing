import pygame
import math
import random
import time
import sys
import os
from playerSetup import Player

pygame.init()
pygame.display.init()
pygame.Mixer.init()
pygame.time.init()

screen = pygame.display.set_mode(600, 800)

clock = pygame.time.Clock()

# variables ===========================================================
player = Player()

# images ==============================================================
startingScreen = pygame.image.load("startingScreen.png")

# images end ==========================================================

def store(): # -> params: None, returns: None
	# we wnat to stop the current thread, and switch to a different thread
	pass

def inRect(x, y, rect): # -> params: int x, int y, Rectangle rect, returns: boolean
	if (x <= rect.right and x >= rect.left and y <= rect.top and y >= rect.bottom):
		return True
	return False

def call(func): # -> params: string func, returns: None
	if (func == "Store"):
		store()
	pass

def fish():
	

# Starting Screen/Splash Art
run = True
while run:
	for event in pygame.events.get():
		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_SPACE):
				run = False
		elif (event.type == pygame.QUIT):
			pygame.display.quit()
			pygame.quit()
			sys.exit()
		elif (event.type == pygame.MOUSEBUTTONDOWN):
			run = False
	# screen.blit()

	clock.tick(60)
	continue

# Introduction Screen
run = True
while run:
	for event in pygame.events.get():
		if (event.type == pygame.KEYDOWN):
			run = False
			continue
		elif (event.type == pygame.QUIT):
			pygame.display.quit()
			pygame.quit()
			sys.exit()
		continue

	# continuously blit the screen here
	clock.tick(60)
	
# Phase 1/Scene 1
HUDrects = [] # is composed of arrays in the format: [rect, func]

run = True
while run:
	for event in pygame.events.get():
		if (event.type == pygame.QUIT):
			pygame.display.quit()
			pygame.quit()
			sys.exit()
		if (event.type == pygame.KEYDOWN):
			continue
		if (event.type == pygame.MOUSEBUTTONDOWN):
			click_pos = pygame.mouse.get_pos()

			for i in range(len(HUDrects)):
				if (inRect(click_pos[0], click_pos[1], HUDrects[i][0])):
					call(HUDrects[i][1])
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_w]):
		player.pos[1] -= 5
	if (keys[pygame.K_a]):
		player.pos[0] -= 5
	if (keys[pygame.K_s]):
		player.pos[1] += 5
	if (keys[pygame.K_d]):
		player.pos[0] += 5

	if (keys[pygame.K_SPACE]):
		fish()
	# blit here
	clock.tick(60)

# Phase 2/Scene 2
HUDrects = []

run = True
while run:
	for event in pygame.events.get():
		if (event.type == pygame.QUIT):
			pygame.display.quit()
			pygame.quit()
			sys.exit()
		if (event.type == pygame.KEYDOWN):
			continue
		if (event.type == pygame.MOUSEBUTTONDOWN):
			click_pos = pygame.mouse.get_pos()

			for i in range(len(HUDrects)):
				if (inRect(click_pos[0], click_pos[1], HUDrects[i][0])):
					call(HUDrects[i][1])
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_w]):
		continue
	if (keys[pygame.K_a]):
		continue
	if (keys[pygame.K_s]):
		continue
	if (keys[pygame.K_d]):
		continue

	# blit here
	clock.tick(60)
	
# Phase 3/Scene 3
run = True
