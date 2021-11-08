import pygame

pygame.init()
color_active = (150, 150, 150)
placeholder_color = (150,150,150)

FONT = pygame.font.Font(None, 32)

class LoginBtn:
    
    def __init__(self,x,y,w,h,placeholder):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color_active
        self.active = False
        self.placeholder = placeholder
        self.placeholder_surface = FONT.render(self.placeholder, True, placeholder_color)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            


    def draw_button(self,screen):
        screen.blit(self.placeholder_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen,self.color, self.rect, 2)
    
    def login(self,username,password):
        #login
        print(username)
        print(password)
        self.active = False


    
        