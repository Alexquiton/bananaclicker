import pygame
import json

pygame.init()
color_active = (150,150,150)
placeholder_color = (150,150,150)
FONT = pygame.font.Font(None,32)

class RegisterBtn:
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
        last_account = account_list[-1]
        id = last_account["id"] + 1
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
                "id": id
            }
            data = open("user_details.txt","a")
            data.write("\n")
            json.dump(account,data)
            data.close
            #--------
            game_progress = {
                "id": id,
                "bananas": 0
            }
            gameprog = open("gameprogress.txt","a")
            gameprog.write("\n")
            json.dump(game_progress,gameprog)
            gameprog.close
            correct_register.append(True)
            return correct_register