from collections.abc import Callable
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget

from handlers import graphGenerator


class MainWindow(QMainWindow):

    def __init__(self, title: str):
        super(MainWindow, self).__init__()

        self.setWindowTitle(title)
        
        self._layoutInit()
        self._createMenu()

    def _addButtion(self, button):
        self.dummy.addWidget(button)

    def _layoutInit(self):
        self.hScreenLayout = QHBoxLayout()
        self.vFilesLayout = QVBoxLayout()
        self.dummy = QVBoxLayout()
        self.hScreenLayout.addLayout(self.vFilesLayout)
        self.hScreenLayout.addLayout(self.dummy)
        
        widget = QWidget()
        widget.setLayout(self.hScreenLayout)
        self.setCentralWidget(widget)

    def fileAdder(self, path: str):
        words = path.split('/')
        file = Button(words[-1], graphGenerator)
        self.vFilesLayout.addWidget(file)


    

    def _createMenu(self):
        menu = self.menuBar()
        if menu is not None:
            fileMenu = menu.addMenu("&File")



class Button(QPushButton):

    def __init__(self, title: str, func: Callable):
        super(Button, self).__init__(title)
        self.clicked.connect(func)



        

