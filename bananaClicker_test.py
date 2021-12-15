from logging import log
from types import NoneType
import unittest, game_button, game_screen, game, inputbox, login_screen, loginScreenBtn,scoreboard,text
import pygame
class TestBananaClicker(unittest.TestCase):
    #game_screen test return correct accounts
    def test_load_accounts(self):
        test1 = [{'username': 'dev', 'password': 'dawg', 'bananas': 164, 'multiClicks': 11}, {'username': 'test_1', 'password': 'testpass', 'bananas': 20, 'multiClicks': 1}]
        self.assertEqual(game_screen.Game_Screen.load_accounts(),test1)
    
    def test_login_buttonTrue(self):
        login_button = loginScreenBtn.LoginScreenBtn
        self.assertEqual(loginScreenBtn.LoginScreenBtn.login(login_button,"dev","dawg"),[True,{'username': 'dev', 'password': 'dawg', 'bananas': 164, 'multiClicks': 11}])

    def test_login_buttonFalse(self):
        login_button = loginScreenBtn.LoginScreenBtn
        self.assertEqual(loginScreenBtn.LoginScreenBtn.login(login_button,"dev","d"),[False,"Wrong password"])

    def test_register_buttonTrue(self):
        register_button = loginScreenBtn.LoginScreenBtn
        self.assertEqual(loginScreenBtn.LoginScreenBtn.register(register_button,"newAccount","newPass"),[True])
    
    def test_register_buttonFalse(self):
        register_button = loginScreenBtn.LoginScreenBtn
        self.assertEqual(loginScreenBtn.LoginScreenBtn.register(register_button,"",""),[False,"Invalid username or password"])
        self.assertEqual(loginScreenBtn.LoginScreenBtn.register(register_button,"dev","dawg"),[False,"Username Already Taken"])

    

