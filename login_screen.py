import json
import pygame
from inputbox import InputBox
from loginBtn import LoginBtn
class login_screen:
    
    def __init__(self,WIN,backgroundColor):
        FONT = pygame.font.Font(None, 32)
        self.WIN = WIN
        self.backgroundColor = backgroundColor
        self.run = True
        self.login = True
        self.register = False
        self.register_title = "REGISTER"
        self.register_color = (0,0,0)
        self.register_surface = FONT.render(self.register_title, True, self.register_color)
        self.login_title = "LOGIN"
        self.login_color = (0,0,0)
        self.login_surface = FONT.render(self.login_title, True, self.login_color )
        
    def draw_screen(self):
        username_box = InputBox("Username",350,200,140,32)
        password_box = InputBox("Password",350,240,140,32)
        input_boxes = [username_box,password_box]
        login_button = LoginBtn(350,290,70,32,"Login")
        #create a register class
        register_button = LoginBtn(450,290,100,32,"Register")
        buttons = [login_button, register_button]
        
        
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                for box in input_boxes:
                    box.handle_event(event)
                for button in buttons:
                    button.handle_event(event)
                    
            self.WIN.fill(self.backgroundColor)
            for box in input_boxes:  
                box.update()
                box.draw(self.WIN)
            for button in buttons:
                button.draw_button(self.WIN)
            
            
            if(login_button.active == True):
                login_button.login(username_box.text,password_box.text)

            
            
           
                
            self.WIN.blit(self.login_surface, (410, 160))
        
            pygame.display.flip()


        


