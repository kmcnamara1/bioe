
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QMessageBox, QDialog,QDialogButtonBox,QVBoxLayout
import sys
from UI_1and2 import UIWindow, UIToolTab, UIinitPatientSetUp,UIinitMeasurePatientSetUp

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(1280, 800)
        self.setStyleSheet("background-color: rgb(255,252,241);");
        self.startUIToolTab()

    def startUIToolTab(self):
        self.ToolTab = UIToolTab(self)
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.lineEdit.returnPressed.connect(self.startUIWindow)
        self.ToolTab.startButton.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setCentralWidget(self.Window)     
        self.Window.patientSetup.clicked.connect(self.startSetUpPopup)
        self.show()

    def startSetUpPopup(self):
        setUpPatient = UIinitPatientSetUp(self)
        setUpPatient.setStyleSheet("background-color: rgb(255,252,241);");
        popup = QMessageBox(setUpPatient)
        setUpPatient.nextButton.clicked.connect(self.startEnterMeasurementsPopup)
        setUpPatient.show()
        
    def startEnterMeasurementsPopup(self):
        startEnterMeasurementsPopup = UIinitMeasurePatientSetUp(self)
        startEnterMeasurementsPopup.backButton.clicked.connect(self.startSetUpPopup)
        startEnterMeasurementsPopup.doneButton.clicked.connect(self.startUIWindow)
        startEnterMeasurementsPopup.show()

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    

