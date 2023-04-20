import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)

from color_widget import Color


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('QTabWidget')

        tabs = QTabWidget()
        # tabs.setDocumentMode(True) # only has effect on macOS
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)

        for color in ['red', 'green', 'blue', 'yellow']:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
