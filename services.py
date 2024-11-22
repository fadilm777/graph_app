from PyQt5.QtWidgets import QFileDialog

from UI import MainWindow


class FileService(QFileDialog):

    def __init__(self, window: MainWindow):
        super(FileService, self).__init__()
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilter("CSV files (*.csv)")
        self.window = window
        if self.exec_():
            self.getFiles()

    def getFiles(self):
        self.filenames = self.selectedFiles()
        if self.filenames:
            for file in self.filenames:
                self.window.fileAdder(file)
