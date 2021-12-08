import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import time

class GameBtn:
    def __init__(self,buttonName,x,y,scaleX,scaleY,image,soundEffect1,soundEffect2):
        self.soundEffect1 = pygame.mixer.Sound(soundEffect1)
        if(soundEffect2 != ""):
            self.enableSE2 = True
            self.soundEffect2 = pygame.mixer.Sound(soundEffect2)
        else:
            self.enableSE2 = False
        self.image = pygame.transform.scale(pygame.image.load(image), (scaleX,scaleY))
        self.image_rect = self.image.get_rect(topleft=(x,y))
        self.active = False
        self.button_name = buttonName
        
    def on_click(self,event):
        if event.type == MOUSEBUTTONDOWN:
            if self.image_rect.collidepoint(event.pos):
                self.active = True
                self.soundEffect1.set_volume(0.008)
                self.soundEffect1.play()
        else:
            self.active = False
        if event.type == MOUSEBUTTONUP:
            if self.image_rect.collidepoint(event.pos):
                if(self.enableSE2):
                    self.soundEffect2.set_volume(0.009)
                    self.soundEffect2.play()
                    
    def draw_button(self,WIN):
        self.image.convert_alpha(WIN)
        WIN.blit(self.image,self.image_rect)