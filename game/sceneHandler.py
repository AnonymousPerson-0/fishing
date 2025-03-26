import pygame
import math

class Building:
    def __init__(self, x, y, sceneNum, width, height, orientation):
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.sceneNum = sceneNum
        if (orientation == 0):
            # orientation is towards the right
            self.doorPos = [x + width, y + height/2]
        elif (orientation == 1):
            # towards the bottom
            self.doorPos = [x + width/2, y + height]
        elif (orientation == 2):
            # towards the left
            self.doorPos = [x, y + height/2]
        else:
            #towards the top
            self.doorPos = [x + width/2, y]

    def checkProximity(self, player):
        if (math.hypot(self.player.pos[0] - self.doorPos[0], self.player.pos[1] - self.doorPos[1]) <= 10):
            return True
        return False
