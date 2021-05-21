import os
import json
import function
import backend
import random
from fuzzywuzzy import process
import Levenshtein as lev
class Commands  :
    def __init__ (self,function,module,neuralNetwork) :
        self.function = function
        self.module = module
        self.neuralNetwork = neuralNetwork
        with open ("./Data/commands.json","r",encoding='utf8' ) as file:
            self.commands=json.load (file)   
            
    def Run (self,data) :
        data=data.lower()
        for key in self.commands.keys():
            for command in self.commands[key]:
                if data in self.commands[key][command]:
                    return self.Execute( command,key )
        #search komutları
        words=data.split(" ")
        for command in self.commands["search"].keys():
            for word in words:
                if word in self.commands["search"][command]:
                    words.remove(word)
                    search=""
                    for i in words:
                        search+=i+" "
                    return self.Execute(command,"search",search)
        """
        #Yapay sinir ağı analizi
        i = neuralNetwork.Analyse(data)
        if i == 1:
            data=data.lower()
            ratio = 0
            command = ""
            key=""
            for k in self.commands.keys():
                for com in self.commands[k]:
                    highest = process.extractOne(data,com)
                    if ratio<highest[1]:
                        ratio=highest[1]
                        command=highest[0]
                        key=k
            return self.Execute(command,key)
        elif i == 2:
            self.Execute2()
        else:
            data=data.lower()
            ratio = 0
            command = ""
            key=""
            for k in self.commands.keys():
                for com in self.commands[k]:
                    highest = process.extractOne(data,com)
                    if ratio<highest[1]:
                        ratio=highest[1]
                        command=highest[0]
                        key=k
            return self.Execute(command,key)
        """
        self.module.speak ("Ne dediğini anlayamadım.") 
        return 1   

    def Execute (self,command,commandType,search="") :
        #conversation
        if commandType=="sohbetCumleleri":
            if command=="nasilsin":
                self.module.speak(random.choice(self.commands["nasilsindonusCumleleri"]["donus"]))
            elif command=="tesekkur":
                self.module.speak("Rica ederim {}".format(self.function.GetInfo("name")))
            elif command=="iyiyim":
                self.module.speak("Hep iyi ol :)")
        #user update
        elif commandType=="update" :
            if command=="isimguncelle" :
                if self.function.UpdateInfo ("name"):
                    self.module.speak ("İsmini {} olarak güncelledim".format( self.function.GetInfo ("name")))   
            elif command=="yasguncelle" :
                if self.function.UpdateInfo( "age"):
                    self.module.speak("Yaşını {} olarak güncelledim.".format(self.function.GetInfo("age")))
            elif command=="sehirguncelle":
                if self.function.UpdateInfo("hometown","city"):
                    self.module.speak("Yaşadığın şehri {} olarak güncelledim.".format(self.function.GetInfo("hometown","city")))
            elif command=="dogumtarihiguncelle":
                if self.function.UpdateInfo("birthdate"):
                    self.module.speak("Doğum tarihini {} olarak güncelledim.".format(self.function.GetInfo("birthdate")))
            elif command=="okulguncelle":
                if self.function.UpdateInfo("university","faculty","department"):
                    self.module.speak("Okul bilgilerini {} olarak güncelledim.".format(self.function.GetInfo("university","faculty","department")))
            elif command=="meslekguncelle":
                if self.function.UpdateInfo("job"):
                    self.module.speak( "Meslek bilgilerini {} olarak güncelledim.".format(self.function.GetInfo("job")))
        #user info
        elif commandType=="getInfo" :
            if command=="meslekgetir" :
                self.module.speak(self.function.GetInfo ("job")) 
            if command=="yasgetir":
                self.module.speak(self.function.GetInfo("age"))
            if command=="sehirgetir":
                self.module.speak(self.function.GetInfo("hometown","city"))
            if command=="dogumtarihigetir":
                self.module.speak(self.function.GetInfo("birthdate"))
            if command=="okulbilgisigetir":
                self.module.speak(self.function.GetInfo("school","university"))
                self.module.speak(self.function.GetInfo("school","faculty"))
                self.module.speak(self.function.GetInfo("school","department"))
        #asistan info
        elif commandType=="asistanInfo" :
            if command=="kendinitanit" :
                self.module.speak ("Merhabalar benim adım Seda. Ben bir sesli asistanım" )
            elif command=="isimsoru" :
                self.module.speak ("Benim adım Seda" )
        #time functions
        elif commandType=="timeFunctions" :
            if command=="saatSoru" :
                self.module.speak ("Şu an saat "+self.function.Clock() )  
            elif command=="tarihSoru" :
                self.module.speak ("Bugün: "+self.function.Date())
        #quick search
        elif commandType=="quickSearch":
            if command=="havaDurumuSoru":
                self.module.speak("İşte bugünkü hava durumu:")
                self.function.Search("Hava durumu")
        #search
        elif commandType=="search":
            if command=="webAra":
                self.module.speak("İşte senin için bulduklarım: ")
                self.function.Search(search)
            if command=="musicAra":
                self.function.YoutubePlay(search)
        #close
        elif commandType=="close" :
            if command=="kapat" :
                self.module.speak ("Görüşmek üzere {}".format (self.function.GetInfo ("name")))   
                return 0
        else:
            self.module.speak ("Bir şeyler ters gitti" )
            return 0
        return 1