from PyQt5.QtWidgets import QFileDialog

from UI import MainWindow


class FileService(QFileDialog):

    def __init__(self):
        super(FileService, self).__init__()
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilter("CSV files (*.csv)")
        if self.exec_():
            self.getFiles()

    def getFiles(self):
        self.filenames = self.selectedFiles()
