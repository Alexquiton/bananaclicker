import pygame


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
    def __init__(self,bananas,multiClicks):
        self.bananas = bananas
        self.clickMultiplier = multiClicks
        self.bananaPerClick = 1
        self.upgradeCost = ((10 + self.clickMultiplier) * 10)

    def addBanana(self):
        self.bananaPerClick = 1 + self.clickMultiplier
        self.bananas += self.bananaPerClick
    
    def multiClick(self):
        if(self.bananas >= self.upgradeCost):
            self.bananas -= self.upgradeCost
            self.clickMultiplier += 1
            self.upgradeCost += 10
            
        
        
    
