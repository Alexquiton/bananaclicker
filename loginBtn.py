import pygame
import json
from text import Text

pygame.init()
color_active = (150, 150, 150)
placeholder_color = (150,150,150)


class LoginBtn:
    
    def __init__(self,x,y,w,h,placeholder):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color_active
        self.active = False
        self.placeholder = placeholder
        self.placeholder_surface = Text()
        self.placeholder_surface = self.placeholder_surface.createText(self.color,self.placeholder,32)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            
    def draw_button(self,screen):
        screen.blit(self.placeholder_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen,self.color, self.rect, 2)
    
    def load(self):
        data = open("user_details.txt","r")
        account_list = []
        for account in data:
            if(account != ""):
                dict_account = json.loads(account)
                account_list.append(dict_account)
        return account_list

    def login(self,username,password):
        login_access = False
        no_username = True
        wrong_password = False
        false_login = []
        correct_login = []
        account_list = self.load()
        user_account = {}
        for account in account_list:
            if(account["username"] == username and account["password"] == password):
                login_access = True
                no_username = False
                user_account = account
                break
            if(account["username"] == username and account["password"] != password):
                no_username = False
                wrong_password = True
                break
        self.active = False
        if(login_access == True):
            #found account and password correctly
            correct_login.append(True)
            correct_login.append(user_account)
            return correct_login
        else:
            if(no_username):
                false_login.append(False)
                false_login.append("No account under username")
            if(wrong_password):
                false_login.append(False)
                false_login.append("Wrong password")
            return false_login
        


    
        