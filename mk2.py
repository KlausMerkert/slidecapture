import sys
from PySide.QtGui import *
 
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('drittes Fenster')

l = QLabel(w)
p = QPixmap(sys.argv[1])
l.resize(1245,891)
l.setPixmap(p)

w.show()

app.exec_()
sys.exit()