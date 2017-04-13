import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QGridLayout

class PriceFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.grid = QGridLayout()
        self.outlabel = QLabel(self)
        self.output = QLabel(self)
        self.instruct = QLabel(self)
        self.entry = QLineEdit(self)
        
        self.setLayout(self.grid)
        self.grid.addWidget(self.outlabel, 0, 0)
        self.grid.addWidget(self.output, 0, 1)
        self.grid.addWidget(self.instruct, 1, 0)
        self.grid.addWidget(self.entry, 1, 1)
        
        self.outlabel.setText("Range:")
        self.output.setText("0 - 0")
        self.instruct.setText("Item Price:")
        self.entry.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(0, 0, 300, 100)
        self.setWindowTitle('LOTR Trading Price Finder')
        self.show()
    
    def onChanged(self, price):
        if price != "":
            try:
                price = float(price)
            except ValueError:
                self.output.setText("Only Input Numbers!")
                print("[Error] Only input numbers!")
                return
            item = Item(price)
            self.output.setText(str(int(item.small)) + " - " + str(int(item.large)))
            self.output.adjustSize()
        else:
            self.output.setText("0 - 0")
            self.output.adjustSize()

class Item():
    price = 0
    def __init__(self, price):
        self.price = price
        self.findRange()
    
    def findRange(self):
        oddAverage = self.price / 2 + 0.5;
        if self.price % 2 == 0:
            if self.price % 4 == 0:
                diff = self.price / 4
                self.large = self.price + diff
                self.small = self.price - diff
            else:
                diff = self.price / 4 + 0.5;
                self.large = self.price + diff
                self.small = (self.price - diff) + 1;
                if self.price == 2:
                    self.small -= 1
        else:
            if oddAverage % 2 != 0:
                diff = (oddAverage / 2) + 0.5
                self.large = self.price + diff
                diff = (oddAverage / 2) + 0.5
                self.small = self.price - diff
            else:
                diff = oddAverage / 2
                self.large = self.price + diff
                self.small = self.price - diff

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PriceFinder()
    sys.exit(app.exec_())
