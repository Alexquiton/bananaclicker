from typing import Text
import pygame



pygame.init()
color_inactive = (214, 214, 214)
color_active = (200, 200, 200)
FONT = pygame.font.Font(None, 32)

class InputBox:
    def __init__(self,screen,x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
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
                    self.text=""
                    #draw_window()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    #draw_window()
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w= width
        
    
    def draw(self,screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        
    
    