from PySide.QtGui import *
 
app = QApplication([])

w = QWidget()
w.setWindowTitle('erstes Fenster')
w.resize(200,150)
w.show()

app.exec_()
