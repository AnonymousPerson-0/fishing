import pygame

class Lake:
    def __init__(self, playerRef):
        self.position = [0, 0]
        self.blocks = [] # -> Array<Rect r>
        self.blockPos = {} # -> Array<int x, int y> a : True
        self.playerRef = playerRef
        self.proximConst = 10
    
    def checkProximity():
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # b4 we check anything determine the lines that are the sides of the object.
        lines = [] # -> Rect, [dx, dy]
        for i in range(len(blocks)):
            for j in range(4):
                if (not blockPos.get([blocks[i].centerx + dx[j]*blocks[i].width, blocks[i].centery + dy[j]*blocks[i].height], False)):
                    lines.append([blocks[i], [dx[i], dx[y]])

        for i in range(len(lines)):
            if (lines[i][1][0] == 1):
                if ((self.playerRef.pos[0] <= lines[i][0].right + proximConst and self.playerRef.pos[0] >= lines[i][0].right) and (self.playerRef.pos[1] <= lines[i][0].top and self.playerRef.pos[1] >= lines[i][0].bottom)):
                    # it is next to the line
                    return True
            elif (lines[i][1][1] == 1):
                if ((self.playerRef.pos[1] <= lines[i][0].bottom + proximConst and self.playerRef.pos[1] >= lines[i][0].bottom) and (self.playerRef.pos[0] >= lines[i][0].left and self.playerRef.pos[0] <= lines[i][0].right)):
                    return True
            elif (lines[i][1][0] == -1):
                if ((self.playerRef.pos[0] >= lines[i][0].left - proximConst and self.playerRef.pos[0] <= lines[i][0].left) and (self.playerRef.pos[1] <= lines[i][0].top and self.playerRef.pos[1] >= lines[i][0].bottom)):
                    return True
            elif (lines[i][1][1] == -1):
                if ((self.playerRef.pos[1] >= lines[i][0].top - proximConst and self.playerRef.pos[1] <= lines[i][0].top) and (self.playerRef.pos[0] >= lines[i][0].left and self.playerRef.pos[0] <= lines[i][0].right)):
                    return True
        return False
