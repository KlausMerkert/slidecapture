import sys
import os
from PySide.QtGui import *
from PySide.QtCore import * # Qt.Checked
 
app = QApplication(sys.argv)

mainwindow = QWidget()
mainwindow.setWindowTitle('Dias einlesen')
mainwindow.resize(1600,1200)

h = 936

PicLabel = QLabel(mainwindow)
PicLabel.move(5,5)
PicLabel.resize(3*h//2, h)
aktuellInfo = QFileInfo('aktuell.jpg')
if aktuellInfo.size()>0:
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(h)
    PicLabel.setPixmap(p)
else:
    print('aktuell.jpg existiert nicht oder hat Größe 0!')

x  = 1500 # linke Kante der Eingabeelemente
y  = 20   # Abstand der Eingabeelemente von oben
dy = 30   # vertikaler Abstand der Eingabeelemente


def getExpComp():
    os.system('gphoto2 --get-config exposurecompensation > ExpComp.txt')
    datei = open('ExpComp.txt','r')
    s = datei.read(300)
    s2 = ''
    n = 50
    while s[n] != '\n':
    	s2 = s2+s[n]
    	n = n + 1
    datei.close()
    if s2 == ' »--debug«.':
        s2 = '-----'
    return s2
    

def getColorTemp():
    os.system('gphoto2 --get-config colortemperature > color.txt')
    datei = open('color.txt','r')
    s = datei.read(300)
    s = s[45:49]
    datei.close()
    if s == 'ptio':
        s = '-----'
    return s


def getCamera():
    os.system('gphoto2 --auto-detect > camera.txt')
    datei = open('camera.txt','r')
    s = datei.read(300)
    s = s[107:-17]
    if s == '':
        s = '-----'
    datei.close()
    return s


def getCreateDate():
    os.system('exiftool -CreateDate aktuell.jpg > CreateDate.txt')
    datei = open('CreateDate.txt','r')
    s = datei.read(100)
    s = s.replace('Create Date                     :','')
    s = s[:-1]
    datei.close()
    return s


def getDateTimeOriginal():
    os.system('exiftool -datetimeoriginal aktuell.jpg > datetimeoriginal.txt')
    datei = open('datetimeoriginal.txt','r')
    s = datei.read(100)
    s = s.replace('Date/Time Original              :','')
    s = s[:-1]
    datei.close()
    return s
    

def getLabelWidth(Label):
    return Label.fontMetrics().boundingRect(Label.text()).width()

   
def showDateTimeOriginal():
    lDateTimeOriginal.setText('Date/Time Original: '+getDateTimeOriginal())


def getKeywords():
    os.system('exiftool -keywords aktuell.jpg > keywords.txt')
    datei = open('keywords.txt','r')
    s = datei.read(100)
    s = s.replace('Keywords                        : ','')
    s = s[:-1]
    datei.close()
    return s
    
    
def showKeywords():
    lKeywords.setText('Keywords: '+getKeywords())


def on_Dia():
    if cSave.checkState() == Qt.Checked:
    	  on_Save()
        # print('cSave checked')
    if aktuellInfo.exists():
        os.system('rm aktuell.jpg')
    os.system('gphoto2 --capture-image-and-download --filename aktuell.jpg')
    if cInvert.checkState() == Qt.Checked:
        on_Invert()
    if cTurnMirror.checkState() == Qt.Checked:
        on_TurnMirror()
    if cTimeTag.checkState() == Qt.Checked:
        on_TimeTag()
    if cKeywords.checkState() == Qt.Checked:
        on_Keywords()
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(h)
    PicLabel.setPixmap(p)
    showDateTimeOriginal()
    showKeywords()     
    print('Aufruf von on_Dia!')
    
           	
bDia = QPushButton(mainwindow)
bDia.setText('mache Foto')
bDia.move(x,y)
bDia.clicked.connect(on_Dia)

def on_Invert():
    s = getKeywords()
    os.system('convert -negate -compress lossless aktuell.jpg t1.jpg')
    os.system('exiftool -keywords="'+s+'" t1.jpg')
    os.system('jpegtran -grayscale -copy all t1.jpg > t2.jpg')
    os.system('mv t2.jpg aktuell.jpg')
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(h)
    PicLabel.setPixmap(p)
    showDateTimeOriginal()
    showKeywords()
    print('invertiere das Foto!')
    	
bInvert = QPushButton(mainwindow)
bInvert.setText('invertiere')
bInvert.move(x,y+1*dy)
bInvert.clicked.connect(on_Invert)

def on_Mirror():
    os.system('jpegtran -flip horizontal -copy all aktuell.jpg > temp.jpg')
    os.system('mv temp.jpg aktuell.jpg')
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(h)
    PicLabel.setPixmap(p)
    showDateTimeOriginal()
    showKeywords()
    print('spiegele das Foto!')
    	
bMirror = QPushButton(mainwindow)
bMirror.setText('spiegele')
bMirror.move(x,y+2*dy)
bMirror.clicked.connect(on_Mirror)

def on_Turn():
    os.system('jpegtran -rotate 90 -copy all aktuell.jpg > temp.jpg')
    os.system('mv temp.jpg aktuell.jpg')
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(h)
    PicLabel.setPixmap(p)
    showDateTimeOriginal()
    showKeywords()
    print('drehe das Foto!')
    	
bTurn = QPushButton(mainwindow)
bTurn.setText('drehe')
bTurn.move(x,y+3*dy)
bTurn.clicked.connect(on_Turn)

def on_TurnMirror():
    os.system('jpegtran -rotate 180 -copy all aktuell.jpg > t1.jpg')
    os.system('jpegtran -flip horizontal -copy all t1.jpg > t2.jpg')
    os.system('mv t2.jpg aktuell.jpg')
    p = QPixmap('aktuell.jpg')
    p = p.scaledToHeight(h)
    PicLabel.setPixmap(p)
    showDateTimeOriginal()
    showKeywords()
    print('richte das Dia!')
    	
bTurnMirror = QPushButton(mainwindow)
bTurnMirror.setText('korr. Dia')
bTurnMirror.move(x,y+4*dy)
bTurnMirror.clicked.connect(on_TurnMirror)

eJahr = QLineEdit(mainwindow)
eJahr.move(x,y+5*dy)
eJahr.setInputMask('0000')
eJahr.setText('1983')
eJahr.setFixedWidth(50)
lJahr = QLabel(mainwindow)
lJahr.setText('Jahr')
lJahr.move(x-getLabelWidth(lJahr),y+5*dy+5)

eMonat = QLineEdit(mainwindow)
eMonat.move(x,y+6*dy)
eMonat.setInputMask('00')
eMonat.setText('05')
eMonat.setFixedWidth(50)
lMonat = QLabel(mainwindow)
lMonat.setText('Monat')
lMonat.move(x-getLabelWidth(lMonat),y+6*dy+5)

eTag = QLineEdit(mainwindow)
eTag.move(x,y+7*dy)
eTag.setInputMask('00')
eTag.setText('17')
eTag.setFixedWidth(50)
lTag = QLabel(mainwindow)
lTag.setText('Tag')
lTag.move(x-getLabelWidth(lTag),y+7*dy+5)

def on_TimeTag():
    year = eJahr.text()
    month = eMonat.text()
    day = eTag.text()
    hms = getDateTimeOriginal()[-9:]
    os.system('exiftool -datetimeoriginal="'+year+':'+month+':'+day+' '+hms+'" aktuell.jpg')
    showDateTimeOriginal()
    print('Setze Zeit! Jahr = '+year+', Monat = '+month+', Tag = '+day+', Zeit = '+hms)
    	
bTimeTag = QPushButton(mainwindow)
bTimeTag.setText('setze Zeit')
bTimeTag.move(x,y+8*dy)
bTimeTag.clicked.connect(on_TimeTag)

eKeywords = QLineEdit(mainwindow)
eKeywords.move(x,y+9*dy)
eKeywords.setText('Hausbau')
eKeywords.setFixedWidth(90)
lKeywords = QLabel(mainwindow)
lKeywords.setText('Keywords')
lKeywords.move(x-getLabelWidth(lKeywords),y+9*dy+5)

def on_Keywords():
    os.system('exiftool -keywords="'+eKeywords.text()+'" aktuell.jpg')
    showKeywords()
    print('setze Keywords!')

bKeywords = QPushButton(mainwindow)
bKeywords.setText('setze Tags')
bKeywords.move(x,y+10*dy)
bKeywords.clicked.connect(on_Keywords)

eName = QLineEdit(mainwindow)
eName.move(x,y+11*dy)
eName.setText('dia00000')
eName.setFixedWidth(90)
lName = QLabel(mainwindow)
lName.setText('Name')
lName.move(x-getLabelWidth(lName),y+11*dy+5)

# fFile = QFile(mainwindow) unnötig, da QFile.exists statisch

def on_Save():
    filename = eName.text()+'.jpg'
    if QFile.exists(filename):
        msgBox = QMessageBox()
        msgBox.setText(filename+' existiert bereits!')
        msgBox.exec_()
        print(filename+' existiert bereits!')
    else:
        os.system('cp aktuell.jpg '+filename)
        s = eName.text()[:-5]
        n = int(eName.text()[-5:])
        n = n+1
        eName.setText(s+'{:0>5d}'.format(n))
    print('Aufruf von on_Save!')

bSave = QPushButton(mainwindow)
bSave.setText('speichere')
bSave.move(x,y+12*dy)
bSave.clicked.connect(on_Save)

def on_Camera():
    lCamera.setText('Kamera: '+getCamera())
    eExpComp.setText(getExpComp())
    eColorTemperature.setText(getColorTemp())

bCamera = QPushButton(mainwindow)
bCamera.setText('Kamera')
bCamera.move(x,y+21*dy)
bCamera.clicked.connect(on_Camera)

# sExpComp = QSlider(mainwindow)
# sExpComp.setOrientation(Qt.Horizontal)
# sExpComp.move(x,y+22*dy)

eExpComp = QLineEdit(mainwindow)
eExpComp.setFixedWidth(90)
eExpComp.move(x,y+22*dy)
eExpComp.setText(getExpComp())

def on_ExpComp():
    os.system('gphoto2 --set-config exposurecompensation='+eExpComp.text()) 

bExpComp = QPushButton(mainwindow)
bExpComp.setText('ExpComp')
bExpComp.move(x,y+23*dy)
bExpComp.clicked.connect(on_ExpComp)

eColorTemperature = QLineEdit(mainwindow)
eColorTemperature.setFixedWidth(90)
eColorTemperature.move(x,y+24*dy)
eColorTemperature.setText(getColorTemp())

def on_ColorTemperature():
    os.system('gphoto2 --set-config colortemperature='+eColorTemperature.text()) 

bColorTemperature = QPushButton(mainwindow)
bColorTemperature.setText('FarbTemp.')
bColorTemperature.move(x,y+25*dy)
bColorTemperature.clicked.connect(on_ColorTemperature)

# Checkboxes für Seiteneffekte

lSideEffect1 = QLabel(mainwindow)
lSideEffect1.setText("Seiteneffekte von")
lSideEffect1.move(x-35,y+13.5*dy)

lSideEffect2 = QLabel(mainwindow)
lSideEffect2.setText("'mache Foto'")
lSideEffect2.move(x-35,y+14*dy)

cSave = QCheckBox(mainwindow)
cSave.setText('speichere')
cSave.move(x,y+15*dy)
# cSave.setCheckState(Qt.Checked)

cInvert = QCheckBox(mainwindow)
cInvert.setText('invertiere')
cInvert.move(x,y+16*dy)
# cInvert.setCheckState(Qt.Checked)

cTurnMirror = QCheckBox(mainwindow)
cTurnMirror.setText('korr. Dia')
cTurnMirror.move(x,y+17*dy)
cTurnMirror.setCheckState(Qt.Checked)

cTimeTag = QCheckBox(mainwindow)
cTimeTag.setText('setze Zeit')
cTimeTag.move(x,y+18*dy)
cTimeTag.setCheckState(Qt.Checked)

cKeywords = QCheckBox(mainwindow)
cKeywords.setText('setze Tags')
cKeywords.move(x,y+19*dy)
cKeywords.setCheckState(Qt.Checked)

# Fußleiste

lDateTimeOriginal = QLabel(mainwindow)
lDateTimeOriginal.setFixedWidth(300)
if aktuellInfo.size() > 0:
    lDateTimeOriginal.setText('Date/Time Original: '+getDateTimeOriginal())
else:
    lDateTimeOriginal.setText('Date/Time Original: ?')
lDateTimeOriginal.move(10,h+10)

lKeywords = QLabel(mainwindow)
lKeywords.setFixedWidth(300)
if aktuellInfo.size() > 0:
    lKeywords.setText('Keywords: '+getKeywords())
else:
    lKeywords.setText('Keywords: ?')
lKeywords.move(300,h+10)

lCamera = QLabel(mainwindow)
lCamera.setFixedWidth(300)
lCamera.setText('Kamera: '+getCamera())
lCamera.move(900,h+10)

# -----------------------

mainwindow.show()

app.exec_()
sys.exit()