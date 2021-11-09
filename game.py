import pygame
import json

class Game:
    def __init__(self,bananas):
        self.bananas = bananas
        

    def addBanana(self,amount):
        self.bananas += amount
    
    
