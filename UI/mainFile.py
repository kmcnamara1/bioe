
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QMessageBox, QDialog,QDialogButtonBox,QVBoxLayout
import sys
from UI_1and2 import UIWindow, UIToolTab, UIinitPatientSetUp,UIinitMeasurePatientSetUp,UIchangeExercisePopUp

def close_all():
        sys.exit(0)

def wrist_exercise_():
    wrist_exercise_str()

def wrist_exercise_str():
    print("Wrist Extension")
    res = "Wrist Extension"
    return res


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
        self.Window.Logout.clicked.connect(self.startUIToolTab)     
        self.Window.patientSetup.clicked.connect(self.startSetUpPopup)
        self.Window.changeExerciseButton.clicked.connect(self.changeExercisePopUp)
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

    def changeExercisePopUp(self):
        changeExercisePopUp = UIchangeExercisePopUp(self)
        popup = QMessageBox(changeExercisePopUp)
        changeExercisePopUp.WristExtension.clicked.connect(lambda: self.passCurrentExercise(1))

        changeExercisePopUp.FingerFlexion.clicked.connect(lambda: self.passCurrentExercise(2))
        changeExercisePopUp.Deltoid.clicked.connect(lambda: self.passCurrentExercise(3))
        changeExercisePopUp.show()   


    def passCurrentExercise(self,n):
        print(n)
        if n==1:
            self.Window.currentExerciseSelection = "Wrist Extension"
                  
        elif n==2:
            self.Window.currentExerciseSelection = "Finger Flexion"

        elif n==3:
            self.Window.currentExerciseSelection = "Shoulder Flexion"
        
        self.Window.label_4.setText(self.Window._translate("OverViewWindow", self.Window.currentExerciseSelection))
        self.Window.show()   



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    

