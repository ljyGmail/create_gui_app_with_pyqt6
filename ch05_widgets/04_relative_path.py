import os
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


basedir = os.path.dirname(__file__)
print('Current working folder:', os.getcwd())
print('Paths are relative to:', basedir)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Relative Path')

        widget = QLabel('Hello')
        widget.setPixmap(QPixmap(os.path.join(
            basedir, '../data/ch05/otje.jpg')))

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
