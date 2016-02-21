from PySide.QtGui import *
 
app = QApplication([])

w = QWidget()
w.setWindowTitle('zweites Fenster')
w.resize(200,150)

l = QLabel(w)
l.setText('Hallo, Welt!')
l.move(40,50)

w.show()

app.exec_()
