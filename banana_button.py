import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import time

image = pygame.image.load("banana_image.png")
banana_image = pygame.transform.scale(image, (250,250))
position = (20,70)

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
                click_sound = pygame.mixer.Sound("mouseBtn_down.mp3")
                click_sound.set_volume(0.07)
                click_sound.play()
                
        else:
            self.active = False
        if event.type == MOUSEBUTTONUP:
            if self.image_rect.collidepoint(event.pos):
                release_sound = pygame.mixer.Sound("mouseBtn_up.mp3")
                release_sound.set_volume(0.06)
                release_sound.play()

    
    def draw_button(self,screen):
        screen.blit(self.image,self.image_rect)