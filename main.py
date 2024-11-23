from PyQt5.QtWidgets import QApplication
from UI import Button, MainWindow
import sys

from services import FileService


app = QApplication(sys.argv)
window = MainWindow("Graphing Application")
window.show()



app.exec_()
