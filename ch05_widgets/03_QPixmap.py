import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('QPixmap')

        widget = QLabel('Hello')
        widget.setPixmap(QPixmap('data/ch05/otje.jpg'))

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
