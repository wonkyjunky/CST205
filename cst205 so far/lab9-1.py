import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

my_qt_app = QApplication(sys.argv)
my_window = QWidget()
my_window.setGeometry(0,0,400,400)
my_window.setWindowTitle('LAB 9 TASK3')
my_label = QLabel(my_window)
pixmap = QPixmap('monalisa.jpg')
my_label.setPixmap(pixmap)
my_label.resize(pixmap.width(),pixmap.height())
my_window.show()
sys.exit(my_qt_app.exec_())