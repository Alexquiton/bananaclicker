import pygame
import json
from text import Text
pygame.init()
color_active = (150,150,150)
placeholder_color = (150,150,150)


class RegisterBtn:
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

    def register(self,username,password):
        account_list = self.load()
        false_register = []
        correct_register = []
        taken_username = False
        for account in account_list:
            if(account["username"] == username):
                taken_username = True
                break
        if(taken_username == True):
            false_register.append(False)
            false_register.append("Username Already Taken")
            return false_register
        else:
            account = {
                "username": username,
                "password": password,
                "bananas": 0
            }
            data = open("user_details.txt","a")
            data.write("\n")
            json.dump(account,data)
            data.close
            correct_register.append(True)
            return correct_register