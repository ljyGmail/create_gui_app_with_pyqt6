import sys
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('QDialog filters')

        button1 = QPushButton('Open File')
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        filters = "Portable Network Graphics files (*.png);;Comma Separated Values (*.csv);;All files (*.*)"
        print('Filters are', filters)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self, filter=filters)

        print('Result:', filename, selected_filter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
