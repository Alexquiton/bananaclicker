from typing import Text
import pygame

pygame.init()
color_inactive = (214, 214, 214)
color_active = (150, 150, 150)
placeholder_color = (220,220,220)
FONT = pygame.font.Font(None, 32)

class InputBox:
    pygame.init()
    color_inactive = (214, 214, 214)
    color_active = (150, 150, 150)
    placeholder_color = (220,220,220)
    FONT = pygame.font.Font(None, 32)   
    def __init__(self,placeholder, x, y, w, h, text="", ):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.placeholder = placeholder
        self.placeholder_surface = FONT.render(self.placeholder, True, placeholder_color)
        self.active = False
        self.censored_text = ""
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = color_active if self.active else color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    #if box is password then return should trigger login button
                    self.text=""
                    self.censored_text=""
                elif event.key == pygame.K_BACKSPACE:
                    if(self.placeholder == "Password"):
                        self.censored_text = self.censored_text[:-1]
                    self.text = self.text[:-1]

                else:
                    self.text += event.unicode
                    if(self.placeholder == "Password"):
                        while len(self.censored_text) < len(self.text):
                            self.censored_text += "*"

                if(self.placeholder == "Password"):
                    self.txt_surface = FONT.render(self.censored_text, True, self.color)
                else:
                    self.txt_surface = FONT.render(self.text, True, self.color)
    
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w= width
        
    def draw(self,screen):
        if(self.active == False and self.text == ""):
            screen.blit(self.placeholder_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
    
    
    