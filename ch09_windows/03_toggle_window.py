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
        self.button.clicked.connect(self.toggle_window)

        self.setCentralWidget(self.button)

    def toggle_window(self):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()
