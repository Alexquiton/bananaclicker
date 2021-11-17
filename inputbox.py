from typing import Text
import pygame

pygame.init()
color_inactive = (214, 214, 214)
color_active = (150, 150, 150)
placeholder_color = (220,220,220)
FONT = pygame.font.Font(None, 32)

###############################################################
# Input Box Class
# Functions:
# __init__(placeholder,x,y,w,h,text="")
# @params: placeholder,x,y,w,h,text=""
# placeholdeer is the title of the box and appears in the inputbox
# x and y are the position of the input boxes on the screen
# w and h are the width and height of the input box
# text="" is the text that the user is typing in the inputboxes
# @bref: initalizes self variables
# @returns: none
#
# handle_event(event):
# @params event
# event is the user input such as mousebutton down are keystrokes
# @brief: takes in event and assigns the variables accordlingly to
# what event is inputted, also with each keystroke it will add it to the
# the text="" varible and will also delete a letter of what was inputted
# also differiates between a username box and password box in which the password box
# will censor the text on screen but will still store what the user is typing
# @returns: none
#
# update():
# @params: none
# @brief: updates the width of the box depending on the number of characters in the text
# @returns: none
#
# draw(WIN):
# @params: WIN
# WIN refers to the window that is displaying to the user
# @breif: draws the input box along with the text that the user inputted and the placeholders
# @returns: none
#################################################################

class InputBox:
    pygame.init()
    color_inactive = (214, 214, 214)
    color_active = (150, 150, 150)
    placeholder_color = (220,220,220)
    FONT = pygame.font.Font(None, 32)   
    def __init__(self,placeholder, x, y, w, h, text=""):
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
                    if(event.key != pygame.K_SPACE):
                        if(event.key != pygame.K_TAB):
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
    
    
    