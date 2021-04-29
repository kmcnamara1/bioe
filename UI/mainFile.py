
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QMessageBox, QDialog,QDialogButtonBox,QVBoxLayout
import sys
from UI_1and2 import UIWindow, UIToolTab, UIinitPatientSetUp,UIinitMeasurePatientSetUp,UIchangeExercisePopUp



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



def close_all():
        sys.exit(0)

def wrist_exercise_():
    wrist_exercise_str()

def wrist_exercise_str():
    print("Wrist Extension")
    res = "Wrist Extension"
    return res

def loadPatientName():
        text_file = open("Patient Details/PatientName.txt", "r+")
        data = text_file.read()
        
        if data == None:
                text_file.truncate(0)
                text_file.close()
                return "-"
        else:
                text_file.truncate(0)
                text_file.close()
                return data

def loadClinicianName():
        text_file = open("ClinicanName.txt", "r")
        data = text_file.read()
        text_file.close()
        print(data)
        return data

# We assume the patient name is split with a space 
def checkPatientDetails(patientDetail,name):
    

    patientDetail.patientName = name

    # print(patientName)
    name_list = patientDetail.patientName.split() 

    initials = ""

    for name in name_list:  # go through each name
        initials += name[0].upper()  # append the initial
    
    print(initials)
    print("\n")
    #Now that we have the initals we can check if a document exist with the details
    if checkReturningPatient(initials) == 0:
        patientDetail.clinicanName = loadClinicianName()
        patientDetail.date = 1
        patientDetail.patientID = initials
        print(patientDetail.patientName)
    else:
        pass

    print(patientDetail.clinicanName)
    print("\n")
    print(patientDetail.patientID)


    # print(checkReturningPatient(initials))
    # else:


def checkReturningPatient(initials):
    file_path = ("Patient Details/{}.txt".format(initials))
    try:
        text_file = open( file_path, "r+")
        text_file.close()
        return 1
    except IOError:
        return 0



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(1280, 800)
        self.setStyleSheet("background-color: rgb(255,252,241);");
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
        # setUpPatient.nextButton.clicked.connect(self.startEnterMeasurementsPopup)
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

    # Run after patients name is entered 
    # Checks id code ( the names initals ) for a current file under the given initals
    # IF a current file is there --> load in the data as the patients details
    # ELSE continue on new patient files
    def checkDetail(self,setUpPatient):
        name=setUpPatient.PatientsNameEnter.text()
        checkPatientDetails(self.patientDetail,name)
        self.startEnterMeasurementsPopup()


        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    

