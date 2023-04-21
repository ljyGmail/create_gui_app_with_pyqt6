import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel('Click in this window')

        # self.setMouseTracking(True)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        # registered only when mouse button is pressed down
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e):
        # self.label.setText('mousePressEvent')
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText('mousePressEvent LEFT')
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('mousePressEvent MIDDLE')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('mousePressEvent RIGHT')

    def mouseReleaseEvent(self, e):
        # self.label.setText('mouseReleaseEvent')
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText('mouseReleaseEvent LEFT')
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('mouseReleaseEvent MIDDLE')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('mouseReleaseEvent RIGHT')

    def mouseDoubleClickEvent(self, e):
        # self.label.setText('mouseDoubleClickEvent')
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText('mouseDoubleClickEvent LEFT')
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('mouseDoubleClickEvent MIDDLE')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('mouseDoubleClickEvent RIGHT')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
