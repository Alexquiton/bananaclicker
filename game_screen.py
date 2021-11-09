import pygame
import json
from banana_button import BananaBtn
from game import Game


class Game_Screen:
    def __init__(self,WIN,backgroundColor):
        self.FONT = pygame.font.Font(None, 32)
        self.WIN = WIN
        self.run = True
        self.backgroundColor = backgroundColor
        self.bananas = 0
        self.username = ""
        #temp
        
    
    
    
    def load_progress(self,bananas,username):
        self.bananas = bananas
        self.username = username
    
    def load_accounts(self):
        data = open("user_details.txt","r")
        account_list = []
        for account in data:
            if(account != ""):
                dict_account = json.loads(account)
                account_list.append(dict_account)
        data.close()
        return account_list
    def save_progress(self):
        data = open("user_details.txt","r")
        account_list = self.load_accounts()
        list_of_lines = data.readlines()
        lineNum = 0
        saved_account = {}
        for account in account_list:
            if(account["username"] == self.username):
                saved_account = account
                account["bananas"] = self.bananas
                print(self.bananas) #-------------------------------
                print(saved_account)
                break
            lineNum += 1
        list_of_lines[lineNum] = json.dumps(saved_account)
        data = open("user_details.txt", "w")
        data.writelines(list_of_lines)
        data.close()
        

        data.close()
        print('saved progress')



        

    def draw_screen(self):
        game = Game(self.bananas)
        bananaBtn = BananaBtn()
        button_list = [bananaBtn]
        #temp
        counter_color = (0,0,0)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_progress()
                    self.run = False
                #------all button events will be in here------#
                for buttons in button_list:
                    buttons.on_click(event)
            
            for button in button_list:
                if(button.button_name == "banana"):
                    if(button.active == True):
                        game.addBanana(1)
                        self.bananas = game.bananas
                        button.active = False

            
            self.WIN.fill(self.backgroundColor)
            #anything draw to the screen
            bananaBtn.draw_button(self.WIN)
            counter_title = "Counter: " + str(game.bananas)
            counter_surface = self.FONT.render(counter_title, True, counter_color)
            self.WIN.blit(counter_surface, (600,100))

            pygame.display.flip()