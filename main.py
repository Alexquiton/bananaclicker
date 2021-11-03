#banana clicker
from typing import Optional
import pygame

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Clicker")


#variables
FPS = 60
clock = pygame.time.Clock()
playgame = False
login = False
backgroundColor = (255,255,255)
login_textbox = (214, 214, 214)

#draws up a window with background color of white
def draw_window():
    
    WIN.fill(backgroundColor)
    login_window(login)
    pygame.display.update()

def login_window(logged_in):
    if(logged_in == False):
        #in window ask user to either login or register
        #default is login window with register button

        #dimensions of the text input
        username_input = pygame.Rect(350,200,140,32)
        password_input = pygame.Rect(350,240,140,32)

        #drawing the rectangle
        pygame.draw.rect(WIN,login_textbox,username_input,2)
        pygame.draw.rect(WIN,login_textbox,password_input,2)
        pygame.display.flip()












def main():

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    

    pygame.quit()

if __name__ == "__main__":
    main()