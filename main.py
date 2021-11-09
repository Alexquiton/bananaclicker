#banana clicker
from typing import Optional
import pygame
from game_screen import Game_Screen
from inputbox import InputBox
from login_screen import login_screen

pygame.init()
WIDTH = 1400
LENGTH = 800
WIN = pygame.display.set_mode((WIDTH,LENGTH))
pygame.display.set_caption("Banana Clicker")

#variables
FPS = 60
clock = pygame.time.Clock()
backgroundColor = (255,255,255)
gameBGcolor = (255, 196, 0)
gamerun = False

def main():
    run = True
    user_account = {}
    #login screen can also register
    loginscreen = login_screen(WIN,backgroundColor)
    user_account = loginscreen.draw_screen()
    #should return id number here
    if(user_account != None):
        gamerun = True
    if(gamerun):
        gamescreen = Game_Screen(WIN,gameBGcolor)
        #load game prgoress
        gamescreen.load_progress(user_account["id"])
        gamescreen.draw_screen()

    #play game 

    #save and load

    print("LOGGED In")

    pygame.quit()

if __name__ == "__main__":
    main()