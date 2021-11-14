import pygame
from pygame.constants import MOUSEBUTTONDOWN
import time

image = pygame.image.load("banana_image.png")
banana_image = pygame.transform.scale(image, (500,500))
position = (50,50)

class BananaBtn:
    def __init__(self):
        self.image = banana_image
        self.image_rect = self.image.get_rect(topleft=position)
        self.active = False
        self.button_name = "banana"
    
    def on_click(self,event):
        if event.type == MOUSEBUTTONDOWN:
            if self.image_rect.collidepoint(event.pos):
                self.active = True
        else:
            self.active = False
    
    def draw_button(self,screen):
        screen.blit(self.image,self.image_rect)