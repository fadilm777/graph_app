from PyQt5.QtWidgets import QFileDialog



class FileService(QFileDialog):

    def __init__(self):
        super(FileService, self).__init__()
        
        self.filenames = None
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilter("excel files (*.xlsx *xls)")
        
        if self.exec_():
            self.getFiles()

    def getFiles(self):
        self.filenames = self.selectedFiles()
