
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QMessageBox, QDialog,QDialogButtonBox,QVBoxLayout
import sys
import re
import os
from previousPatientData import *
from UI_1and2 import *

LOAD_PREVIOUS = 1;
NEW_PATIENT = 0;

########################################################################################################################################
                                         # CLASSES #
########################################################################################################################################

class previousPatientData:
    wristMVC = None;
    shoulderMVC = None;
    fingerMVC = None;
    previousSessionNum = None
    setupMeas = None;


class patientDetails:
    clinicanName = None
    date = None
    patientID = None
    patientName = None
    sessionNum = None
    setupMeas = None
    wristMVC = None
    fingerMVC = None
    shoulderMVC = None

########################################################################################################################################
                                        # Generic Functions #
########################################################################################################################################


def close_all():
        sys.exit(0)

def clearPatientFile():
    text_file = open("Patient Details/PatientName.txt", "w")
    data = text_file.write()
    text_file.truncate(0)
    text_file.close()

def loadClinicianName():
        text_file = open("ClinicanName.txt", "r+")
        data = text_file.read()
        text_file.close()
        return data


def getPatientID(name):
    name_list = name.split() 

    initials = ""

    for split_name in name_list:  # go through each name
        initials += split_name[0].upper()  # append the initial    

    return initials


# We assume the patient name is split with a space 
def checkPatientDetails(name):
    
    patientID = getPatientID(name)
    return(checkReturningPatient(patientID)) # return 1 if is reoccuring
                                             # return 0 if new


#trys to open a file with the users ID
# IF: can open --> previous patient must exist
# ELSE: must be a new patient 
def checkReturningPatient(initials):
    file_path = ("Patient Details/{}1.txt".format(initials))

    if not os.path.exists(file_path):
        return 0
    else: 
        return 1



########################################################################################################################################
                                                        # MAIN SECTION #
########################################################################################################################################


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(1280, 800)
        self.setStyleSheet("background-color: rgb(255,252,241);");
        loadClinicianName()
        self.startUIToolTab()
        self.patientDetail = patientDetails() #start instance of patient details

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

        #set up patient details run next class
        self.Window.patientSetup.clicked.connect(self.startSetUpPopup)

        # clinicianName = loadClinicianName()
        #Checks the name once patient set up is done
        if (self.patientDetail.patientName == None):
            self.Window.label_10.setText(self.Window._translate("OverViewWindow", "Patient: - "))
        else:
            self.Window.label_10.setText(self.Window.
            _translate("OverViewWindow", "Patient: {}".format(self.patientDetail.patientName) ))

        #change the exercise
        self.Window.changeExerciseButton.clicked.connect(self.changeExercisePopUp)
        self.show()

    def startSetUpPopup(self):

        #init the patient setup
        setUpPatient = UIinitPatientSetUp(self)
        setUpPatient.setStyleSheet("background-color: rgb(255,252,241);");
        popup = QMessageBox(setUpPatient)
        #Assume that when next is pressed the full name is entered
        # Run function that will see if a text file of the patients id exists in "patients details/id.txt"
        setUpPatient.patientSetup.returnPressed.connect(lambda: self.checkDetail(setUpPatient))
        setUpPatient.nextButton.clicked.connect(lambda: self.checkDetail(setUpPatient))

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
        if n==1:
            self.Window.currentExerciseSelection = "Wrist Extension"
                  
        elif n==2:
            self.Window.currentExerciseSelection = "Finger Flexion"

        elif n==3:
            self.Window.currentExerciseSelection = "Shoulder Flexion"
        
        self.Window.label_4.setText(self.Window._translate("OverViewWindow", self.Window.currentExerciseSelection))
        self.Window.show()   


    def loadPreviousSessionData(self,ID):
        # find how many sessions they have had
        self.previousData.sessionNum = getNumSessions(ID)
        self.currentDetails.sessionNum = (self.previousData.sessionNum + 1)
        self.previousData.wristMVC = getPreviousWrist(self.previousData.sessionNum,ID)
        self.previousData.shoulderMVC = getPreviousShoulder(self.previousData.sessionNum,ID)
        self.previousData.fingerMVC = getPreviousFinger(self.previousData.sessionNum,ID)
        self.previousData.setupMeas = getSetupMeasurement(self.previousData.sessionNum,ID)

    

    # Run after patients name is entered 
    # Checks id code ( the names initals ) for a current file under the given initals
    # IF a current file is there --> load in the data as the patients details
    # ELSE continue on new patient files
    def checkDetail(self,setUpPatient):

        # Setting up the current details for the patient
        name=setUpPatient.patientSetup.text()
        self.patientDetail.patientName = name
        print(name)
 
        # set up current details class
        self.currentDetails = patientDetails()
        temp = loadClinicianName()
        self.currentDetails.clinicanName = temp
        self.currentDetails.date = datetime.today().strftime('%Y-%m-%d')
        self.currentDetails.patientID = getPatientID(name)
        self.currentDetails.patientName = name

        #Check if patient has previous history
        # if new checkPatientDetails returns 0
        # if has previous sessions checkPatientDetails returns 1
        if(checkPatientDetails(name)==1):
            print("PREVIOUS PATIENT")
            self.previousData = previousPatientData()
            self.loadPreviousSessionData(self.currentDetails.patientID)
        else:
            print("NEW PATIENT")
            self.currentDetails.sessionNum = 1

        # Start next pop-up for window
        self.startEnterMeasurementsPopup()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    

