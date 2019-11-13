import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QMainWindow)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor 

my_list = ["Pick a color", "BLACK", "CYAN", "MAGENTA", "TEAL"]
my_RGBdata = ["","(0,0,0)","(0,255,255)","(255,0,255)","(0,128,128)",]
my_HEXdata = ["","#000000","#00FFFF","#FF00FF","#008080"]
my_RGBdata1 = [(0, 0, 0),(0, 255, 255),(255, 0, 255),(0, 128, 128)]


class Window(QWidget):
    def __init__(self):
        super().__init__()



        self.my_intro = QLabel("CST 205 Color Exchange!")
        self.my_combo_box = QComboBox() 
        self.my_combo_box.addItems(my_list)
        self.my_RGB = QLabel("RGB: ")
        self.my_HEX = QLabel("HEX: ")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.my_intro)
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.my_RGB)
        vbox.addWidget(self.my_HEX)


        self.setLayout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui1)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui2)
        self.setWindowTitle("Colors!")


    @pyqtSlot()
    def update_ui2(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_RGB.setText(f'RGB: {my_RGBdata[my_index]}.')

    @pyqtSlot()
    def update_ui1(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_HEX.setText(f'HEX: {my_HEXdata[my_index]}.')


app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())