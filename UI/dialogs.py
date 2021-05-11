
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QDialog, QLabel,QDialogButtonBox,QVBoxLayout,QHBoxLayout,QScrollArea,QVBoxLayout
import sys
import os
from PyQt5.QtCore import * 

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
        self.labelPatientsName.setGeometry(QtCore.QRect(0, 20, 271, 31))
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

    def dialog_exit(self):
        print("close exercise change popup!")
        self.close()   

######################################################################################################

class UIchangeExercisePopUp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        setupWindow = QtWidgets.QWidget(self)
        setupWindow.setObjectName("MainWindow")
        setupWindow.resize(240, 259)
        setupWindow.setMaximumSize(QtCore.QSize(1280, 16777215))
        setupWindow.setStyleSheet("background-color: rgb(255,252,241)\n")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.RightSide = QtWidgets.QColumnView(self.centralwidget)
        self.RightSide.setGeometry(QtCore.QRect(220, 0, 20, 211))
        self.RightSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.RightSide.setObjectName("RightSide")
        self.leftSide = QtWidgets.QColumnView(self.centralwidget)
        self.leftSide.setGeometry(QtCore.QRect(0, 0, 20, 211))
        self.leftSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.leftSide.setObjectName("leftSide")
        self.windowFrame = QtWidgets.QFrame(self.centralwidget)
        self.windowFrame.setGeometry(QtCore.QRect(20, 0, 201, 211))
        self.windowFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.windowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowFrame.setObjectName("windowFrame")
        self.chooseExercise = QtWidgets.QLabel(self.windowFrame)
        self.chooseExercise.setGeometry(QtCore.QRect(50, 10, 111, 21))
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
#########################################################################################

        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 24))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.chooseExercise.setText(_translate("MainWindow", "Choose Exercise:"))
        self.WristExtension.setText(_translate("MainWindow", "Wrist Extension"))
        self.FingerFlexion.setText(_translate("MainWindow", "Finger Flexion"))
        self.Deltoid.setText(_translate("MainWindow", "Deltoid ----"))
        # self.exitexerciseButton.setText(_translate("MainWindow", "EXIT"))
        # self.doneButton2.setText(_translate("MainWindow", "DONE"))

    def test_exit(self):
        print("close exercise change popup!")
        self.close()    

######################################################################################################

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
        self.labelPatientsName.setGeometry(QtCore.QRect(0, 20, 271, 31))
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
