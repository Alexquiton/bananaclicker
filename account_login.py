import json

class Account:
    id = -1
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def loadlist(self):
        data = open("user_details.txt")
        account_list = []
        for account in data:
            if(account != ""):
                dict_account = json.loads(account)
                account_list.append(dict_account)
        return account_list

    

    def register(self):
        account_list = self.loadlist()
        for account in account_list:
            if(account["username"] == self.username):
                print("there is already an account under that username")
                return
        
    

    def login(self):
        login_access = False
        account_list = self.loadlist()
        for account in account_list:
            if(account["username"] == self.username and account["password"] == self.password):
                login_access = True
                break
        if(login_access == True):
            print("login sucessful")
            
        else:
            print("wrong username or password")
