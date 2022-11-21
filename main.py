from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
import UI


class YellowCircles(QWidget, UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paint = False

        self.pushButton.clicked.connect(self.button_click)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor('yellow'))
        count = randint(3, 10)
        for i in range(count):
            x, y = randint(0, self.size().width()), randint(0, self.size().height())
            w = h = randint(5, 200)
            qp.drawEllipse(x, y, w, h)
            qp.setBrush(QColor(
                randint(0, 255),
                randint(0, 255),
                randint(0, 255)))

    def button_click(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication([])
    wnd = YellowCircles()
    wnd.show()
    app.exec_()
