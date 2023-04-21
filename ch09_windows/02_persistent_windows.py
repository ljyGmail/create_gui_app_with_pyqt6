import sys
from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel(f'Another Window {randint(0,100)}')
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.w = AnotherWindow()

        self.button = QPushButton('Push for Window')
        self.button.clicked.connect(self.show_new_window)

        self.setCentralWidget(self.button)

    def show_new_window(self):
        self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
