from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QMessageBox, QDialog,QDialogButtonBox,QVBoxLayout
import sys
import re
import os
from previousPatientData import *
from mainWindows import *
from dialogs import *

LOAD_PREVIOUS = 1
NEW_PATIENT = 0
YES = 1



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
    ur = None
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
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    text_file = open('ClinicianName.txt' , "r+")
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
        self.EXERCISE_SET = None
        self.patientDetail = patientDetails() #start instance of patient details

    def startUIToolTab(self):
        self.ToolTab = UIToolTab(self)
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.lineEdit.returnPressed.connect(self.patientRegister)
        self.ToolTab.startButton.clicked.connect(self.patientRegister)
        
        self.show()

    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setCentralWidget(self.Window)

        self.Window.Logout.clicked.connect(self.logout)  

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
        self.Window.changePatient.clicked.connect(self.patientChangeCheckPopUp)

        # this is for the start and stop functionality 
        self.Window.startButton.clicked.connect(self.startButtonFun)
        self.Window.stopButton.clicked.connect(lambda: self.stopButtonCheck(self.EXERCISE_SET))

        self.Window.historySide.clicked.connect(self.startUIpatietnHistory)
        
        if (self.EXERCISE_SET == None):
            #We must select an exercise to know imgs to display

            self.Window.patientSetup.clicked.connect(self.patientCheckExercisePopUp)         
        else:
            # This will check if a name is in the database and then re check if they want to overwrite this
            self.Window.patientSetup.clicked.connect(self.startSetUpPopup)
            self.show()       

    # performs all clearing of data for logout
    def logout(self):
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
        self.currentDetails.ur = None

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
        
        self.startUIToolTab()

    def patientRegister(self):
        self.startUIWindow()
        ui_patientReg = Ui_Register(self)
        popup = QMessageBox(ui_patientReg)
        ui_patientReg.OK.clicked.connect(self.startUIWindow)
        ui_patientReg.OK.clicked.connect(lambda: self.checkDetail(ui_patientReg))
        ui_patientReg.URnumLine.returnPressed.connect(lambda: self.checkDetail(ui_patientReg))
        ui_patientReg.URnumLine.returnPressed.connect(self.startUIWindow)
        ui_patientReg.show()

    def patientCheckExercisePopUp(self):
        ui_patientCheckPopUp = Ui_checkExercise(self)
        popup = QMessageBox(ui_patientCheckPopUp)
        ui_patientCheckPopUp.BACK.clicked.connect(self.startUIWindow)
        ui_patientCheckPopUp.show()

    def startUIpatietnHistory(self):
        self.historyWindow = Ui_PatientHistoryWindow(self)
        self.setCentralWidget(self.historyWindow)

        self.historyWindow.Logout.clicked.connect(self.logout) 
        self.historyWindow.changePatient.clicked.connect(self.patientChangeCheckPopUp)
        self.historyWindow.patientSetup.clicked.connect(self.changetoHome)

        self.scroll = QtWidgets.QScrollBar(self.historyWindow.PastSessions)

        historyList = displayPatientHistory(self.currentDetails.patientID,self.currentDetails.ur,self.currentDetails.sessionNum, self.currentDetails.beenExported)
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

    def changetoHome(self):
        popHome = changetohomeUI(self)
        popHome.DONE.clicked.connect(self.startUIWindow)
        popHome.show()        

    def startSetUpPopup(self):
        #init the patient setup
        listInfo = self.EXERCISE_SET
        setUpPatient = UIinitPatientSetUp(parent=self, listInfo=listInfo)
        setUpPatient.setStyleSheet("background-color: rgb(255,252,241);");
        popup = QMessageBox(setUpPatient)

        # if (self.patientDetail.patientName == None):
        #     pass
        # else:
        #     name = self.patientDetail.patientName 
        #     setUpPatient.patientSetup.setText(name)

        #Assume that when next is pressed the full name is entered
        # Run function that will see if a text file of the patients id exists in "patients details/id.txt"
        # setUpPatient.patientSetup.returnPressed.connect(lambda: self.checkDetail(setUpPatient))
        # setUpPatient.nextButton.clicked.connect(lambda: self.checkDetail(setUpPatient))
        # setUpPatient.patientSetup.returnPressed.connect(self.startEnterMeasurementsPopup)
        setUpPatient.nextButton.clicked.connect(self.startEnterMeasurementsPopup)

        setUpPatient.show()
        
    def startEnterMeasurementsPopup(self):
        
        listInfo = self.EXERCISE_SET
        startEnterMeasurementsPopup = UIinitMeasurePatientSetUp(parent=self,listInfo=listInfo)
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
        self.EXERCISE_SET = 1

        popup = QMessageBox(changeExercisePopUp)
        changeExercisePopUp.WristExtension.clicked.connect(lambda: self.passCurrentExercise(1))
        changeExercisePopUp.FingerFlexion.clicked.connect(lambda: self.passCurrentExercise(2))
        changeExercisePopUp.Deltoid.clicked.connect(lambda: self.passCurrentExercise(3))

        # changeExercisePopUp.WristExtension.clicked.connect(self.startUIWindow)

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

    def checkPatientSetup(self):
        dialogPatientSetup = Ui_needPatientSetup(self)
        popup = QMessageBox(dialogPatientSetup)
        dialogPatientSetup.show()
