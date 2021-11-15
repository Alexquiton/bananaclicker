import json
import pygame
from inputbox import InputBox
from loginBtn import LoginBtn
from registerBtn import RegisterBtn
from text import Text
background_image = pygame.image.load("loginScreen_bg.png")
background_image = pygame.transform.scale(background_image, (1400,800))

class login_screen:
    def __init__(self,WIN,backgroundColor,FPS):
        FONT = pygame.font.Font(None, 32)
        self.WIN = WIN
        self.backgroundColor = backgroundColor
        self.run = True
        self.login = True
        self.register_surface = Text()
        self.login_surface = Text()
        self.error_message = ""
        self.error_color = (255,50,0)
        self.error_active = False
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        background_image.convert(WIN)
        
    def draw_screen(self):
        username_box = InputBox("Username",595,325,140,32)
        password_box = InputBox("Password",595,375,140,32)
        input_boxes = [username_box,password_box]
        login_button = LoginBtn(595,425,70,32,"Login")
        register_button = RegisterBtn(695,425,100,32,"Register")
        back_button = RegisterBtn(595,425,70,32, "Back")
        signup_button = RegisterBtn(700,425,95,32,"Sign Up")
        buttons = [login_button, signup_button]
        self.register_surface = self.register_surface.createText((0,0,0),"REGISTER",32)
        self.login_surface = self.login_surface.createText((0,0,0),"LOGIN",32)
        
        while self.run:
            self.clock.tick(self.FPS)
            #event handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.event.clear()
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
            
            #self.WIN.fill(self.backgroundColor)
            self.WIN.blit(background_image,background_image.get_rect(topleft=(0,0)))
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
                self.WIN.blit(self.login_surface, (655, 275))
                register_button.active = False
                back_button.active = False
            else:
                #display register title and register/back buttons
                self.WIN.blit(self.register_surface, (635, 275))
                register_button.draw_button(self.WIN)
                back_button.draw_button(self.WIN)
            
            #displays errors
            if(self.error_active):
                error_surface = Text()
                error_surface = error_surface.createText(self.error_color,self.error_message,32)
                self.WIN.blit(error_surface,(555,495))
                
            pygame.display.flip()


        


