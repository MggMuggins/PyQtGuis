#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Based on the calculator skeleton in the ZetCode PyQt5 tutorial
Hopefully works better than that one...
"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QApplication


class PyCalc(QWidget):
    
    def __init__(self):
        super().__init__()
        self.calc = Calculator()
        self.disp = "0"
        self.isClear = False
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.output = QLabel()
        self.output.setText("0")
        grid.addWidget(self.output, 0, 0, 3, 1)
 
        names = ['Clr', '', '', '',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        
        positions = [(i,j) for i in range(1, 6) for j in range(4)]
        
        for position, name in zip(positions, names):
            
            # Prevent accidental bugs...
            if name == '':
                continue
            button = QPushButton(name)
            if name in ".0123456789":
                button.clicked.connect(self.onNumberClick)
            elif name in "=+-*/":
                button.clicked.connect(self.onOperatorClick)
            elif name == "Clr":
                button.clicked.connect(self.onClrClick)
            grid.addWidget(button, *position)
        
        self.setWindowTitle('PyCalc')
        self.show()
    
    # Construct a string that contains the correct digits
    def onNumberClick(self):
        self.isClear = False
        if self.disp == "0" or self.calc.isNew == True:
            self.disp = self.sender().text()
            self.calc.isNew = False
        else:
            self.disp += self.sender().text()
        
        self.output.setText(self.disp)
    
    # Tell calc that it has an operation to do
    def onOperatorClick(self):
        # Self prep
        self.isClear = False
        oprtor = self.sender().text()
        # Calc prep
        self.calc.stand = int(self.disp)
        self.calc.oprtor = oprtor
        self.calc.isNew = True
        # Calc action
        self.calc.completeOprtn()
    
    # Clear the display string and update the label
    # If clear is pressed again, clear everything out of everythin
    def onClrClick(self):
        self.disp = "0"
        self.output.setText(self.disp)
        if self.isClear == True:
            self.calc.stand = 0
            self.calc.isNew = False
        self.isClear = True

class Calculator():
    def __init__(self):
        self.stand = 0
        self.isNew = False
        self.oprtor = None
    
    def completeOprtn(self):
        if self.oprtor != None:
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyCalc()
    sys.exit(app.exec_())
