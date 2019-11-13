import sys
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
import numpy as np


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.pshb = QtWidgets.QPushButton(Form)
        self.pshb.setGeometry(QtCore.QRect(370, 280, 93, 28))
        self.pshb.setObjectName("pshb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pshb.setText(_translate("Form", "Окружность"))


class MyWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

    def random_color(self):
        return tuple(np.random.choice(range(256), size=3))


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())