import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import time
#############################
# GameBtn Class
# Functions: 
# __init__(buttonName,x,y,scaleX,scaleY,image,soundEffect1,soundEffect2):
# @params: buttonName,x,y,scaleX,scaleY,image,soundEffect1,soundEffect2
# buttonName is the name of the button in which function it would do
# x and y are the positons of the button on the screen shown to the user
# scaleX,scaleY refer to the amount to scale the image
# image is the string path in which the image file is in
# soundEffect1 and soundEffect2 are string paths in which the audio file is located
# @brief: initalizes all of the self variables for the button
# @return: none
#
# on_click(event):
# @params: event
# event refers to the user input (mouse button down, key down)
# @breif: listens to when the mouse button is down and sets the button bool to true for active
# and upon mouse release it set the button bool to false for not active along with plays the
# sound effect for when the button mouse is down or up
# @return: none
#
# draw_button(WIN):
# @params: WIN
# WIN refers to the screen in which the user is interacting with
# @brief: draws the button onto the screen 
# @return: none
##############################

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