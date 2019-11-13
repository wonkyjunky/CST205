import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QMainWindow)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.x = QLabel(self)
		self.y = QLabel("Jeanne Modigliani",self)
		self.z = QPixmap("monalisa.jpg")
		self.x.setPixmap(self.z)
		my_layout = QVBoxLayout()
		my_layout.addWidget(self.x)
		my_layout.addWidget(self.y)
		self.setLayout(my_layout)

app = QApplication(sys.argv)
a = MyWindow()
a.show()
sys.exit(app.exec_())