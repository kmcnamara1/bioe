from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QDialog
import sys

class WindowLV3(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.setGeometry(300, 300, 120, 150)
        self.setWindowTitle('LV3')

        self.quit = QtWidgets.QPushButton('Close', self)
        self.quit.setGeometry(10, 10, 60, 35)

        self.quit.clicked.connect(self.test_done) # this will close entire program

    def test_done(self):
        self.close()  

class WindowLV2(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.Window3 = WindowLV3()

        self.setGeometry(300, 300, 120, 150)
        self.setWindowTitle('LV2')

        self.quit = QtWidgets.QPushButton('Close', self)
        self.quit.setGeometry(10, 10, 60, 35)

        next = QtWidgets.QPushButton('Lv3', self)
        next.setGeometry(10, 50, 60, 35)

        self.connect(self.quit, QtCore.SIGNAL('clicked()'),
            self.close)  # this should work

        self.next.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.Window3.show()


class WindowLV1(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.Window2 = WindowLV2()

        self.setGeometry(300, 300, 120, 150)
        self.setWindowTitle('LV1')

        next = QtWidgets.QPushButton('Lv2', self)
        next.setGeometry(10, 50, 60, 35)

        self.quit = QtWidgets.QPushButton('Close', self)
        self.quit.setGeometry(10, 10, 60, 35)

        self.connect(next, QtCore.SIGNAL('clicked()'),
            self.nextWindow)

    def nextWindow(self):
        self.Window2.show()

        self.quit.clicked.connect(self.test_quit)  # this should work      

    def test_quit(self):
        self.close()         


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window1 = WindowLV1()
    Window1.show()
    sys.exit(app.exec_())
