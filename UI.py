from collections.abc import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from handlers import graphGenerator
from services import FileService


class MainWindow(QMainWindow):

    def __init__(self, title: str):
        super(MainWindow, self).__init__()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas)

        self.setWindowTitle(title)
        self._layoutInit()
        self._initWidgets()
        self._initCanvas()

    def _addButtion(self):
        button = Button("Import csv", self.fileAdder)
        self.widgets.addWidget(button)

    def _layoutInit(self):
        self.hScreenLayout = QHBoxLayout()
        self.vFilesLayout = QVBoxLayout()
        #self.vFilesLayout.setSpacing(0)
        #self.vFilesLayout.setContentsMargins(0,0,0,0)
        self.vFilesLayout.addStretch()
        self.plot = QVBoxLayout()
        self.widgets = QVBoxLayout()
        self.hScreenLayout.addLayout(self.vFilesLayout)
        self.hScreenLayout.addLayout(self.plot)
        self.hScreenLayout.addLayout(self.widgets)
       

    def _initWidgets(self):
        widget = QWidget()
        widget.setLayout(self.hScreenLayout)
        self.setCentralWidget(widget)
        self.plot.addWidget(self.canvas)
        self.plot.addWidget(self.toolbar)

    def fileAdder(self, path: str):
        fileservice = FileService()
        self.fileList = fileservice.filenames
        for path in self.fileList:
            name = path.split('/')[-1]
            file = Button(name, lambda: graphGenerator(path, self))
            file.setIcon(QIcon("./assets/csv.png"))
            self.vFilesLayout.insertWidget(0, file)
        
    def _initCanvas(self):
        ax = self.figure.add_subplot(111)

        self.canvas.draw()

class Button(QPushButton):

    def __init__(self, title: str, func: Callable, minw=200, maxw=200):
        super(Button, self).__init__(title)
        self.clicked.connect(func)
        self.setMaximumWidth(maxw)
        self.setMinimumWidth(minw)
