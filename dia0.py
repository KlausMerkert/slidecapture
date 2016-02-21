import sys
import os
from PySide.QtGui import *
 
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('Dias einlesen')
w.resize(1200,800)

l = QLabel(w)
l.move(5,5)
l.resize(1024,768)
p = QPixmap('aktuell.jpg')
p = p.scaledToHeight(768)
l.setPixmap(p)

x  = 1100
y  = 20
dy = 30

def lWidth(lName):
    return lName.fontMetrics().boundingRect(lName.text()).width()
    
def showCreateDate():
    os.system('exiftool -CreateDate aktuell.jpg > CreateDate.txt')
    datei = open('CreateDate.txt','r')
    s = datei.read(100)
    s = s.replace('Create Date                     :','Create Date:')
    datei.close()
    lCreateDate.setText(s)
    
def showKeywords():
    os.system('exiftool -mwg:keywords aktuell.jpg > keywords.txt')
    datei = open('keywords.txt','r')
    s = datei.read(100)
    s = s.replace('Keywords                        :','Keywords:')
    datei.close()
    lKeywords.setText(s)

def on_Dia():
    print('mache ein Foto!')
    showCreateDate()
    showKeywords()
    	
bDia = QPushButton(w)
bDia.setText('mache Foto')
bDia.move(x,y)
bDia.clicked.connect(on_Dia)

def on_Invert():
    print('invertiere das Foto!')
    	
bInvert = QPushButton(w)
bInvert.setText('invertiere')
bInvert.move(x,y+1*dy)
bInvert.clicked.connect(on_Invert)

def on_Mirror():
    os.system('convert aktuell.jpg -flop aktuell.jpg')
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(768)
    l.setPixmap(p)
    print('spiegele das Foto!')
    	
bMirror = QPushButton(w)
bMirror.setText('spiegele')
bMirror.move(x,y+2*dy)
bMirror.clicked.connect(on_Mirror)

def on_Turn():
    print('drehe das Foto!')
    	
bTurn = QPushButton(w)
bTurn.setText('drehe')
bTurn.move(x,y+3*dy)
bTurn.clicked.connect(on_Turn)

eJahr = QLineEdit(w)
eJahr.move(x,y+4*dy)
eJahr.setInputMask('0000')
eJahr.setText('1983')
eJahr.setFixedWidth(50)
lJahr = QLabel(w)
lJahr.setText('Jahr')
lJahr.move(x-lWidth(lJahr),y+4*dy+5)

eMonat = QLineEdit(w)
eMonat.move(x,y+5*dy)
eMonat.setInputMask('00')
eMonat.setText('05')
eMonat.setFixedWidth(50)
lMonat = QLabel(w)
lMonat.setText('Monat')
lMonat.move(x-lWidth(lMonat),y+5*dy+5)

eTag = QLineEdit(w)
eTag.move(x,y+6*dy)
eTag.setInputMask('00')
eTag.setText('17')
eTag.setFixedWidth(50)
lTag = QLabel(w)
lTag.setText('Tag')
lTag.move(x-lWidth(lTag),y+6*dy+5)

def on_TimeTag():
    print('setze TimeTag!')
    	
bTimeTag = QPushButton(w)
bTimeTag.setText('setze Zeit')
bTimeTag.move(x,y+7*dy)
bTimeTag.clicked.connect(on_TimeTag)

eKeywords = QLineEdit(w)
eKeywords.move(x,y+8*dy)
eKeywords.setText('Hausbau')
eKeywords.setFixedWidth(90)
lKeywords = QLabel(w)
lKeywords.setText('Keywords')
lKeywords.move(x-lWidth(lKeywords),y+8*dy+5)

def on_Keywords():
    print('setze Keywords!')
    	
bKeywords = QPushButton(w)
bKeywords.setText('setze Tags')
bKeywords.move(x,y+9*dy)
bKeywords.clicked.connect(on_Keywords)

eName = QLineEdit(w)
eName.move(x,y+10*dy)
eName.setText('dia00000')
eName.setFixedWidth(90)
lName = QLabel(w)
lName.setText('Name')
lName.move(x-lWidth(lName),y+10*dy+5)

lCreateDate = QLabel(w)
lCreateDate.setFixedWidth(300)
lCreateDate.setText('CreateDate: ?')
lCreateDate.move(10,778)

lKeywords = QLabel(w)
lKeywords.setFixedWidth(400)
lKeywords.setText('Keywords: ?')
lKeywords.move(320,778)

w.show()

app.exec_()
sys.exit()