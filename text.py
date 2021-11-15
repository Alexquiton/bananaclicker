import pygame
pygame.init()


class Text:
    def __init__(self):
        pass
    

    def createText(self,text_color,text_title,font_size):
        FONT = pygame.font.Font(None,font_size)
        title_surface = FONT.render(text_title,True,text_color)
        return title_surface
