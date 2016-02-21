import sys
import os
from PySide.QtGui import *
 
app = QApplication(sys.argv)

mainwindow = QWidget()
mainwindow.setWindowTitle('Dias einlesen')
mainwindow.resize(1200,800)

PicLabel = QLabel(mainwindow)
PicLabel.move(5,5)
PicLabel.resize(1024, 768)
p = QPixmap('aktuell.jpg')
p = p.scaledToHeight(768)
PicLabel.setPixmap(p)

x  = 1100 # linke Kante der Eingabeelemente
y  = 20   # Abstand der Eingabeelemente von oben
dy = 30   # vertikaler Abstand der Eingabeelemente


def getLabelWidth(Label):
    return Label.fontMetrics().boundingRect(Label.text()).width()

   
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
    	
bDia = QPushButton(mainwindow)
bDia.setText('mache Foto')
bDia.move(x,y)
bDia.clicked.connect(on_Dia)

def on_Invert():
    print('invertiere das Foto!')
    	
bInvert = QPushButton(mainwindow)
bInvert.setText('invertiere')
bInvert.move(x,y+1*dy)
bInvert.clicked.connect(on_Invert)

def on_Mirror():
    os.system('convert aktuell.jpg -flop aktuell.jpg')
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(768)
    PicLabel.setPixmap(p)
    print('spiegele das Foto!')
    	
bMirror = QPushButton(mainwindow)
bMirror.setText('spiegele')
bMirror.move(x,y+2*dy)
bMirror.clicked.connect(on_Mirror)

def on_Turn():
    print('drehe das Foto!')
    	
bTurn = QPushButton(mainwindow)
bTurn.setText('drehe')
bTurn.move(x,y+3*dy)
bTurn.clicked.connect(on_Turn)

eJahr = QLineEdit(mainwindow)
eJahr.move(x,y+4*dy)
eJahr.setInputMask('0000')
eJahr.setText('1983')
eJahr.setFixedWidth(50)
lJahr = QLabel(mainwindow)
lJahr.setText('Jahr')
lJahr.move(x-getLabelWidth(lJahr),y+4*dy+5)

eMonat = QLineEdit(mainwindow)
eMonat.move(x,y+5*dy)
eMonat.setInputMask('00')
eMonat.setText('05')
eMonat.setFixedWidth(50)
lMonat = QLabel(mainwindow)
lMonat.setText('Monat')
lMonat.move(x-getLabelWidth(lMonat),y+5*dy+5)

eTag = QLineEdit(mainwindow)
eTag.move(x,y+6*dy)
eTag.setInputMask('00')
eTag.setText('17')
eTag.setFixedWidth(50)
lTag = QLabel(mainwindow)
lTag.setText('Tag')
lTag.move(x-getLabelWidth(lTag),y+6*dy+5)

def on_TimeTag():
    print('setze TimeTag!')
    	
bTimeTag = QPushButton(mainwindow)
bTimeTag.setText('setze Zeit')
bTimeTag.move(x,y+7*dy)
bTimeTag.clicked.connect(on_TimeTag)

eKeywords = QLineEdit(mainwindow)
eKeywords.move(x,y+8*dy)
eKeywords.setText('Hausbau')
eKeywords.setFixedWidth(90)
lKeywords = QLabel(mainwindow)
lKeywords.setText('Keywords')
lKeywords.move(x-getLabelWidth(lKeywords),y+8*dy+5)

def on_Keywords():
    print('setze Keywords!')
    	
bKeywords = QPushButton(mainwindow)
bKeywords.setText('setze Tags')
bKeywords.move(x,y+9*dy)
bKeywords.clicked.connect(on_Keywords)

eName = QLineEdit(mainwindow)
eName.move(x,y+10*dy)
eName.setText('dia00000')
eName.setFixedWidth(90)
lName = QLabel(mainwindow)
lName.setText('Name')
lName.move(x-getLabelWidth(lName),y+10*dy+5)

lCreateDate = QLabel(mainwindow)
lCreateDate.setFixedWidth(300)
lCreateDate.setText('CreateDate: ?')
lCreateDate.move(10,778)

lKeywords = QLabel(mainwindow)
lKeywords.setFixedWidth(400)
lKeywords.setText('Keywords: ?')
lKeywords.move(320,778)

mainwindow.show()

app.exec_()
sys.exit()