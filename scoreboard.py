import pygame
import json
from text import Text

pygame.init()
FONT = pygame.font.Font(None, 32)


class Scoreboard:
    def __init__(self,x,y,w,h,title):
        self.rect = pygame.Rect(x,y,w,h)
        self.box_color = (117, 59, 0)
        self.text_color = (0,0,0)
        self.title = title
        self.title_surface = FONT.render(self.title,True, self.text_color)

    def users_score(self):
        #display top 5
        data = open("user_details.txt", "r")
        top_five = []
        player_text = Text()
        player_blit_list = []
        player_blit = []
        y_increment = 12
        account_list = []
        for account in data:
            if(account != ""):
                dict_account = json.loads(account)
                account_list.append(dict_account)
        data.close()
        top_five = sorted(account_list, key=lambda d: d['bananas'], reverse=True)
        for account in top_five:
            y_increment += 17
            playersurface = player_text.createText(self.text_color,account["username"])
            player_blit = [playersurface,(self.rect.x+5,self.rect.y+y_increment)]
            player_blit_list.append(player_blit)
        
        return player_blit_list
        



    def draw(self,screen):
        blit_list = []
        blit_list = self.users_score()

        #draws player names
        for blit in blit_list:
            screen.blit(blit[0],blit[1])
            
        #draws scoreboard box and title and underline
        screen.blit(self.title_surface,(self.rect.x+5,self.rect.y+5))
        pygame.draw.line(screen,self.text_color,(self.rect.x+3,self.rect.y+27),(self.rect.x+130,self.rect.y+27),2)
        pygame.draw.rect(screen,self.box_color, self.rect,2)
        