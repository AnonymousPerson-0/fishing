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
canFish = False # only true when the player is next to a lake object
stage = 0 # the stage of the game at some point
money = 0
sanity = 0 # integer that determines the ending the player receives.
# images ==============================================================
startingScreen = pygame.image.load("startingScreen.png")

# images end ==========================================================
def inRect(x, y, rect): # -> params: int x, int y, Rectangle rect, returns: boolean
	if (x <= rect.right and x >= rect.left and y <= rect.top and y >= rect.bottom):
		return True
	return False

def store(): # -> params: None, returns: None
	# we wnat to stop the current thread, and switch to a different thread
	# simply use a while loop and we're good.
	temp = True
	
	while temp:
		for event in pygame.events.get():
			if (event.type == pygame.MOUSEBUTTONDOWN):
				p = pygame.mouse.get_pos() # format: [float x, float y] or [int x, int y]

				if (inRect(p[0], p[1], settings.storeRects[1]):
					temp = False
		
		# blit here
		for i in range(len(settings.storeRects)):
			r = storeRects[i]
			pygame.draw.rect(pygame.Rect(r[0], r[1], r[2], r[3]))

		clock.tick(30)

def decision(stage, choice):
	pass

def call(func): # -> params: string func, returns: None
	if (func == "Store"):
		store()
	if (func[0:7] == "Decision"):
		if (stage == 1):
			if (func[7:] == "1"):
				decision(stage, 1)
			elif (func[7:] == "2"):
				decision(stage, 2)
		elif (stage == 2):
			pass
	pass

def fish(stage): # -> params: int stage, returns: int index of fish caught
	p = math.random()
	for i in range(len(settings.probabilities[stage])):
		if (p < settings.probabilities[stage][i]):
			return i
	return len(settings.probabilities[stage]) - 1

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
HUDrects = [[pygame.Rect(0, 3*settings.HEIGHT/4, settings.WIDTH/10, settings.HEIGHT/4), "Store"]

] # is composed of arrays in the format: [rect, func]
stage = 1

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

	if (keys[pygame.K_SPACE] and canFish):
		index = fish(0)
		if (player.inventory.get(settings.fishByStage[0][index], 0) == 0):
			player.inventory[settings.fishByStage[0][index]] = [settings.object[settings.fishByStage[0][index]], 1]
		else:
			if (not settings.objects[settings.fishByStage[0][index]][2] == "Key Fish"):
				player.inventory[settings.fishByStage[0][index]] = [settings.objects[settings.fishByStage[0][index]], player.inventory[settings.fishByStage[0][index]][1] + 1]
			# this array contains the descriptor for the object
	# blit here
	clock.tick(60)

# Phase 2/Scene 2
HUDrects = []
stage = 2

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
