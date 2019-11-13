import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
app = QApplication(sys.argv)
class MainWindow(QMainWindow):
 	def __init__(self):
 		super().__init__()
 		self.setWindowTitle('Default')
 		self.show()
mainWin = MainWindow()
input("press enter")
mainWin.setWindowTitle("cst 205 Main Windows")
mainWin.show()
status = app.exec_()
sys.exit(status)