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
        #temp
        
    
    
    
    def load_progress(self,id):
        game_data = open("gameprogress.txt","r")
        gameprog_list = []
        for progress in game_data:
            if(progress != ""):
                dict_progress = json.loads(progress)
                gameprog_list.append(dict_progress)
        
        for progress in gameprog_list:
            if(progress["id"] == id):
                self.bananas = progress["bananas"]
                break

    def draw_screen(self):
        game = Game(self.bananas)
        bananaBtn = BananaBtn()
        button_list = [bananaBtn]
        #temp
        counter_color = (0,0,0)
        while self.run:
            
            print(bananaBtn.active)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                #------all buttons will be in here------#
                for buttons in button_list:
                    buttons.on_click(event)
            
            for button in button_list:
                if(button.button_name == "banana"):
                    if(button.active == True):
                        game.addBanana(1)
                        button.active = False

            
            self.WIN.fill(self.backgroundColor)
            #anything draw to the screen
            bananaBtn.draw_button(self.WIN)
            counter_title = "Counter: " + str(game.bananas)
            counter_surface = self.FONT.render(counter_title, True, counter_color)
            self.WIN.blit(counter_surface, (600,100))

            pygame.display.flip()