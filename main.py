import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
import numpy as np


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
            a, b, c = self.random_color()
            qp.setBrush(QColor(a, b, c))
            qp.drawEllipse(x, y, r, r)
            qp.end()

    def random_color(self):
        return tuple(np.random.choice(range(256), size=3))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())