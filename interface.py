import sys
from PyQt5 import QtCore 
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QListWidget,QListWidgetItem 
from PyQt5.QtGui import QFont, QIcon

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'SEDA'
        self.left = 50
        self.top = 50
        self.width = 480
        self.height = 640
        
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.initUI()
        self.setFixedSize(480, 640)
        self.setStyleSheet("background-color: #292929; color:white;")

        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        

        self.textbox2 = QtWidgets.QTextEdit(self)
        self.textbox2.move(20,60)
        self.textbox2.resize(440,500)
        self.textbox2.setFont(QFont("Calibra",12))
       

        self.label1 = QtWidgets.QLabel("SEDA",self)
        self.label1.move(200,20)
        self.label1.setFont(QFont("Arial",16))
        self.button = QtWidgets.QPushButton("Push",self)
        self.button.setGeometry(200,580,60,40)
        #self.button.clicked.connect(self.buttonClicked)
        
        self.show()


           
    def AddUserText(self,name,text):
        self.textbox2.append(name+":"+text)

    def AddBotText(self,text):
        self.textbox2.append(text)
