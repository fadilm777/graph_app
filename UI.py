from collections.abc import Callable

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QLabel, QMainWindow, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

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
        
        self.ax = self.figure.add_subplot(111)
        
        self._layoutInit()
        self._initWidgets()
        self._initCanvas()
        
        self.table = None

    def _addImport(self):
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
       
    def _initLabels(self):
        self.label = QLabel("File List")
        
        font = QFont("Arial", 15)
        self.label.setFont(font)
        self.label.setMinimumWidth(200)
    
    def _initWidgets(self):
        widget = QWidget()
        widget.setLayout(self.hScreenLayout)
        self.setCentralWidget(widget)
       
        self.plot.addWidget(self.canvas)
        self.plot.addWidget(self.toolbar)
        
        self._addImport()
        self._initLabels()
        
        self.vFilesLayout.insertWidget(0, self.label)

    def fileAdder(self):
        fileservice = FileService()
        self.fileList = fileservice.filenames
        if self.fileList is not None:
            for path in self.fileList:
                name = path.split('/')[-1]
                file = Button(name, lambda: graphGenerator(path, self))
                file.setIcon(QIcon("./assets/csv.png"))
                self.vFilesLayout.insertWidget(1, file)
            
    def _initCanvas(self):
        self.canvas.draw()
        
        self.ax.spines['left'].set_position('center')  # Vertical axis
        self.ax.spines['bottom'].set_position('center')  # Horizontal axis

        # Hide the top and right spines
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')

        # Set ticks to appear on both sides of the axes
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

    def plotCanvas(self, dispEnvPos1, forceEnvPos1, x, y, negEnv):
       
        self.ax.plot(dispEnvPos1, forceEnvPos1, marker='.', color='r')
        self.ax.plot(x, y, linewidth=0.5, color='b')
        self.ax.plot(negEnv[:,0], negEnv[:,1], marker='.', color='r')
        
        self.canvas.draw()
        
        self.createTable(dispEnvPos1, forceEnvPos1, negEnv[:,1], negEnv[:,0])

    def createTable(self, force1, disp1, force2, disp2):
        if self.table is not None: self.widgets.removeWidget(self.table)
        
        self.table = QTableWidget()
        self.table.setRowCount(force1.size)
        self.table.setColumnCount(2)
        
        for i in range(force1.size):
            self.table.setItem(i, 0, QTableWidgetItem(f"{force1[i]:.3f}"))
        
        for i in range(force1.size):
            self.table.setItem(i, 1, QTableWidgetItem(f"{disp1[i]:.3f}"))
        
        for i in range(force2.size):
            self.table.setItem(i, 0, QTableWidgetItem(f"{force2[i]:.3f}"))
        
        for i in range(force2.size):
            self.table.setItem(i, 1, QTableWidgetItem(f"{disp2[i]:.3f}"))       
        
        self.table.setMaximumWidth(300)
        self.table.setHorizontalHeaderLabels(["Force", "Displacement"])
        
        self.widgets.addWidget(self.table)

class Button(QPushButton):

    def __init__(self, title: str, func: Callable, minw=200, maxw=200):
        super(Button, self).__init__(title)
       
        self.clicked.connect(func)
        self.setMaximumWidth(maxw)
        self.setMinimumWidth(minw)
