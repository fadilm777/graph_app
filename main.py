from PyQt5.QtWidgets import QApplication
from UI import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow("Graphing Application")
window.show()



app.exec_()
