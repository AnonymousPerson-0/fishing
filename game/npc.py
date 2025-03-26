import pygame
import math

class NPC:
    def __init__(self, dialogue, choices, pos): # -> dialogue - Array of strings that determines dialogue, choices -> array of strings that determines choices, pos -> tuple (x, y) position of sprite
		self.dialogue = []
		self.dialogueSeen = False
		self.choices = []
		self.pos = pos
	def checkProximity(self, player):
		if (math.hypot(player.pos[0] - self.pos[0], player.pos[1] - self.pos[1]) <= 10):
			return True
		return False
