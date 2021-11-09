import json
import pygame
from inputbox import InputBox
from loginBtn import FONT, LoginBtn
from registerBtn import RegisterBtn
class login_screen:
    
    def __init__(self,WIN,backgroundColor):
        FONT = pygame.font.Font(None, 32)
        self.WIN = WIN
        self.backgroundColor = backgroundColor
        self.run = True
        self.login = True
        self.register_title = "REGISTER"
        self.register_color = (0,0,0)
        self.register_surface = FONT.render(self.register_title, True, self.register_color)
        self.login_title = "LOGIN"
        self.login_color = (0,0,0)
        self.login_surface = FONT.render(self.login_title, True, self.login_color )
        self.error_message = ""
        self.error_color = (0,0,0)
        self.error_active = False
        
    def draw_screen(self):
        username_box = InputBox("Username",350,200,140,32)
        password_box = InputBox("Password",350,240,140,32)
        input_boxes = [username_box,password_box]
        login_button = LoginBtn(350,290,70,32,"Login")
        #create a register class
        register_button = RegisterBtn(450,290,100,32,"Register")
        back_button = RegisterBtn(350,290,70,32, "Back")
        signup_button = RegisterBtn(450,290,90,32,"Sign Up")
        buttons = [login_button, signup_button]
        
        while self.run:
            #event handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                for box in input_boxes:
                    box.handle_event(event)
                for button in buttons:
                    if(self.login):
                        button.handle_event(event)
                if(self.login == False):
                    register_button.handle_event(event)
                    back_button.handle_event(event)
            
            #drawing buttons/input boxes
            self.WIN.fill(self.backgroundColor)
            for box in input_boxes:  
                box.update()
                box.draw(self.WIN)
            for button in buttons:
                if(self.login):
                    button.draw_button(self.WIN)
            
            #screen switching buttons
            if(signup_button.active == True):
                self.login = False
                self.error_active = False
            
            if(back_button.active == True):
                self.login = True
                signup_button.active = False
                self.error_active = False
            
            #main buttons
            if(login_button.active == True):
                login_access = []
                login_access = login_button.login(username_box.text,password_box.text)
                if(login_access[0] == False):
                    #no username or password wrong
                    self.error_message = login_access[1]
                    self.run = True
                    self.error_active = True
                    login_button.active = False
                else:
                    return login_access[1]
                    
            if(register_button.active == True):
                register_access = []
                register_access = register_button.register(username_box.text,password_box.text)
                if(register_access[0] == False):
                    #username already taken
                    self.error_message = register_access[1]
                    self.run = True
                    signup_button.active = False
                    self.error_active = True
                    register_button.active = False
                else:
                    self.login = True
                    signup_button.active = False
                    self.error_active = False

            #controls screens
            if(self.login):
                #displays login title
                self.WIN.blit(self.login_surface, (410, 160))
                register_button.active = False
                back_button.active = False
            else:
                self.WIN.blit(self.register_surface, (390, 160))
                register_button.draw_button(self.WIN)
                back_button.draw_button(self.WIN)
            
            #errors
            if(self.error_active):
                error_surface = FONT.render(self.error_message, True, self.error_color)
                self.WIN.blit(error_surface,(200,100))
                
            pygame.display.flip()


        


