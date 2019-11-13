import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.q = 0
        self.pshb.clicked.connect(self.run)

    def run(self):
        self.q = 1
        self.update()

    def paintEvent(self, event):
        if self.q == 1:
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            r = random.randint(20, 100)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(x, y, r, r)
            qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())