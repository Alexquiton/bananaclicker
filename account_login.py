import json

class Account:
    def __init__(self, username, password, id):
        self.username = username
        self.password = password
        self.id = id
    
    def loadlist(self):
        data = open("user_details.txt")
        account_list = []
        for account in data:
            if(account != ""):
                dict_account = json.loads(account)
                account_list.append(dict_account)
        return account_list

    

    def save(self):
        self.loadlist()