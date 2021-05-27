########################################################################################################################################
# This file:
# - has all of the checking popups for the main windows
# 
# Team 4
# Date Modified: 27/05/2021
# Author: Anna Scolaro 
########################################################################################################################################


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import *
import sys
import os
from PyQt5.QtCore import * 

""" GENERATED FROM PYQT5 DESIGNER 
UIREGISTER: Register UR and Name dialog
This is the class is the layout for the name entering and dialog
"""
class Ui_Register(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(330, 138)
        self.setMaximumSize(QtCore.QSize(330, 138))
        self.setStyleSheet("background-color: rgb(255,252,241)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(310, 10, 20, 101))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 10, 20, 101))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, 10, 291, 101))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(0, 10, 131, 21))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.OK = QtWidgets.QPushButton(self.MAIN)
        self.OK.setGeometry(QtCore.QRect(190, 70, 101, 20))
        self.OK.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                                "color: rgb(37,39,51);\n"
                                "border-top-color: rgb(85, 86, 86);\n"
                                "selection-background-color: rgb(197, 201, 201);\n"
                                "")
        self.OK.setObjectName("OK")
        self.labelPatientsName_2 = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName_2.setGeometry(QtCore.QRect(0, 50, 131, 21))
        self.labelPatientsName_2.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                                                "background-color: rgb(255, 255, 255);\n"
                                                "color: rgb(37,39,51);")
        self.labelPatientsName_2.setObjectName("labelPatientsName_2")
        self.PnameLine = QtWidgets.QLineEdit(self.MAIN)


        self.PnameLine.setStyleSheet("background-color: rgb(255,252,241);\n"
                                        "color: rgb(115, 116, 116);\n"
                                        "selection-color: rgb(207, 212, 212);\n"
                                        "border-color: rgb(156, 160, 159);\n"
                                        "border-bottom-color: rgb(159, 163, 163);")


        self.PnameLine.setGeometry(QtCore.QRect(0, 30, 281, 21))
        self.PnameLine.setObjectName("PnameLine")


        self.URnumLine = QtWidgets.QLineEdit(self.MAIN)
        self.URnumLine.setGeometry(QtCore.QRect(0, 70, 181, 21))
        self.URnumLine.setObjectName("URnumLine")

        self.URnumLine.setStyleSheet("background-color: rgb(255,252,241);\n"
                                        "color: rgb(115, 116, 116);\n"
                                        "selection-color: rgb(207, 212, 212);\n"
                                        "border-color: rgb(156, 160, 159);\n"
                                        "border-bottom-color: rgb(159, 163, 163);")

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.OK.clicked.connect(self.save_UR_and_name)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPatientsName.setText(_translate("MainWindow", "Patient Name:"))
        self.OK.setText(_translate("MainWindow", "OK"))
        self.labelPatientsName_2.setText(_translate("MainWindow", "UR Number:"))

        self.labelPatientsName.adjustSize()
        self.labelPatientsName_2.adjustSize()

    def save_UR_and_name(self):
        text_file = open("./Patient Details/PatientName.txt", "w")
        text_file.writelines('{}\n'.format(self.PnameLine.text()))
        text_file.writelines('{}'.format(self.URnumLine.text()))
        text_file.close()
        self.close() 

        
""" GENERATED FROM PYQT5 DESIGNER 
UIPATIENTPOPUP: Change patient check popup
This is the class to check is you want to change the patient and clear data
"""
class Ui_changePatientPopUp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(313, 90)
        self.setMaximumSize(QtCore.QSize(313, 90))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(293, 0, 20, 81))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 20, 81))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.DONE = QtWidgets.QPushButton(self.centralwidget)
        self.DONE.setGeometry(QtCore.QRect(190, 50, 101, 20))
        self.DONE.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.DONE.setObjectName("DONE")
        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(20, 50, 101, 20))
        self.BACK.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.BACK.setObjectName("BACK")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, -10, 271, 61))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(0, 35, 271, 31))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")

        self.DONE.clicked.connect(self.dialog_exit)
        self.BACK.clicked.connect(self.dialog_exit)   
          
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.DONE.setText(_translate("MainWindow", "OK"))
        self.BACK.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "This will clear current data"))       


        self.labelPatientsName.adjustSize()
    '''
    Closes self and goes to home
    '''
    def dialog_exit(self):
        print("close exercise change patient!")
        self.close()   

