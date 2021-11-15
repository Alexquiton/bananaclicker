import pygame
pygame.init()
FONT = pygame.font.Font(None,24)

class Text:
    def __init__(self):
        pass
    

    def createText(self,text_color,text_title):
        title_surface = FONT.render(text_title,True,text_color)
        return title_surface
