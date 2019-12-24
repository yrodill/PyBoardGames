#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import sys
import pickle
import os
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Menu(QMainWindow):

    """
    Main Window ;
    Select the game to be played
    """

    def __init__(self):
        super(Menu,self).__init__()
        self.gui()

    def gui(self):
        layout = QGridLayout()
        label = QLabel("Choix du jeu :",self)
        #.label.move(10,10)
        combo = QComboBox(self)
        combo.addItem("Default")
        combo.addItem("Jeu de l'oie")
        combo.addItem("Rouge ou noir")
        combo.addItem("Pyramide")
        combo.resize(150,20)
        #.combo.move(110
        start_button = QPushButton("Launch the game",self)
        start_button.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)
        #.start_button.move(80,200)
        start_button.clicked.connect(self.launchGame)
        layout.addWidget(label,0,0)
        layout.addWidget(combo,1,0)
        layout.addWidget(start_button,3,3)
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("Menu Principal")
        self.setLayout(layout)
        self.show()


    def launchGame(self):
        print(self.combo.currentText())
        #if self.combo.currentText() == "Jeu de l'oie"
            #self.game = 

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Menu()
    #window.show()
    sys.exit(app.exec_())