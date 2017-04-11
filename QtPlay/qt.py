import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenu()
    
    def initUI(self):
        QToolTip.setFont(QFont('Ubuntu', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a button Widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
    
        self.center()
        self.setWindowTitle("OOP Test Using Qt")
        self.setWindowIcon(QIcon('web.png'))
        
        # self.statusBar().showMessage('Ready')
        self.show()
    
    def initMenu(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
    
    """ # Cant Stand dealing with this every time I run the app...
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """
    
    def center(self):
        # Rectangle Describing the size of the main window
        winGeo = self.frameGeometry()
        # Center of Screen
        centerPnt = QDesktopWidget().availableGeometry().center()
        # Set center of rectangle to center of screen
        winGeo.moveCenter(centerPnt)
        # Move top left point of window to top-left of the rectangle
        self.move(winGeo.topLeft())
        

app = QApplication(sys.argv)
gui = Gui()

sys.exit(app.exec_())