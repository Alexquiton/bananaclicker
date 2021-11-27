import pygame
pygame.init()

#########################################
# Text Class
# Functions:
# __init__():
# @params: none
# @breif: takes no paramaters basically a method
# @return none:
# 
# createText(text_color,text_title,font_size)
# @params: text_color, text_title, font_size
# text_color is the color of the text
# text_title refers to what the text is going to say
# font_size refers to the size of the text
# @breif: takes in those 3 paramaters and creates a surface
# for the text
# @returns: returns title_surface which is what is needed to blit(draw) the 
# text to the screen
############################################
class Text:
    def __init__(self):
        pass
    

    def createText(self,text_color,text_title,font_size):
        FONT = pygame.font.Font(None,font_size)
        title_surface = FONT.render(text_title,True,text_color)
        return title_surface
