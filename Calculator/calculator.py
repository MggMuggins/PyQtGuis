#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Based on the calculator skeleton in the ZetCode PyQt5 tutorial
Hopefully works better than that one...
"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
 
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        
        positions = [(i,j) for i in range(5) for j in range(4)]
        
        for position, name in zip(positions, names):
            
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.onButtonClick)
            grid.addWidget(button, *position)
            
        self.move(300, 150)
        self.setWindowTitle('PyCalc')
        self.show()
    
    def onButtonClick(self):
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