########################################################################################################################################
                                            # Class functions #
########################################################################################################################################
    def startButtonFun(self):
        self.Window.label_7.setText(self.Window._translate("OverViewWindow", "41.322mV"))
        self.Window.label_7.adjustSize()

    def stopButtonCheck(self,exercise):
        stopCheck = Ui_finishEMGReading(self)
        popup = QMessageBox(stopCheck)

        #functionality of the buttons

        stopCheck.nextExB.clicked.connect(self.changeExercisePopUp)   

        if (exercise == 1):
            #wrist
            stopCheck.redoB.clicked.connect(lambda: self.clearVal(exercise))
            stopCheck.middleB.clicked.connect(self.exportData)
        elif (exercise == 2):
            #finger
            stopCheck.redoB.clicked.connect(lambda: self.clearVal(exercise))
            stopCheck.middleB.clicked.connect(self.exportData)
        else:
            #shoulder
            stopCheck.redoB.clicked.connect(lambda: self.clearVal(exercise))
            stopCheck.middleB.clicked.connect(self.exportData)


        stopCheck.show()

    def clearVal(self,exercise):
        print(exercise)
        if (exercise == 1):
            self.currentDetails.wristMVC = None
        elif (exercise == 2):
            self.currentDetails.fingerMVC = None
        else:
            self.currentDetails.shoulderMVC = None
        self.passCurrentExercise(exercise)
        self.startUIWindow()
        
        

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
        self.currentDetails.ur = None

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
        self.patientRegister()

    def passCurrentExercise(self,n):
        self.EXERCISE_SET = n
        self.startUIWindow()
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
        self.previousData.sessionNum = getNumSessions(ID+self.currentDetails.ur)
        self.currentDetails.sessionNum = (self.previousData.sessionNum + 1)
        self.currentDetails.beenExported = YES
        self.previousData.wristMVC = getPreviousWrist(self.previousData.sessionNum,ID,self.currentDetails.ur)
        self.previousData.shoulderMVC = getPreviousShoulder(self.previousData.sessionNum,ID,self.currentDetails.ur)
        self.previousData.fingerMVC = getPreviousFinger(self.previousData.sessionNum,ID,self.currentDetails.ur)
        self.previousData.setupMeas = getSetupMeasurement(self.previousData.sessionNum,ID,self.currentDetails.ur)
        
        self.Window.SessionNum = self.currentDetails.sessionNum
    

    # Run after patients name is entered 
    # Checks id code ( the names initals ) for a current file under the given initals
    # IF a current file is there --> load in the data as the patients details
    # ELSE continue on new patient files
    def checkDetail(self,ui_patientReg):

        # Setting up the current details for the patient
        name=ui_patientReg.PnameLine.text()
        ur=ui_patientReg.URnumLine.text()

        self.patientDetail.patientName = name
        # set up current details class
        temp = loadClinicianName()
        self.currentDetails.clinicanName = temp
        self.currentDetails.date = datetime.today().strftime('%Y-%m-%d')
        self.currentDetails.patientID = getPatientID(name)
        self.currentDetails.ur = ur
        self.currentDetails.patientName = name

        #Check if patient has previous history
        # if new checkPatientDetails returns 0
        # if has previous sessions checkPatientDetails returns 1

        if(checkPatientDetails(name,ur)==1):
            print("PREVIOUS PATIENT")
            self.previousData = previousPatientData()
            self.loadPreviousSessionData(self.currentDetails.patientID)
        else:
            print("NEW PATIENT")
            self.currentDetails.sessionNum = 1
    

        # Start next pop-up for window
        # self.show() 
        self.startUIWindow()


########################################################################################################################################
                                            # Export Function #
########################################################################################################################################
   
    def exportData(self):

        self.currentDetails.beenExported = YES
        # If patients first session must make a new directory for it
        PATH = './Patient Details/{}'.format((self.currentDetails.patientID+self.currentDetails.ur))
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
    

