from PyQt5.QtWidgets import QApplication
from UI import Button, MainWindow
from application import Application
import sys

from services import FileService

def get_files():
    FileService(window)

app = QApplication(sys.argv)
window = MainWindow("Graphing Application")
button = Button("Files", get_files)
window._addButtion(button)
window.show()



app.exec_()
