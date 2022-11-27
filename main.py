import sys

# как
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5 import uic

from random import randint, randrange


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow.ui', self)
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.func(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def func(self, qp):
        ran = randint(1, 7)
        for i in range(ran):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x = randint(0, 100)
            qp.drawEllipse(QPoint(randrange(0, 440), randrange(0, 331)), x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
