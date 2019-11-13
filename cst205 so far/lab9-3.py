import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot 

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()

		vbox = QVBoxLayout()
		hbox = QHBoxLayout()

		self.botton1 = QPushButton("Button1", self)
		self.botton2 = QPushButton("Button2", self)
		self.label1 = QLabel('Push the botton and find out your fortune today')
		self.label2 = QLabel('you click just once, okay?')
		self.botton1.clicked.connect(self.bt1_clicked)
		self.botton2.clicked.connect(self.bt2_clicked)

		vbox.addWidget(self.label1)
		vbox.addWidget(self.label2)
		vbox.addWidget(self.botton1)
		vbox.addWidget(self.botton2)
		self.setLayout(vbox)
		self.setLayout(hbox)
		self.show() 

	@pyqtSlot()
	def bt1_clicked(self):
		self.botton1.setText('GOOD DAY')
	def bt2_clicked(self):
		self.botton2.setText('BAD DAY')




my_qt_app = QApplication(sys.argv)
my_window= MyWindow()
my_window.setGeometry(0,0,150,150)
my_window.setWindowTitle('LAB 9 TASK4')
my_window.show()
sys.exit(my_qt_app.exec_())