#banana clicker
from typing import Optional
import pygame

from inputbox import InputBox


pygame.init()
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Clicker")


#variables
FPS = 60
clock = pygame.time.Clock()
playgame = False
login = False
backgroundColor = (1,1,1)
base_font = pygame.font.SysFont("GameOfSquids.ttf", 32)
input_boxes = []



        


def main():
    global input_boxes
    run = True
    username_box = InputBox(WIN,350,200,140,32)
    password_box = InputBox(WIN,350,240, 140,32)
    input_boxes = [username_box,password_box]
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for box in input_boxes:
                box.handle_event(event)
        WIN.fill(backgroundColor)
        for box in input_boxes:  
            box.update()
            box.draw(WIN)
        
        pygame.display.flip()
        
        
        
        
        
        
        

        
        
        

    

    pygame.quit()

if __name__ == "__main__":
    main()