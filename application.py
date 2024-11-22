from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

from UI import MainWindow

class Application():

    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = MainWindow("Graphing Application")
        self.window.show()

    def start(self) -> None:
        self.app.exec_()
