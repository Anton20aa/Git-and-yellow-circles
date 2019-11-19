from tkinter import Image
from PyQt5 import uic
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow)
import sys
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.create_circles)
        self.image = Image.new("RGBA", (700, 700), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)

    def create_circles(self):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        d = random.randint(30, 300)
        self.draw.ellipse((x, y, x + d, y + d), outline='red')
        # draw.ellipse((10,10,300,300), outline="red")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())