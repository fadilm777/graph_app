from PyQt5.QtWidgets import QFileDialog

class FileService(QFileDialog):
    """
    A custom class that inherits from QFIleDialog(). 
    When an instance of this class is created it pops up the file dialog, 
    through which the user can open an excel file.
    The list of files selected is stored in FileService.fileNames.
    """
    def __init__(self):
        super(FileService, self).__init__()
        
        self.filenames = None
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilter("excel files (*.xlsx *xls *csv)")
        
        if self.exec_():
            self.getFiles()

    def getFiles(self):
        self.filenames = self.selectedFiles()