######################################################################################################

""" GENERATED FROM PYQT5 DESIGNER 
UICHANGEEXERCISEPOPUP: Change exercise check popup
This is the class that lets you change between the three exercise choices
"""
class UIchangeExercisePopUp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        setupWindow = QtWidgets.QWidget(self)
        setupWindow.setObjectName("MainWindow")
        setupWindow.resize(240, 150)
        setupWindow.setMaximumSize(QtCore.QSize(240, 150))
        setupWindow.setStyleSheet("background-color: rgb(255,252,241)\n")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.RightSide = QtWidgets.QColumnView(self.centralwidget)
        self.RightSide.setGeometry(QtCore.QRect(220, 0, 20, 150))
        self.RightSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.RightSide.setObjectName("RightSide")
        self.leftSide = QtWidgets.QColumnView(self.centralwidget)
        self.leftSide.setGeometry(QtCore.QRect(0, 0, 20, 150))
        self.leftSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.leftSide.setObjectName("leftSide")
        self.windowFrame = QtWidgets.QFrame(self.centralwidget)
        self.windowFrame.setGeometry(QtCore.QRect(20, 0, 201, 150))
        self.windowFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.windowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowFrame.setObjectName("windowFrame")
        self.chooseExercise = QtWidgets.QLabel(self.windowFrame)
        self.chooseExercise.setGeometry(QtCore.QRect(40, 20, 111, 21))
        self.chooseExercise.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")     

        self.chooseExercise.setObjectName("chooseExercise")
        self.WristExtension = QtWidgets.QPushButton(self.windowFrame)
        self.WristExtension.setGeometry(QtCore.QRect(0, 40, 201, 31))
        self.WristExtension.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.WristExtension.setObjectName("WristExtension")
        self.FingerFlexion = QtWidgets.QPushButton(self.windowFrame)
        self.FingerFlexion.setGeometry(QtCore.QRect(0, 80, 201, 31))
        self.FingerFlexion.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.FingerFlexion.setObjectName("FingerFlexion")
        self.Deltoid = QtWidgets.QPushButton(self.windowFrame)
        self.Deltoid.setGeometry(QtCore.QRect(0, 120, 201, 31))
        self.Deltoid.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.Deltoid.setObjectName("Deltoid")


#####################################BUTTON SIGNALS######################################
        self.WristExtension.clicked.connect(self.test_exit)
        self.FingerFlexion.clicked.connect(self.test_exit)
        self.Deltoid.clicked.connect(self.test_exit)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.chooseExercise.setText(_translate("MainWindow", "Choose Exercise:"))
        self.WristExtension.setText(_translate("MainWindow", "Wrist Extension"))
        self.FingerFlexion.setText(_translate("MainWindow", "Finger Flexion"))
        self.Deltoid.setText(_translate("MainWindow", "Shoulder Extension"))

        self.chooseExercise.setAlignment(Qt.AlignCenter)
        self.chooseExercise.adjustSize()

    '''
    This closes the popup to go to home
    '''
    def test_exit(self):
        print("close exercise change popup!")
        self.close()    

######################################################################################################

