import sys
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from color_widget import Color


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Tab-Like Stack Layout')

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)

        btn = QPushButton('red')
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color('red'))

        btn = QPushButton('green')
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color('green'))

        btn = QPushButton('purple')
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color('purple'))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stack_layout.setCurrentIndex(2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
