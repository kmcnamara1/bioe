########################################################################################################################################
########################################################################################################################################
# This file:
# - joins all the dialog popups and classes together
# - controls the whole GUI
# 
# Team 4
# Date Modified: 27/05/2021
# Author: Anna Scolaro 
########################################################################################################################################
########################################################################################################################################


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import copy
from PyQt5.QtWidgets import * 
import sys
import re
import os
from GUI_patientData import *
from GUI_mainWindows import *
from GUI_dialogs import *


'''
GLOBALS
''' 
LOAD_PREVIOUS = 1
NEW_PATIENT = 0
YES = 1



########################################################################################################################################
                                         # Global #
########################################################################################################################################

class previousPatientData:
    wristMVC = None
    shoulderMVC = None
    fingerMVC = None
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

'''
Handles: Display and functionality of the table and HISTORY window
''' 
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
    '''
    Handles: Display and functionality of the HOME window
    Inputs: Text (the history), wrist, finger and shoulder past MVC values as lists
    ''' 
    def UiComponents(self,text,wristEntry,fingerEntry,shoulderEntry):
        # creating scroll label
        label = ScrollLabel(self)

        WE = copy.deepcopy(wristEntry)
        FE = copy.deepcopy(fingerEntry)
        SE = copy.deepcopy(shoulderEntry)

        # if (text != "no previous sessions"):

        lengths = [len(wristEntry),len(fingerEntry),len(shoulderEntry)]
        maxVal = max(lengths)

        if (maxVal != len(wristEntry)):
            
            diff = maxVal-len(wristEntry)
            for i in range(1,(diff+1)):
                WE.append('-')

        if(maxVal != len(fingerEntry)):
        
            diff = maxVal-len(fingerEntry)
            for i in range(1,(diff+1)):
                FE.append('-')

        if(maxVal != len(shoulderEntry)):
        
            diff = maxVal-len(shoulderEntry)
            for i in range(1,(diff+1)):
                SE.append('-')

        self.tableFrame = QtWidgets.QFrame(self)
                # self.label.setWordWrap(True)
        self.tableFrame.setGeometry(QtCore.QRect(500,170,500,145))
        self.tableFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableFrame.setObjectName("WelcomeFrame")

        #making the table
        self.table = QTableWidget(self.tableFrame)
        self.table.raise_()
        self.table.setWordWrap(True)
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "color:#323232")
        self.table.setRowCount(3)
        self.table.setVerticalHeaderLabels(['Wrist (mvc)','Finger (mvc)','Shoulder (mvc)'])

        # adding title names to the headers
        sessionNameArray = []
        for i in range(1,(maxVal+1)):
            temp = "Ses {}".format(i)
            sessionNameArray.insert(0,temp)

        self.table.setColumnCount(maxVal)
        self.table.setHorizontalHeaderLabels(sessionNameArray)

        self.table.verticalHeader().setStyleSheet("background-color: rgb(207, 207, 207);\n" "border-radius:14px")
        self.table.horizontalHeader().setStyleSheet("background-color: rgb(207, 207, 207);\n" "border-radius:14px")
        
        
        # loads in data to table
        for column in range(0,maxVal):
            for row in range(0,3):
                #making sure it goes in backwards order
                if (row == 0):
                    val = WE[abs(column-(maxVal-1))]
                elif (row == 1):
                    val = FE[abs(column-(maxVal-1))]    
                else:
                    val = SE[abs(column-(maxVal-1))] 
    
                self.table.setItem(row,column,QTableWidgetItem(val))

        self.table.adjustSize()


        layout = QGridLayout()
        layout.addWidget(self.table, 1, 0)
        self.tableFrame.setLayout(layout)

        self.clip = QApplication.clipboard()

        # setting text to the label
        # label.setText(text)
        label.label.setText("\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r-----------------------------------------------------------------------------------------\n\r{}".format(text))
        label.label.setStyleSheet("font: 13pt \".AppleSystemUIFont\"; \n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "color: #000000")     
        # setting geometry
        label.setGeometry(QtCore.QRect(450, 150, 621, 581))


########################################################################################################################################
                                    # Generic Functions #
########################################################################################################################################

"""
Loads the store name of the clinican for home window display-ing
"""
def loadClinicianName():
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    text_file = open('ClinicianName.txt' , "r+")
    data = text_file.read()
    text_file.close()
    return data

"""
Gets the stored measurement from the EMG location popup
"""
def get_meas_txt():
    text_file = open("meas.txt", "r+")
    data = text_file.read()
    text_file.truncate(0)
    text_file.close()
    return data
 
########################################################################################################################################
                                            # MAIN SECTION #
########################################################################################################################################


class MainWindow(QMainWindow):

    #start classes and login window
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(1280, 800)
        self.setStyleSheet("background-color: rgb(255,252,241);");
        loadClinicianName()
        self.currentDetails = patientDetails()
        self.startUIToolTab()
        self.current_delsys_MVC = None
        self.EXERCISE_SET = None
        self.patientDetail = patientDetails() #start instance of patient details
        self.setWindowTitle("EMG Assessment")

    '''
    Handles: Display and functionality of the LOGIN window
    ''' 
    def startUIToolTab(self):
        
        self.ToolTab = UIToolTab(self)
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.lineEdit.returnPressed.connect(self.patientRegister)
        self.ToolTab.startButton.clicked.connect(self.patientRegister)
        self.show()


    '''
    Handles: Display and functionality of the HOME window
    '''  
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

    '''
    Handles: performs all clearing of data for logout
    '''  
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
        #display LOGIN window
        self.startUIToolTab()


    '''
    Handles: Register Patient NAME and UR
    '''  
    def patientRegister(self):
        self.startUIWindow()
        ui_patientReg = Ui_Register(self)
        popup = QMessageBox(ui_patientReg)
        ui_patientReg.OK.clicked.connect(self.startUIWindow)
        #check if patient is previous or new
        ui_patientReg.OK.clicked.connect(lambda: self.checkDetail(ui_patientReg))
        ui_patientReg.URnumLine.returnPressed.connect(lambda: self.checkDetail(ui_patientReg))
        ui_patientReg.URnumLine.returnPressed.connect(self.startUIWindow)
        #display dialog
        ui_patientReg.show()

    '''
    Handles: Shows the patient history window
    '''  
    def startUIpatietnHistory(self):
        self.historyWindow = Ui_PatientHistoryWindow(self)
        self.setCentralWidget(self.historyWindow)

        self.historyWindow.Logout.clicked.connect(self.logout) 
        self.historyWindow.changePatient.clicked.connect(self.patientChangeCheckPopUp)
        self.historyWindow.patientSetup.clicked.connect(self.changetoHome)

        self.scroll = QtWidgets.QScrollBar(self.historyWindow.PastSessions)

        historyList = displayPatientHistory(self.currentDetails.patientID,self.currentDetails.ur,self.currentDetails.sessionNum, self.currentDetails.beenExported)
        if (historyList == 0):
            ScrollLabel.UiComponents(self.historyWindow,"no previous sessions saved",self.previousData.wristMVC,self.previousData.fingerMVC,self.previousData.shoulderMVC)
        else:
            ScrollLabel.UiComponents(self.historyWindow,historyList,self.previousData.wristMVC,self.previousData.fingerMVC,self.previousData.shoulderMVC)

        #Checks the name once patient set up is done
        if (self.patientDetail.patientName == None):
            self.historyWindow.label_10.setText(self.historyWindow._translate("OverViewWindow", "Patient: - "))
            self.historyWindow.label_5.setText(self.historyWindow._translate("OverViewWindow", "Session no. -"))
        else:
            self.historyWindow.label_10.setText(self.historyWindow._translate("OverViewWindow", "Patient: {}".format(self.patientDetail.patientName) ))
            self.historyWindow.label_5.setText(self.historyWindow._translate("OverViewWindow", "Session no.{} ".format(self.currentDetails.sessionNum)))
            self.historyWindow.label_5.adjustSize()

        self.historyWindow.overviewSide.clicked.connect(self.startUIWindow)

        self.show()

    
    '''
    Handles: First popup for exercise setup
    '''  
    def startSetUpPopup(self):
        #init the patient setup
        listInfo = self.EXERCISE_SET
        setUpPatient = UIinitPatientSetUp(parent=self, listInfo=listInfo)
        setUpPatient.setStyleSheet("background-color: rgb(255,252,241);");
        popup = QMessageBox(setUpPatient)

        setUpPatient.nextButton.clicked.connect(self.startEnterMeasurementsPopup)

        setUpPatient.show()

    '''
    Handles: Second popup for exercise setup
    '''    
    def startEnterMeasurementsPopup(self):
        
        listInfo = self.EXERCISE_SET
        self.EnterMeasurementsPopup = UIinitMeasurePatientSetUp(parent=self,listInfo=listInfo)

        if ((self.currentDetails.setupMeasWrist != None) and (self.EXERCISE_SET ==1)):
            self.EnterMeasurementsPopup.PatientsNameEnter.setText(self.currentDetails.setupMeasWrist)
        elif((self.currentDetails.setupMeasFinger != None) and (self.EXERCISE_SET ==2)):
            self.EnterMeasurementsPopup.PatientsNameEnter.setText(self.currentDetails.setupMeasFinger)
        elif((self.currentDetails.setupMeasShoulder != None) and (self.EXERCISE_SET ==3)):
            self.EnterMeasurementsPopup.PatientsNameEnter.setText(self.currentDetails.setupMeasShoulder)

        # print(self.startEnterMeasurementsPopup.PatientsNameEnter.text())

        self.EnterMeasurementsPopup.backButton.clicked.connect(self.startSetUpPopup)
        self.EnterMeasurementsPopup.doneButton.clicked.connect(self.sampleEMGPopup)
        self.EnterMeasurementsPopup.show()
    
    '''
    Handles: Third popup for exercise setup
    '''
    def sampleEMGPopup(self):
        self.popup = Ui_SampleEMG(self)
        #making sure functionality is set for each exercise
        if ((self.currentDetails.setupMeasWrist == None) and (self.EXERCISE_SET ==1)):
            self.currentDetails.setupMeasWrist = get_meas_txt()
        elif((self.currentDetails.setupMeasFinger == None) and (self.EXERCISE_SET ==2)):
            self.currentDetails.setupMeasFinger = get_meas_txt()
        elif((self.currentDetails.setupMeasShoulder == None) and (self.EXERCISE_SET ==3)):
            self.currentDetails.setupMeasShoulder = get_meas_txt()      

  
        self.popup.nextButton.clicked.connect(self.startUIWindow)
        self.popup.backBB.clicked.connect(self.startEnterMeasurementsPopup)
        self.popup.show()       

    '''
    Handles: Exercise change
    '''
    def changeExercisePopUp(self):
        changeExercisePopUp = UIchangeExercisePopUp(self)
        self.EXERCISE_SET = 1

        popup = QMessageBox(changeExercisePopUp)
        changeExercisePopUp.WristExtension.clicked.connect(lambda: self.passCurrentExercise(1))
        changeExercisePopUp.FingerFlexion.clicked.connect(lambda: self.passCurrentExercise(2))
        changeExercisePopUp.Deltoid.clicked.connect(lambda: self.passCurrentExercise(3))

        changeExercisePopUp.show()   

#################################################################
         # Small checking dialog popup classes #
#################################################################
    '''
    Go to home window
    '''
    def changetoHome(self):
        popHome = changetohomeUI(self)
        popHome.DONE.clicked.connect(self.startUIWindow)
        popHome.show()    

    '''
    Go to patient name and UR popup
    '''
    def patientCheckPopUp(self):
        ui_patientCheckPopUp = Ui_patientPopUp(self)
        popup = QMessageBox(ui_patientCheckPopUp)
        ui_patientCheckPopUp.DONE.clicked.connect(self.startSetUpPopup)
        ui_patientCheckPopUp.BACK.clicked.connect(self.startUIWindow)
        ui_patientCheckPopUp.show()

    '''
    check if user want to change patient popup
    '''
    def patientChangeCheckPopUp(self):
        ui_patientChangeCheckPopUp = Ui_changePatientPopUp(self)
        popup = QMessageBox(ui_patientChangeCheckPopUp)
        ui_patientChangeCheckPopUp.DONE.clicked.connect(self.changePatientButton)
        ui_patientChangeCheckPopUp.BACK.clicked.connect(self.startUIWindow)
        ui_patientChangeCheckPopUp.show()        

    '''
    Start the exercise selection popup
    '''
    def patientCheckExercisePopUp(self):
        ui_patientCheckPopUp = Ui_checkExercise(self)
        popup = QMessageBox(ui_patientCheckPopUp)
        ui_patientCheckPopUp.BACK.clicked.connect(self.startUIWindow)
        ui_patientCheckPopUp.show()

#################################################################
         # Allows the table to copy and paste #
#################################################################
    '''
    Handles the interupts to be able to copy and paste info from table
    '''
    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.historyWindow.table.selectedRanges()

            if e.key() == QtCore.Qt.Key_C: #copy
                s = '\t'+"\t".join([str(self.historyWindow.table.horizontalHeaderItem(i).text()) for i in range(selected[0].leftColumn(), selected[0].rightColumn()+1)])
                s = s + '\n'

                for r in range(selected[0].topRow(), selected[0].bottomRow()+1):
                    s += self.historyWindow.table.verticalHeaderItem(r).text() + '\t'
                    for c in range(selected[0].leftColumn(), selected[0].rightColumn()+1):
                        try:
                            s += str(self.historyWindow.table.item(r,c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n" #eliminate last '\t'
                self.historyWindow.clip.setText(s)

########################################################################################################################################
                                            # Class functions #
########################################################################################################################################


#################################################################
         # HERE WILL BE USED TO DISP READING VALUE #
#################################################################
    '''
    Return: MVC
    '''
    def get_reading(self):
        # called after measurements have been taken
        mvc = self.popup.myFig.delsysWorker.getMax()
        print("getreading {}".format(mvc))
        return mvc
        # return self.current_delsys_MVC    
    
    '''
    Start EMG reading for MVC
    '''
    def startButtonFun(self):
        self.popup.myFig.delsysWorker.clearEMG()

        self.Window.label_7.setText(self.Window._translate("OverViewWindow", ". . ."))
        self.Window.label_7.adjustSize()

#################################################################
         # Stop Button #
#################################################################
    '''
    User has pressed stop button and needs to check if they want to redo, save, or next exercise
    '''
    def stopButtonCheck(self,exercise):
        stopCheck = Ui_finishEMGReading(self)
        popup = QMessageBox(stopCheck)

        # send stop to EMG thread and update display
        self.popup.myFig.delsysWorker.commands.guiSendStop()
        mvc = self.get_reading()
        self.Window.label_7.setText(self.Window._translate("OverViewWindow","{}".format(mvc)))
        self.Window.label_7.adjustSize()

        #functionality of the buttons
        
        stopCheck.nextExB.clicked.connect(lambda: self.storeReading(exercise))   

        if (exercise == 1):
            #wrist
            stopCheck.redoB.clicked.connect(lambda: self.clearVal(exercise))
            stopCheck.middleB.clicked.connect(lambda: self.checkFinished(exercise))
        elif (exercise == 2):
            #finger
            stopCheck.redoB.clicked.connect(lambda: self.clearVal(exercise))
            stopCheck.middleB.clicked.connect(lambda: self.checkFinished(exercise))
        else:
            #shoulder
            stopCheck.redoB.clicked.connect(lambda: self.clearVal(exercise))
            stopCheck.middleB.clicked.connect(lambda: self.checkFinished(exercise))
        stopCheck.show()

    '''
    checks if the EMG readings are finished
    '''
    def checkFinished(self,n):
        finished = checkFinishedUI(self)
        self.popup.myFig.delsysWorker.clearEMG()
        self.popup.myFig.delsysWorker.commands.guiSendQuit()

        if (n == 1):
            #wrist
            self.currentDetails.wristMVC = self.get_reading()
        elif (n == 2):
            #finger
            self.currentDetails.fingerMVC = self.get_reading()
        elif (n == 3):
            #shoulder
            self.currentDetails.shoulderMVC = self.get_reading()

        finished.BACK.clicked.connect(self.stopButtonCheck)
        finished.DONE.clicked.connect(self.exportData)
        finished.show()

    '''
    stores reading after pressed the NEXT button
    '''
    def storeReading(self,n):
        self.popup.myFig.delsysWorker.clearEMG()
        self.popup.myFig.delsysWorker.commands.guiSendQuit()

        if (n == 1):
            #wrist
            self.currentDetails.wristMVC = self.get_reading()
            self.previousData.wristMVC.append("{}".format(self.currentDetails.wristMVC))
        elif (n == 2):
            #finger
            self.currentDetails.fingerMVC = self.get_reading()
            self.previousData.fingerMVC.append("{}".format(self.currentDetails.fingerMVC))
        elif (n == 3):
            #shoulder
            self.currentDetails.shoulderMVC = self.get_reading()
            self.previousData.shoulderMVC.append("{}".format(self.currentDetails.shoulderMVC))

        self.changeExercisePopUp()

    '''
    clears current reading if REDO is pressed
    '''
    def clearVal(self,exercise):
        print(exercise)
        self.current_delsys_MVC  = None
        if (exercise == 1):
            self.currentDetails.wristMVC = None
        elif (exercise == 2):
            self.currentDetails.fingerMVC = None
        else:
            self.currentDetails.shoulderMVC = None
        self.passCurrentExercise(exercise)
        self.startUIWindow()
        
    """
    clears all patient info from pressing "change patient"
    """
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

        self.patientRegister()

    """
    used to display the current exercise selection
    """
    def passCurrentExercise(self,n):
        self.EXERCISE_SET = n
        self.startUIWindow()

        #setting the test depending on what exercise was chosen
        if n==1:
            self.Window.currentExerciseSelection = "Wrist Extension"
                  
        elif n==2:
            self.Window.currentExerciseSelection = "Finger Flexion"

        elif n==3:
            self.Window.currentExerciseSelection = "Shoulder Flexion"
        
        self.Window.label_4.setText(self.Window._translate("OverViewWindow", self.Window.currentExerciseSelection))
        
        self.Window.show()  

########################################################################################################################################
                                            # init prev patient #
########################################################################################################################################

    '''
    Loads in the previous session data of patient
    '''
    def loadPreviousSessionData(self,ID):
        # find how many sessions they have had
        self.previousData.sessionNum = getNumSessions(ID+self.currentDetails.ur)
        self.currentDetails.sessionNum = (self.previousData.sessionNum + 1)
        self.currentDetails.beenExported = YES
        self.previousData.wristMVC = getPreviousWrist(self.previousData.sessionNum,ID,self.currentDetails.ur)
        self.previousData.shoulderMVC = getPreviousShoulder(self.previousData.sessionNum,ID,self.currentDetails.ur)
        self.previousData.fingerMVC = getPreviousFinger(self.previousData.sessionNum,ID,self.currentDetails.ur)
        self.previousData.setupMeas = getSetupMeasurement(self.previousData.sessionNum,ID,self.currentDetails.ur)

        print(self.previousData.wristMVC)
        print(self.previousData.fingerMVC)
        print(self.previousData.shoulderMVC)

        self.currentDetails.setupMeasWrist = self.previousData.setupMeas[0]
        self.currentDetails.setupMeasFinger = self.previousData.setupMeas[1]
        self.currentDetails.setupMeasShoulder = self.previousData.setupMeas[2]     
        
        self.Window.SessionNum = self.currentDetails.sessionNum
    
    """
    run after patients name is entered 
    Checks id code ( the names initals ) for a current file under the given initals
    IF a current file is there --> load in the data as the patients details
    ELSE continue on new patient files
    input: patient exercise setup class
    """
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
            self.previousData = previousPatientData()
            self.previousData.wristMVC = []
            self.previousData.fingerMVC= []
            self.previousData.shoulderMVC = []
            self.currentDetails.sessionNum = 1
    

        # Start next pop-up for window
        # self.show() 
        self.startUIWindow()


########################################################################################################################################
                                            # Export Function #
########################################################################################################################################
    '''
    This function exports the current session data from currentDetails into a new text file
    '''
    def exportData(self):

        self.currentDetails.beenExported = YES

        # If patients first session must make a new directory for it
        PATH = 'Patient Details/{}'.format((self.currentDetails.patientID+self.currentDetails.ur))
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

'''
runs the whole application
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    sys.exit(app.exec_())
    

