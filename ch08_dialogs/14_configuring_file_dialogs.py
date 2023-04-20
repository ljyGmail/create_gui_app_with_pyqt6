import os
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

FILE_FILTERS = [
    'Portable Network Graphics files (*.png)',
    'Text files (*.txt)',
    'Comma Separated Values (*.csv)',
    'All files (*)',
]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        button1 = QPushButton('Open File')
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton('Open Files')
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton('Save File')
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton('Select Folder')
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = ''  # Empty uses default caption.
        initial_dir = ''  # Empty uses current folder.
        initial_filter = FILE_FILTERS[3]
        filters = ';;'.join(FILE_FILTERS)
        print('Filters are:', filters)
        print('Initial filter:', initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self, caption=caption, directory=initial_dir, filter=filters, initialFilter=initial_filter)
        print('Result:', filename, selected_filter)

        if filename:
            with open(filename, 'r', encoding='utf-16') as f:
                print(f.read())

    def get_filenames(self):
        caption = ''
        initial_dir = ''
        initial_filter = FILE_FILTERS[1]
        filters = ';;'.join(FILE_FILTERS)
        print('Filters are:', filters)
        print('Initial filter:', initial_filter)

        (filenames, selected_filter,) = QFileDialog.getOpenFileNames(self, caption=caption,
                                                                     directory=initial_dir, filter=filters, initialFilter=initial_filter,)
        print('Result:', filenames, selected_filter)

        for filename in filenames:
            with open(filename, 'r', encoding='utf-8') as f:
                print(f.read())
                print('#' * 20)

    def get_save_filename(self):
        caption = ''
        initial_dir = ''
        initial_filter = FILE_FILTERS[2]
        filters = ';;'.join(FILE_FILTERS)
        print('Filters are:', filters)
        print('Initial filter:', initial_filter)

        filename, selected_filter = QFileDialog.getSaveFileName(
            self, caption=caption, directory=initial_dir, filter=filters, initialFilter=initial_filter)
        print('Result:', filename, selected_filter)

        if filename:
            if os.path.exists(filename):
                # Existing file, ask the user for confirmation
                write_confirmed = QMessageBox.question(
                    self, 'Overwrite file?', f'The file {filename} exists. Are you sure you want to overwrite it?')
            else:
                # File does not exist, always-confirmed.
                write_confirmed = True

            if write_confirmed:
                with open(filename, 'w') as f:
                    file_content = 'I cry, hopelessly. \nCause I know I\'ll never breath your love again.'
                    f.write(file_content)

    def get_folder(self):
        caption = ''
        initial_dir = ''
        folder_path = QFileDialog.getExistingDirectory(
            self, caption=caption, directory=initial_dir,)
        print('Result:', folder_path)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
