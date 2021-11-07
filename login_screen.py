import json
import pygame
from inputbox import InputBox
class login_screen:
    
    def __init__(self,WIN,backgroundColor):
        FONT = pygame.font.Font(None, 32)
        self.WIN = WIN
        self.backgroundColor = backgroundColor
        self.run = True
        self.login_title = "LOGIN"
        self.login_color = (0,0,0)
        self.login_surface = FONT.render(self.login_title, True, self.login_color )
        
    def draw_screen(self):
        username_box = InputBox(self.WIN,"Username",350,200,140,32)
        password_box = InputBox(self.WIN,"Password",350,240, 140,32)
        input_boxes = [username_box,password_box]
        
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                for box in input_boxes:
                    box.handle_event(event)
            self.WIN.fill(self.backgroundColor)
            for box in input_boxes:  
                box.update()
                box.draw(self.WIN)
                

            self.WIN.blit(self.login_surface, (410, 160))
        
            pygame.display.flip()


        


