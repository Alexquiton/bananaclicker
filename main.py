#banana clicker
from typing import Optional
import pygame

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Clicker")

backgroundColor = (255,255,255)

#variables
playgame = False

def draw_window():
    WIN.fill(backgroundColor)
    pygame.display.update()

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    

    pygame.quit()

if __name__ == "__main__":
    main()