import os
import json
class User():
    def __init__(self):
        self.Import()  
    def Export(self):
        with open("./Data/user.json","r+", encoding='utf8') as file:
            json.dump(self.data,file,indent = 4,ensure_ascii=False)     
    def Import(self):
        with open("./Data/user.json","r",encoding='utf8') as file:
            self.data=json.load(file)

