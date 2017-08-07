import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit

class FinCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.finPercentLabel = QLabel(self)
        self.finPercent = QLineEdit(self)
        self.gradeLabel = QLabel(self)
        self.grade = QLineEdit(self)
        self.result = QLabel(self)

        self.setLayout(self.grid)
        self.grid.addWidget(self.finPercentLabel, 0, 0)
        self.grid.addWidget(self.finPercent, 0, 1)
        self.grid.addWidget(self.gradeLabel, 1, 0)
        self.grid.addWidget(self.grade, 1, 1)
        self.grid.addWidget(self.result, 2, 0)

        self.finPercentLabel.setText("Final is worth %")
        self.finPercent.setText("10")
        self.gradeLabel.setText("Your grade is %")
        self.grade.setText("80")

        self.grade.textChanged[str].connect(self.onChanged)

        self.resize(300, 100)
        self.setWindowTitle("Finals Calculator")
        self.show()

    def onChanged(self):
        self.classgrade =


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinCalc()
    sys.exit(app.exec_())
