#banana clicker
from typing import Optional
import pygame
from game_screen import Game_Screen
from login_screen import login_screen

pygame.init()
WIDTH = 1400
LENGTH = 800
WIN = pygame.display.set_mode((WIDTH,LENGTH))
WIN.set_alpha(None)
pygame.display.set_caption("Banana Clicker")

#variables
FPS = 15
backgroundColor = (255,255,255)
gameBGcolor = (255, 196, 0)

#######################################
# 
# main() - Controls the sequence of 
# screens to display
# @param: none
# @return: none
#
#######################################

def main():
    gamerun = False
    user_account = {}
    #login screen can also register
    loginscreen = login_screen(WIN,FPS)
    user_account = loginscreen.runLogin()
    #should return id number here
    if(user_account != None):
        gamerun = True
    if(gamerun):
        gamescreen = Game_Screen(WIN,FPS)
        #load game prgoress
        gamescreen.load_progress(user_account["bananas"],user_account["username"])
        gamescreen.runGame()
    pygame.quit()

if __name__ == "__main__":
    main()