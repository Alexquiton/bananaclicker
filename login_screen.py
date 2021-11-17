import json
import pygame
from inputbox import InputBox
from loginScreenBtn import LoginScreenBtn
from text import Text
background_image = pygame.image.load("Assets/loginScreen_bg.png")
background_image = pygame.transform.scale(background_image, (1400,800))

##################################
# Login Screen  Class
# Functions:
# __init__(WIN, FPS):
# @params: WIN, FPS
# WIN is the main screen window that is initalized in main.py
# FPS is how many frames per second the login screen will refresh
# @brief: function initalizes the login screen self variables
# @returns: none
#
# runLogin():
# @params: none
# @brief: handles the user inputs along with drawing buttons,text,inputboxes,background image to the window
# @returns: the account that is logged in to the mainscreen
#
# draw_screen(input_boxes, loginScreen_buttons, registerScreen_buttons):
# @params: input_boxes, loginScreen_buttons, registerScreen_buttons
# input_boxes are the username and inputbox fields
# loginScreen_buttons are the buttons that are shown on the login screen
# registerScreen_buttons are the buttons that are shown when registering
# @bref: draws the buttons,input boxes, and title of current screen onto the window
# @returns: none
#####################################


class login_screen:
    def __init__(self,WIN,FPS):
        FONT = pygame.font.Font(None, 32)
        self.WIN = WIN
        self.run = True
        self.login = True
        self.register_surface = Text()
        self.login_surface = Text()
        self.register_surface = self.register_surface.createText((0,0,0),"REGISTER",32)
        self.login_surface = self.login_surface.createText((0,0,0),"LOGIN",32)
        self.error_message = ""
        self.error_color = (255,50,0)
        self.error_active = False
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        background_image.convert(self.WIN)
    
    def runLogin(self):
        username_box = InputBox("Username",595,325,140,32)
        password_box = InputBox("Password",595,375,140,32)
        input_boxes = [username_box,password_box]
        login_button = LoginScreenBtn(595,425,70,32,"Login")
        register_button = LoginScreenBtn(695,425,100,32,"Register")
        back_button = LoginScreenBtn(595,425,70,32, "Back")
        signup_button = LoginScreenBtn(700,425,95,32,"Sign Up")
        loginScreen_buttons = [login_button, signup_button]
        registerScreen_buttons = [register_button,back_button]
        
            
        while self.run:
            self.clock.tick(self.FPS)
            #event handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.event.clear()
                    self.run = False
                for box in input_boxes:
                    box.handle_event(event)
                for button in loginScreen_buttons:
                    if(self.login):
                        button.handle_event(event)
                if(self.login == False):
                    for button in registerScreen_buttons:
                        button.handle_event(event)
            
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
            self.draw_screen(input_boxes,loginScreen_buttons,registerScreen_buttons)
            

    def draw_screen(self,input_boxes,loginScreen_buttons,registerScreen_buttons):
        self.WIN.blit(background_image,background_image.get_rect(topleft=(0,0)))
        for box in input_boxes:  
            box.update()
            box.draw(self.WIN)
        for button in loginScreen_buttons:
            if(self.login):
                button.draw_button(self.WIN)
            
        #controls screens
        if(self.login):
            #displays login title
            self.WIN.blit(self.login_surface, (655, 275))
            for button in registerScreen_buttons:
                button.active = False
        else:
            #display register title and register/back buttons
            self.WIN.blit(self.register_surface, (635, 275))
            for button in registerScreen_buttons:
                button.draw_button(self.WIN)
            

        #screen switching buttons
        if(loginScreen_buttons[1].active == True):
            self.login = False
            self.error_active = False
        
        if(registerScreen_buttons[1].active == True):
            self.login = True
            loginScreen_buttons[1].active = False
            self.error_active = False
        
        #displays errors
        if(self.error_active):
            error_surface = Text()
            error_surface = error_surface.createText(self.error_color,self.error_message,32)
            self.WIN.blit(error_surface,(555,495))
            
        pygame.display.flip()


        


