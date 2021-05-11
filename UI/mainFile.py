from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QMessageBox, QDialog,QDialogButtonBox,QVBoxLayout
import sys
import re
import os
from previousPatientData import *
from mainWindows import *
from dialogs import *

LOAD_PREVIOUS = 1;
NEW_PATIENT = 0;
YES = 1;

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
    sessionNum = 0
    setupMeas = None
    setupMeasWrist = None
    setupMeasFinger = None
    setupMeasShoulder = None
    wristMVC = None
    fingerMVC = None
    shoulderMVC = None
    beenExported = None

########################################################################################################################################
                                         # SCROLL #
########################################################################################################################################


class ScrollLabel(QScrollArea):
      
    # contructor
    def __init__(self, parent=None):
        super(ScrollLabel,self).__init__(parent)
  
        # making widget resizable
        self.setWidgetResizable(True)
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
        # vertical box layout
        lay = QVBoxLayout(content)
        # creating label
        self.label = QLabel(content)
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # making label multi-line
        self.label.setWordWrap(True)
        # adding label to the layout
        lay.addWidget(self.label)  

    def UiComponents(self,text):
        # creating scroll label
        label = ScrollLabel(self)
  
        # setting text to the label
        # label.setText(text)
        label.label.setText(text)
        label.label.setStyleSheet("font: 13pt \".AppleSystemUIFont\"; \n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "color: #000000")     
        # setting geometry
        label.setGeometry(QtCore.QRect(450, 150, 621, 581))


########################################################################################################################################
                                        # Generic Functions #
########################################################################################################################################

def close_all():
        sys.exit(0)

def loadClinicianName():
        text_file = open("ClinicanName.txt", "r+")
        data = text_file.read()
        text_file.close()
        return data

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
        self.currentDetails = patientDetails()
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
        if (self.currentDetails.sessionNum!=0):
            self.Window.label_5.setText(self.Window._translate("OverViewWindow", "Session no.{} ".format(self.currentDetails.sessionNum)))       

        #Checks the name once patient set up is done
        if (self.patientDetail.patientName == None):
            self.Window.label_10.setText(self.Window._translate("OverViewWindow", "Patient: - "))
        else:
            self.Window.label_10.setText(self.Window.
            _translate("OverViewWindow", "Patient: {}".format(self.patientDetail.patientName) ))

        #change the exercise
        self.Window.changeExerciseButton.clicked.connect(self.changeExercisePopUp)
        #export data button
        self.Window.ExportDataButton.clicked.connect(self.exportData)
        #view all past patient history

        # print(self.currentDetails.patientName)
        self.Window.changePatient.clicked.connect(self.patientChangeCheckPopUp)

        self.Window.historySide.clicked.connect(self.startUIpatietnHistory)
        if ((self.patientDetail.patientName) == None):
            self.Window.patientSetup.clicked.connect(self.startSetUpPopup)
        else:
            self.Window.patientSetup.clicked.connect(self.patientCheckPopUp)
        self.show()

    def startUIpatietnHistory(self):
        self.historyWindow = Ui_PatientHistoryWindow(self)
        self.setCentralWidget(self.historyWindow)

        self.scroll = QtWidgets.QScrollBar(self.historyWindow.PastSessions)

        historyList = displayPatientHistory(self.currentDetails.patientID,self.currentDetails.sessionNum, self.currentDetails.beenExported)
        if (historyList == 0):
            ScrollLabel.UiComponents(self.historyWindow,"no previous sessions")
        else:
            ScrollLabel.UiComponents(self.historyWindow,historyList)

        #Checks the name once patient set up is done
        if (self.patientDetail.patientName == None):
            self.historyWindow.label_10.setText(self.historyWindow._translate("OverViewWindow", "Patient: - "))
        else:
            self.historyWindow.label_10.setText(self.historyWindow._translate("OverViewWindow", "Patient: {}".format(self.patientDetail.patientName) ))
        
        self.historyWindow.overviewSide.clicked.connect(self.startUIWindow)

        self.show()

    def startSetUpPopup(self):
        #init the patient setup
        setUpPatient = UIinitPatientSetUp(self)
        setUpPatient.setStyleSheet("background-color: rgb(255,252,241);");
        popup = QMessageBox(setUpPatient)

        if (self.patientDetail.patientName == None):
            pass
        else:
            name = self.patientDetail.patientName 
            setUpPatient.patientSetup.setText(name)

        #Assume that when next is pressed the full name is entered
        # Run function that will see if a text file of the patients id exists in "patients details/id.txt"
        # setUpPatient.patientSetup.returnPressed.connect(lambda: self.checkDetail(setUpPatient))
        setUpPatient.nextButton.clicked.connect(lambda: self.checkDetail(setUpPatient))
        setUpPatient.show()
        
    def startEnterMeasurementsPopup(self):
        startEnterMeasurementsPopup = UIinitMeasurePatientSetUp(self)
        startEnterMeasurementsPopup.backButton.clicked.connect(self.startSetUpPopup)
        startEnterMeasurementsPopup.doneButton.clicked.connect(self.sampleEMGPopup)
        startEnterMeasurementsPopup.show()

    def sampleEMGPopup(self):
        popup = Ui_SampleEMG(self)
        popup.nextButton.clicked.connect(self.startUIWindow)
        popup.backBB.clicked.connect(self.startEnterMeasurementsPopup)
        popup.show()       

    def changeExercisePopUp(self):
        changeExercisePopUp = UIchangeExercisePopUp(self)
        popup = QMessageBox(changeExercisePopUp)
        changeExercisePopUp.WristExtension.clicked.connect(lambda: self.passCurrentExercise(1))
        changeExercisePopUp.FingerFlexion.clicked.connect(lambda: self.passCurrentExercise(2))
        changeExercisePopUp.Deltoid.clicked.connect(lambda: self.passCurrentExercise(3))
        changeExercisePopUp.show()   

    def patientCheckPopUp(self):
        ui_patientCheckPopUp = Ui_patientPopUp(self)
        popup = QMessageBox(ui_patientCheckPopUp)
        ui_patientCheckPopUp.DONE.clicked.connect(self.startSetUpPopup)
        ui_patientCheckPopUp.BACK.clicked.connect(self.startUIWindow)
        ui_patientCheckPopUp.show()

    def patientChangeCheckPopUp(self):
        ui_patientChangeCheckPopUp = Ui_changePatientPopUp(self)
        popup = QMessageBox(ui_patientChangeCheckPopUp)
        ui_patientChangeCheckPopUp.DONE.clicked.connect(self.changePatientButton)
        ui_patientChangeCheckPopUp.BACK.clicked.connect(self.startUIWindow)
        ui_patientChangeCheckPopUp.show()        


########################################################################################################################################
                                            # Class functions #
########################################################################################################################################
    def changePatientButton(self):     
        self.currentDetails.clinicanName = None
        self.currentDetails.date = None
        self.currentDetails.patientID = None
        self.currentDetails.patientName = None
        self.currentDetails.sessionNum = 0
        self.currentDetails.setupMeas = None
        self.currentDetails.setupMeasWrist = None
        self.currentDetails.setupMeasFinger = None
        self.currentDetails.setupMeasShoulder = None
        self.currentDetails.wristMVC = None
        self.currentDetails.fingerMVC = None
        self.currentDetails.shoulderMVC = None
        self.currentDetails.beenExported = None  

        self.patientDetail.patientName = None
        self.patientDetail.patientID = None
        self.patientDetail.date = None
        self.patientDetail.sessionNum = 0
        self.patientDetail.setupMeas = None
        self.patientDetail.setupMeasWrist = None
        self.patientDetail.setupMeasFinger = None
        self.patientDetail.setupMeasShoulder = None
        self.patientDetail.wristMVC = None
        self.patientDetail.fingerMVC = None
        self.patientDetail.shoulderMVC = None
        self.patientDetail.beenExported = None 

        self.Window.label_5.setText(self.Window._translate("OverViewWindow", "Session no.  ")) 
        self.Window.label_10.setText(self.Window._translate("OverViewWindow", "Patient: - "))   

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
        self.currentDetails.beenExported = YES
        self.previousData.wristMVC = getPreviousWrist(self.previousData.sessionNum,ID)
        self.previousData.shoulderMVC = getPreviousShoulder(self.previousData.sessionNum,ID)
        self.previousData.fingerMVC = getPreviousFinger(self.previousData.sessionNum,ID)
        self.previousData.setupMeas = getSetupMeasurement(self.previousData.sessionNum,ID)
        
        self.Window.SessionNum = self.currentDetails.sessionNum
    

    # Run after patients name is entered 
    # Checks id code ( the names initals ) for a current file under the given initals
    # IF a current file is there --> load in the data as the patients details
    # ELSE continue on new patient files
    def checkDetail(self,setUpPatient):

        # Setting up the current details for the patient
        name=setUpPatient.patientSetup.text()
        self.patientDetail.patientName = name
        # set up current details class
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
            # self.Window.SessionNum = 1
            # self.Window.label_5.setText(self.Window._translate("OverViewWindow", "{}".format(self.currentDetails.sessionNum)))
    

        # Start next pop-up for window
        self.startEnterMeasurementsPopup()

########################################################################################################################################
                                            # Export Function #
########################################################################################################################################
   
    def exportData(self):

        self.currentDetails.beenExported = YES
        # If patients first session must make a new directory for it
        PATH = './Patient Details/{}'.format(self.currentDetails.patientID)
        if (self.currentDetails.sessionNum == 1):
            os.mkdir(PATH)
        
        file = open("{}/{}{}.txt".format(PATH,self.currentDetails.patientID,self.currentDetails.sessionNum), "w") 
        file.writelines('PatientID:{}\n'.format(self.currentDetails.patientID))
        file.writelines('PatientName:{}\n'.format(self.currentDetails.patientName))
        file.writelines('Date:{}\n'.format(self.currentDetails.date))
        file.writelines('Clinician:{}\n'.format(self.currentDetails.clinicanName))
        file.writelines('sessionNum:{}\n'.format(self.currentDetails.sessionNum))
        file.writelines('setupMeasWrist:{}\n'.format(self.currentDetails.setupMeasWrist))
        file.writelines('setupMeasFinger:{}\n'.format(self.currentDetails.setupMeasFinger))
        file.writelines('setupMeasShoulder:{}\n'.format(self.currentDetails.setupMeasShoulder))
        file.writelines('wristMVC:{}\n'.format(self.currentDetails.wristMVC))
        file.writelines('fingerMVC:{}\n'.format(self.currentDetails.fingerMVC))
        file.writelines('shoulderMVC:{}\n'.format(self.currentDetails.shoulderMVC))


########################################################################################################################################
                                            # Start Application #
########################################################################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    

