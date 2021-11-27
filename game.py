import pygame
import json

#########################################
# Game class
# Functions:
# __init__(bananas):
# @params: bananas
# bananas refers to the amount of bananas the user had
# @brief: stores the amount of bananas in self.bananas
# @return: none
#
# addBanana(amount):
# @params amount
# amount is the the number of bananas to add to the existing amount
# @brief: updates the current number of bananas on the game itself depending
# on the number of bananas added
# @returns: none
##########################################

class Game:
    def __init__(self,bananas):
        self.bananas = bananas
        

    def addBanana(self,amount):
        self.bananas += amount
    
    
