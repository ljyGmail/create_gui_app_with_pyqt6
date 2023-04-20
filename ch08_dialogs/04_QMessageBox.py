import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('QMessageBox')

        button = QPushButton('Press me for a dialog!')
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('I have a question!')
        dlg.setText('This is a simple dialog')
        button = dlg.exec()

        button = QMessageBox.StandardButton(button)

        if button == QMessageBox.StandardButton.Ok:
            print('OK!')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
