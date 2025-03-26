import pygame

class LinkedList:
    def __init__(self, next = None, prev = None):
        self.next = next
        self.prev = prev

class Player:
    def __init__(self):
        self.v = [0, 0]
        self.pos = [0, 0]

        self.inventory = {} # a dictionary filled with pairs of values: key is name of object, value is a descriptor of object
