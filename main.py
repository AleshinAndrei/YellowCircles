import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QPoint
from random import choice


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.drawing = False

    def initUI(self):
        self.setGeometry(400, 400, 600, 600)
        self.setWindowTitle('YellowCircles')
        self.pb_draw.clicked.connect(self.draw)

    def draw(self):
        self.drawing = True
        self.update()

    def paintEvent(self, event):
        if self.drawing:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QPen(QColor(255, 255, 0)))
            for i in range(5):
                x, y = choice(range(self.size().width())), choice(range(self.size().height()))
                r = choice(range(1, 50))
                qp.drawEllipse(QPoint(x, y), r, r)
            qp.end()
            self.drawing = False


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
