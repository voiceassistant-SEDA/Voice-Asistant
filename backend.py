from gtts import gTTS
import PyQt5.QtCore as coremodule
import PyQt5.QtMultimedia as multimedia
import speech_recognition as sr

import sys
class Backend:
    mic=sr.Microphone()
    r=sr.Recognizer()
    
    def __init__(self):
        self.app = coremodule.QCoreApplication(sys.argv)
        self.sleep_mode = False
    def Connection(self,ex,function):
        self.ex=ex
        self.function = function
    def sleep(self):
        print("Uyku modunu açmak için ismimi söyle")
        self.ex.AddBotText("Uyku modunu açmak için ismimi söyle")
        self.sleep_mode=True
        command=""
        while command!="seda":
            command=self.hear().lower()
        self.speak("Merhaba")
        self.sleep_mode=False

    def hear(self,response=""):
        if response !="":
            self.speak(response)

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            #print("Arka plan gürültüsü:" + str(r.energy_threshold))
            if self.sleep_mode == False:
                print("->Seda Dinliyor...")
            try:
                ses = self.r.listen(source,timeout=5,phrase_time_limit=5)
                yazi = self.r.recognize_google(ses, language="tr-tr")
                if self.sleep_mode==False:
                    print(self.function.GetInfo("name")+":"+yazi)
                    self.ex.AddUserText(self.function.GetInfo("name"),yazi)

            except sr.WaitTimeoutError:
                if self.sleep_mode==False:
                    print("Dinleme zaman aşımına uğradı")
                yazi="&&"
            except sr.UnknownValueError:
                if self.sleep_mode==False:                
                    print("Ne dediğini anlayamadım")
                yazi="&&"
            except sr.RequestError:
                if self.sleep_mode==False:
                    print("İnternete bağlanamıyorum")
                yazi="&&"
            finally:
                return yazi

    def playSound(self, audioPath):
        url = coremodule.QUrl.fromLocalFile(audioPath)
        content = multimedia.QMediaContent(url)
        player = multimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(self.app.quit)
        self.app.exec()

    def speak(self, audioString):
        tts = gTTS(text=audioString, lang='tr')
        print("Seda:"+audioString)
        self.ex.AddUserText("Seda",audioString)
        tts.save("audio.mp3")
        # os.system("audio.mp3")
        self.playSound("audio.mp3")

    def recordAudio(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio, language='tr-tr')
            data = data.lower()
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Ne dediğini anlamadım")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data