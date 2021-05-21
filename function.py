from audioop import tomono
import locale
import os
from datetime import datetime
from typing import ContextManager
import webbrowser
#from bs4 import BeautifulSoup
import backend
import time
import user
import json
import requests

locale.setlocale(locale.LC_ALL, '')
class Function:
    def __init__(self,backend):
        self.user=user.User()
        self.module=backend
    def Save(self):
        self.user.Export()

    def UpdateInfo(self,key,type=None):
        #key => dış anahtar
        #type => iç anahtar
        if type==None:
            if key in self.user.data.keys():
                if key =="name":
                    isim = self.module.hear("İsmin nedir ?")
                    self.user.data["name"]=isim
                elif key =="surname":
                    soyisim = self.module.hear("Soyismin nedir ?")
                    self.user.data["soyisim"]=soyisim
                elif key=="age":
                    yas=self.module.hear("Kaç yaşındasın ?")
                    self.user.data["age"]=yas
                elif key=="birthdate":
                    dogumtarihi=self.module.hear("Doğum tarihiniz nedir?")
                    self.user.data["birthdate"]=dogumtarihi
                else:
                    self.module.speak("Bir aksilik oldu.")
                    return 0
        else:
            if key in self.user.data.keys():
                if type in self.user.data[key].keys():
                    if key =="school":
                        if type == "university":
                            okul=self.module.hear("Hangi okula gidiyorsunuz?")
                            self.user.data[key][type]=okul
                        elif type =="faculty":
                            faculty = self.module.hear("Hangi fakültedesiniz?")
                            self.user.data[key][type]=faculty
                    elif key == "hometown":
                        if type == "city":
                            city=self.module.hear("Hangi şehirde yaşıyorsunuz?")
                            self.user.data[key][type]=city
                    else:
                        self.module.speak("Bir aksikilk oldu.")
                        return 0
        return 1
    def Clock(self):
        now = datetime.now()
        clk=(now.strftime("%H:%M:%S"))
        return clk
    
    def Date(self):
        now = datetime.now()
        date= datetime.strftime(now, '%x')
        return date
        
    def Search(self,search):
        url="https://www.google.com/search?q="+search
        webbrowser.get().open(url)
        
    def GetInfo(self,key,type=None):
        if type == None:
            if key in self.user.data.keys():
                return self.user.data[key]
            else:
                self.module.speak("Bilgi bulunamadı.")
        else:
            if key in self.user.data.keys():
                if type in self.user.data[key].keys():
                    return self.user.data[key][type]
            self.module.speak("Bilgi bulunamadı.")    