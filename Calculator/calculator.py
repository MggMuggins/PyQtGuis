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
        if self.disp == "0":
            self.disp = self.sender().text()
        else:
            self.disp += self.sender().text()
        
        self.output.setText(self.disp)
    
    
    def onOperatorClick(self):
        text = self.sender().text()
        disp = int(self.disp)
        if self.calc.stand == 0:
            pass
        else:
            if text == '+':
                self.calc.addVal(disp)
            elif text == '-':
                self.calc.subVal(disp)
            elif text == '*':
                self.calc.multVal(disp)
            elif text == '/':
                self.calc.divVal(disp)
    
    # Clear the display string and update the label
    def onClrClick(self):
        self.disp = "0"
        self.output.setText(self.disp)

class Calculator():
    def __init__(self):
        self.stand = 0
    
    def addVal(self, value):
        self.stand += value
    
    def subVal(self, value):
        self.stand -= value
    
    def multVal(self, value):
        self.stand *= value
    
    def divVal(self, value):
        self.stand /= value

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyCalc()
    sys.exit(app.exec_())