""" GENERATED FROM PYQT5 DESIGNER 
UIPATIENTPOPUP: Change patient check popup
This is the class that lets you change patients
"""
class Ui_patientPopUp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(313, 90)
        self.setMaximumSize(QtCore.QSize(313, 90))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(293, 0, 20, 81))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 20, 81))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.DONE = QtWidgets.QPushButton(self.centralwidget)
        self.DONE.setGeometry(QtCore.QRect(190, 50, 101, 20))
        self.DONE.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.DONE.setObjectName("DONE")
        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(20, 50, 101, 20))
        self.BACK.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.BACK.setObjectName("BACK")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, -10, 271, 61))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(0 , 20, 271, 31))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")

        self.DONE.clicked.connect(self.dialog_exit)
        self.BACK.clicked.connect(self.dialog_exit)   
          
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.DONE.setText(_translate("MainWindow", "OK"))
        self.BACK.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "Are you sure you want to change Patient"))       

    def dialog_exit(self):
        print("close exercise change popup!")
        self.close()   

######################################################################################################

""" GENERATED FROM PYQT5 DESIGNER 
UIPATIENTPOPUP: Set up patient dialog
This is the class that lets you setup the patients data
"""
class Ui_needPatientSetup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(313, 90)
        self.setMaximumSize(QtCore.QSize(313, 90))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(293, 0, 20, 81))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 20, 81))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.DONE = QtWidgets.QPushButton(self.centralwidget)
        self.DONE.setGeometry(QtCore.QRect(190, 50, 101, 20))
        self.DONE.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.DONE.setObjectName("DONE")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, -10, 271, 61))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(0, 20, 271, 31))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")

        self.DONE.clicked.connect(self.dialog_exit)
          
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.DONE.setText(_translate("MainWindow", "OK"))
        self.labelPatientsName.setText(_translate("MainWindow", "You need to select Activity"))       

    '''
    Closes dialog and goes to home
    '''
    def dialog_exit(self):
        print("close exercise change popup!")
        self.close()   

""" GENERATED FROM PYQT5 DESIGNER 
UICHECKEXERCISE: Make sure they have selected an exercise dialogs
"""
class Ui_checkExercise(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(313, 90)
        self.setMaximumSize(QtCore.QSize(313, 90))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(293, 0, 20, 81))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 20, 81))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")

        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(110, 50, 101, 20))
        self.BACK.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(45,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.BACK.setObjectName("BACK")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, -10, 271, 61))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(0, 35, 271, 31))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")

        self.BACK.clicked.connect(self.dialog_exit)   
          
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.BACK.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "You need to select Activity"))       


        self.labelPatientsName.adjustSize()

    '''
    Closes dialog to home
    '''
    def dialog_exit(self):
        print("Please Select Exercise First")
        self.close()   


""" GENERATED FROM PYQT5 DESIGNER 
UIFINISHEMGREADING: displays after pressing stop
shows REDO, SAVE and NEXT EXERCISE
"""
class Ui_finishEMGReading(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("MainWindow")
        self.resize(400, 160)
        self.setMaximumSize(QtCore.QSize(400, 160))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                                        "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(380, 0, 20, 131))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, -10, 20, 141))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.redoB = QtWidgets.QPushButton(self.centralwidget)
        self.redoB.setGeometry(QtCore.QRect(30, 0, 101, 131))
        self.redoB.setStyleSheet("background-color: rgb(255, 238, 245);\n"
                                "color: rgb(37,39,51);\n"
                                "border-top-color: rgb(85, 86, 86);\n"
                                "selection-background-color: rgb(197, 201, 201);\n"
                                "")
        self.redoB.setObjectName("redoB")
        self.middleB = QtWidgets.QPushButton(self.centralwidget)
        self.middleB.setGeometry(QtCore.QRect(150, 0, 101, 131))
        self.middleB.setStyleSheet("background-color: rgb(238, 255, 254);\n"
                                        "color: rgb(37,39,51);\n"
                                        "border-top-color: rgb(85, 86, 86);\n"
                                        "selection-background-color: rgb(197, 201, 201);\n"
                                        "")
        self.middleB.setObjectName("middleB")
        self.nextExB = QtWidgets.QPushButton(self.centralwidget)
        self.nextExB.setGeometry(QtCore.QRect(270, 0, 101, 131))
        self.nextExB.setStyleSheet("background-color: rgb(241, 255, 216);\n"
                                        "color: rgb(37,39,51);\n"
                                        "border-top-color: rgb(85, 86, 86);\n"
                                        "selection-background-color: rgb(197, 201, 201);\n"
                                        "")
        self.nextExB.setObjectName("nextExB")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 24))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        
        self.nextExB.clicked.connect(self.dialog_exit)
        self.middleB.clicked.connect(self.dialog_exit)
        self.redoB.clicked.connect(self.dialog_exit)


        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.redoB.setText(_translate("MainWindow", "REDO"))
        self.middleB.setText(_translate("MainWindow", "Save and finish  \n"
                                                        " session"))
        self.nextExB.setText(_translate("MainWindow", "Next Exercise"))

    '''
    Closes dialog to home
    '''
    def dialog_exit(self):
        self.close()   


