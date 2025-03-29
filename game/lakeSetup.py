import pygame

class Lake:
    def __init__(self, playerRef):
        self.position = 0
        self.proximConst = 10

    def checkProximity(self, player):
        # because the lake is now just a line, just measure 
        if (player.pos[0] >= self.position - self.proximConst):
            return True
        return False
