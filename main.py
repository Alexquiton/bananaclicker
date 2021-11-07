#banana clicker
from typing import Optional
import pygame

from inputbox import InputBox
from login_screen import login_screen


pygame.init()
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Clicker")


#variables
FPS = 60
clock = pygame.time.Clock()
backgroundColor = (255,255,255)



        


def main():
    run = True
    
    #login screen can also register
    loginscreen = login_screen(WIN,backgroundColor)
    loginscreen.draw_screen()

    #load game progress

    #play game

    print("hi")
        
        
        
        
        
        
        

        
        
        

    

    pygame.quit()

if __name__ == "__main__":
    main()