""" GENERATED FROM PYQT5 DESIGNER 
CHANGETOHOMEUI: Dialog to tell them they must be on home
"""
class changetohomeUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(313, 90)
        self.setMaximumSize(QtCore.QSize(313, 90))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(293, 0, 20, 81))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 20, 81))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.DONE = QtWidgets.QPushButton(self.centralwidget)
        self.DONE.setGeometry(QtCore.QRect(190, 50, 101, 20))
        self.DONE.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.DONE.setObjectName("DONE")
        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(20, 50, 101, 20))
        self.BACK.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.BACK.setObjectName("BACK")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, -10, 271, 61))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(0 , 30, 271, 31))
        self.labelPatientsName.setStyleSheet("font: 13pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")

        self.DONE.clicked.connect(self.dialog_exit)
        self.BACK.clicked.connect(self.dialog_exit)   
          
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.DONE.setText(_translate("MainWindow", "Go to home"))
        self.BACK.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "You must be on HOME to do this"))  
        self.labelPatientsName.adjustSize()

    '''
    Closes dialog to home
    '''
    def dialog_exit(self):
        print("Please change to home")
        self.close()   


""" GENERATED FROM PYQT5 DESIGNER 
CHECKFINISHEDUI: Check the user really wants to end the session
"""
class checkFinishedUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(313, 110)
        self.setMaximumSize(QtCore.QSize(313, 110))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.right = QtWidgets.QColumnView(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(290, 0, 25, 110))
        self.right.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.right.setObjectName("right")
        self.left = QtWidgets.QColumnView(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 20, 110))
        self.left.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.left.setObjectName("left")
        self.DONE = QtWidgets.QPushButton(self.centralwidget)
        self.DONE.setGeometry(QtCore.QRect(190, 70, 101, 20))
        self.DONE.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.DONE.setObjectName("DONE")
        self.BACK = QtWidgets.QPushButton(self.centralwidget)
        self.BACK.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.BACK.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.BACK.setObjectName("BACK")
        self.MAIN = QtWidgets.QFrame(self.centralwidget)
        self.MAIN.setGeometry(QtCore.QRect(20, -10, 271, 81))
        self.MAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MAIN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MAIN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MAIN.setObjectName("MAIN")
        self.labelPatientsName = QtWidgets.QLabel(self.MAIN)
        self.labelPatientsName.setGeometry(QtCore.QRect(30 , 20, 271, 50))
        self.labelPatientsName.setStyleSheet("font: 13pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")

        self.DONE.clicked.connect(self.dialog_exit)
        self.BACK.clicked.connect(self.dialog_exit)   
          
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.DONE.setText(_translate("MainWindow", "Save"))
        self.BACK.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "This will end the Session if you want to\n continue click BACK and NEXT"))  
        self.labelPatientsName.adjustSize()

    '''
    Closes dialog to home
    '''
    def dialog_exit(self):
        print("Please change to home")
        self.close()  
