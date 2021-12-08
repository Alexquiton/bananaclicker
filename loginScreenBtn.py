import pygame
import json
from text import Text

pygame.init()
color_active = (150, 150, 150)
placeholder_color = (150,150,150)
##############################################
# Login Button Class
# Functions:
# __init__(x,y,w,h,placeholder):
# @params: x,y,w,h,placeholder
# x and y refer to the positon the button is on the window
# w and h refer to the width and height of the button
# placeholder refers to the text inside of the box that displays what input box it is
# @bref: initalizes the position of the button and the dimensions along with the title
# of the button
# @returns: none
#
# handle_event(event):
# @params: event
# event is the action that the user is inputing to the system
# thing such as mouse down or keystrokes
# @bref: takes in user input and sets variables accordingly to the input
# return: none
#
# draw_button(screen):
# @params: WIN
# WIN is the window of the main screen that is displaying
# @breif: draws the button onto the screen
# @return: none
#
# load():
# @params: none
# @bref: opens data from user_details.txt and reads it,
# then takes each line in the file and converts it from a string
# to a diction using json and appends it to a list which stores
# a list of all the users data in a dictionary form
# @returns: the list of accounts in dictionary form
#
# login(username,password):
# @params: username, password
# username is the username that the user inputs on the login screen
# password is the password that the user inputs on the login screen
# @bref: When the user hits the login button it goes through the account list
# from the function load() and checks if the there is an account that exist with that user
# name and if the password is wrong
# @returns: a a list in which stores a bool in the first slot showing that the
# login checks out with the data and returns the account the user is trying to
# login into, also returns two false logins in which returns a list that contains
# false meaning that the login isn't correct and in the second slot is the error
# message depending on what happened
# 
# register(username,password):
# @params: username, password
# username is what the user inputs on the login screen
# password is what the user inputs on the login screen
# @bref: When the user hits the register button it goes through the account list
# from the function load() and checks if there is no account with the same username
# or if the user inputs invalid register credientials like no username or no password
# and if it checks out as good register it will save the account in a dictionary and
# then open up user_details.txt and save it there with json that converts it to a string
# on its own separate line
# @return: returns a list that indicates if it is a correct register or false in the first slot
# and includes the error in the second slot, if it is a correct reigster it returns a list
# with only true
#################################################################
class LoginScreenBtn:
    
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
            
    def draw_button(self,WIN):
        WIN.blit(self.placeholder_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(WIN,self.color, self.rect, 2)
    
    def load(self):
        data = open("user_details.txt","r")
        account_list = []
        for account in data:
            if(account != ""):
                dict_account = json.loads(account)
                account_list.append(dict_account)
        data.close()
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
    
    def register(self,username,password):
        account_list = self.load()
        false_register = []
        correct_register = []
        taken_username = False
        for account in account_list:
            if(account["username"] == username):
                taken_username = True
                break
        if(len(username) == 0 or len(password) == 0):
            false_register.append(False)
            false_register.append("Invalid username or password")
            return false_register
        if(taken_username == True):
            false_register.append(False)
            false_register.append("Username Already Taken")
            return false_register
        else:
            account = {
                "username": username,
                "password": password,
                "bananas": 0,
                "multiClicks": 0
            }
            data = open("user_details.txt","a")
            data.write("\n")
            json.dump(account,data)
            data.close
            correct_register.append(True)
            return correct_register
        


    
        