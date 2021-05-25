########################################################################################################################################
# This file:
# - has all of the main GUI window designs
# 
# Team 4
# Date Modified: 25/05/2021
# Author: Anna Scolaro 
########################################################################################################################################


from __future__ import annotations
from typing import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon,QFont
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QDialog, QLabel,QDialogButtonBox,QVBoxLayout,QHBoxLayout,QScrollArea,QVBoxLayout
import sys
import os
from PyQt5.QtCore import * 

from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib as mpl
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim
import numpy as np
from numpy.core.records import array
from delsys_func import *




def loadPatientName():
        # dir_path = os.path.dirname(os.path.realpath(__file__))
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
        text_file = open("ClinicianName.txt", "r")
        data = text_file.read()
        text_file.close()
        return data


class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))

        self.currentExerciseSelection = None
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(890, 170, 141, 71))
        self.startButton.setStyleSheet("background-color: rgb(111, 207, 151);border-color: rgb(34, 34, 34);")
        self.startButton.setObjectName("startButton")

        #icon!
        self.startButton.setIcon(QIcon('icons/play-button.png')) 
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(1050, 170, 141, 71))
        self.stopButton.setStyleSheet("background-color: rgb(235,87,87)")
        self.stopButton.setObjectName("stopButton")

        #icon!
        self.stopButton.setIcon(QIcon('icons/square.png'))     

        self.changeExerciseButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeExerciseButton.setGeometry(QtCore.QRect(890, 280, 141, 71))
        self.changeExerciseButton.setStyleSheet("background-color: rgb(242, 201, 76)")
        self.changeExerciseButton.setObjectName("changeExerciseButton")
        self.ExportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportDataButton.setGeometry(QtCore.QRect(1050, 280, 141, 71))
        self.ExportDataButton.setStyleSheet("background-color: rgb(242,153,74)")
        self.ExportDataButton.setObjectName("ExportDataButton")


        #icon!
        self.ExportDataButton.setIcon(QIcon('icons/export.png'))



        self.SideColum = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum.setGeometry(QtCore.QRect(0, 0, 201, 741))
        self.SideColum.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum.setObjectName("SideColum")
        self.overviewSide = QtWidgets.QPushButton(self.centralwidget)
        self.overviewSide.setGeometry(QtCore.QRect(0, 90, 201, 41))
        self.overviewSide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        self.overviewSide.setObjectName("overviewSide")
        self.historySide = QtWidgets.QPushButton(self.centralwidget)
        self.historySide.setGeometry(QtCore.QRect(0, 130, 201, 41))
        self.historySide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")

        
        self.historySide.setObjectName("historySide")

        self.patientSetup = QtWidgets.QPushButton(self.centralwidget)
        self.patientSetup.setGeometry(QtCore.QRect(0, 170, 201, 41))
        self.patientSetup.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        self.patientSetup.setObjectName("patientSetup")
        self.Logout = QtWidgets.QPushButton(self.centralwidget)
        self.Logout.setGeometry(QtCore.QRect(0, 680, 201, 41))
        self.Logout.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";\n"
                "border-color: rgb(34, 34, 34);")
        self.Logout.setObjectName("Logout")


        self.Logout.clicked.connect(self.exit)

        self.changePatient = QtWidgets.QPushButton(self.centralwidget)
        self.changePatient.setGeometry(QtCore.QRect(0, 630, 201, 41))
        self.changePatient.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        
        self.changePatient.setObjectName("changePatient")
        self.WelcomeFrame = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame.setGeometry(QtCore.QRect(400, 160, 431, 101))
        self.WelcomeFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame.setObjectName("WelcomeFrame")
        self.label_3 = QtWidgets.QLabel(self.WelcomeFrame)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 101, 41))

        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                        "color: #7f7f7f")       

        self.label_3.setFont(QFont('.AppleSystemUIFont', 24))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.WelcomeFrame)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 190, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "color:#323232")

        self.label_4.setFont(QFont('.AppleSystemUIFont', 24))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 20, 250, 31))
        self.label_5.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color:#323232")
        self.label_5.setObjectName("label_5")
        self.WelcomeFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_2.setGeometry(QtCore.QRect(400, 270, 211, 91))
        self.WelcomeFrame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_2.setObjectName("WelcomeFrame_2")
        self.label_6 = QtWidgets.QLabel(self.WelcomeFrame_2)
        self.label_6.setGeometry(QtCore.QRect(90, 20, 31, 31))
        self.label_6.setStyleSheet("font: 14pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color: #7f7f7f")


        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.WelcomeFrame_2)
        self.label_7.setGeometry(QtCore.QRect(50, 40, 110, 41))
        self.label_7.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color:#323232")
        self.label_7.setObjectName("label_7")
        self.WelcomeFrame_3 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_3.setGeometry(QtCore.QRect(620, 270, 211, 91))
        self.WelcomeFrame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_3.setObjectName("WelcomeFrame_3")
        self.label_8 = QtWidgets.QLabel(self.WelcomeFrame_3)
        self.label_8.setGeometry(QtCore.QRect(90, 20, 31, 31))
        self.label_8.setStyleSheet("font: 14pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color: #7f7f7f")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.WelcomeFrame_3)
        self.label_9.setGeometry(QtCore.QRect(90, 40, 51, 41))
        self.label_9.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color:#323232")
        self.label_9.setObjectName("label_9")
        self.WelcomeFrame_4 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_4.setGeometry(QtCore.QRect(210, 0, 1061, 51))
        self.WelcomeFrame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_4.setObjectName("WelcomeFrame_4")
        self.label_10 = QtWidgets.QLabel(self.WelcomeFrame_4)
        self.label_10.setGeometry(QtCore.QRect(820, 20, 231, 31))
        self.label_10.setStyleSheet("font: 18pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color: #7f7f7f")
        self.label_10.setObjectName("label_10")
        self.WelcomeFrame_5 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_5.setGeometry(QtCore.QRect(0, 0, 201, 91))
        self.WelcomeFrame_5.setStyleSheet("background-color: rgba(106, 108, 108, 157); color: white;\n"
                "")
        self.WelcomeFrame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_5.setObjectName("WelcomeFrame_5")
        self.label_13 = QtWidgets.QLabel(self.WelcomeFrame_5)
        self.label_13.setGeometry(QtCore.QRect(70, 20, 51, 31))
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.WelcomeFrame_5)
        self.label_14.setGeometry(QtCore.QRect(50, 40, 100, 31))
        self.label_14.setStyleSheet("font: 13pt \".AppleSystemUIFont\";")
        self.label_14.setObjectName("label_14")
        self.startButton.raise_()
        self.stopButton.raise_()
        self.changeExerciseButton.raise_()
        self.ExportDataButton.raise_()
        self.SideColum.raise_()
        self.overviewSide.raise_()
        self.historySide.raise_()
        self.patientSetup.raise_()
        self.Logout.raise_()
        self.changePatient.raise_()
        self.WelcomeFrame.raise_()
        self.WelcomeFrame_2.raise_()
        self.WelcomeFrame_3.raise_()
        self.WelcomeFrame_4.raise_()
        self.label_5.raise_()
        self.WelcomeFrame_5.raise_()
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self._translate = QtCore.QCoreApplication.translate

        self.startButton.setText(self._translate("OverViewWindow", "Start"))
        self.stopButton.setText(self._translate("OverViewWindow", "Stop"))
        self.changeExerciseButton.setText(self._translate("OverViewWindow", "Change Exercise"))
        self.ExportDataButton.setText(self._translate("OverViewWindow", "Save Data"))
        self.overviewSide.setText(self._translate("OverViewWindow", "Home"))
        self.historySide.setText(self._translate("OverViewWindow", "History"))
        self.patientSetup.setText(self._translate("OverViewWindow", "Exercise Setup"))
        self.Logout.setText(self._translate("OverViewWindow", "Logout"))
        self.changePatient.setText(self._translate("OverViewWindow", "Change Patient"))
        self.label_3.setText(self._translate("OverViewWindow", "ACTIVITY"))

        # self.currentExerciseSelection 
        if self.currentExerciseSelection == None:
                self.label_4.setText(self._translate("OverViewWindow", "Select Exercise"))
        else:
                self.label_4.setText(self._translate("OverViewWindow", self.currentExerciseSelection))


        self.SessionNum = ''
        self.label_5.setText(self._translate("OverViewWindow", "Session no.{} ".format(self.SessionNum)))
        self.label_6.setText(self._translate("OverViewWindow", "MVC"))
        self.label_7.setText(self._translate("OverViewWindow", "---.--mV"))
        self.label_8.setText(self._translate("OverViewWindow", "REP"))
        self.label_9.setText(self._translate("OverViewWindow", "-/3"))

        self.patientName = loadPatientName()

        self.label_10.setText(self._translate("OverViewWindow", "Patient: {}".format(self.patientName) ))
        self.label_13.setText(self._translate("OverViewWindow", "Clinician"))

        clinicianName = loadClinicianName()

        self.label_14.setText(self._translate("OverViewWindow", clinicianName ))

        self.label_3.adjustSize()
        self.label_3.setGeometry(QtCore.QRect(170, 20, (self.label_3.width() + 25), 35))
        self.label_4.adjustSize()
        self.label_8.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        
        self.label_4.setGeometry(QtCore.QRect(130, 50, (self.label_4.width() + 25), 41))

    def exit(self):
            self.close()

###############################################################################################################

class UIToolTab(QWidget):
    def __init__(self, parent=None):
        super(UIToolTab, self).__init__(parent)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget") 
        self.SideColum_2 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_2.setGeometry(QtCore.QRect(1261, 0, 20, 741))
        self.SideColum_2.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_2.setObjectName("SideColum_2")  

        self.WelcomeFrame = QtWidgets.QFrame(self)
        self.WelcomeFrame.setGeometry(QtCore.QRect(400, 100, 491, 151))
        self.WelcomeFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame.setObjectName("WelcomeFrame")

        self.label_3 = QtWidgets.QLabel(self.WelcomeFrame)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 231, 111))
        # self.label_3.setStyleSheet("font: 48pt \".AppleSystemUIFont\";\n" 
        # "background-color: rgb(255, 255, 255);\n"
        # "color: rgb(37,39,51);")

        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(37,39,51);")
        self.label_3.setFont(QFont('.AppleSystemUIFont', 48))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.LoginFrame = QtWidgets.QFrame(self.centralwidget)
        self.LoginFrame.setGeometry(QtCore.QRect(440, 280, 411, 121))
        self.LoginFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginFrame.setObjectName("LoginFrame")

        self.startButton = QtWidgets.QPushButton(self.LoginFrame)
        self.startButton.setGeometry(QtCore.QRect(300, 90, 101, 20))
        self.startButton.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
        "color: rgb(37,39,51);\n"
        "border-top-color: rgb(85, 86, 86);\n"
        "selection-background-color: rgb(197, 201, 201);\n"
        "")       

        self.startButton.setObjectName("startButton")
        self.startButton.setCheckable(True)
        self.startButton.toggle()
        # self.startButton.clicked.connect(self.txtstate)
        
        self.lineEdit = QtWidgets.QLineEdit(self.LoginFrame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 321, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255,252,241);\n"
                                        "color: rgb(115, 116, 116);\n"
                                        "selection-color: rgb(207, 212, 212);\n"
                                        "border-color: rgb(156, 160, 159);\n"
                                        "border-bottom-color: rgb(159, 163, 163);")
        self.lineEdit.setObjectName("lineEdit")

#################################Setting for typing input and print on enter################################### 
       

        self.lineEdit.returnPressed.connect(self.txtstate)
        self.startButton.clicked.connect(self.txtstate)

        self.startButton.setIcon(QIcon('icons/ENTER.png'))
###############################################################################################################
     
        self.label = QtWidgets.QLabel(self.LoginFrame)
        self.label.setGeometry(QtCore.QRect(190, 17, 71, 21))
        self.label.setStyleSheet("color: rgb(37,39,51)")
        
        self.label.setFont(QFont('.AppleSystemUIFont', 18))
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.LoginFrame)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_2.setStyleSheet("color: rgb(37,39,51)\n"
                "")
        self.label_2.setObjectName("label_2")


        self.SideColum_3 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_3.setGeometry(QtCore.QRect(890, 90, 20, 171))
        self.SideColum_3.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_3.setObjectName("SideColum_3")
        self.SideColum_4 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_4.setGeometry(QtCore.QRect(380, 90, 20, 171))
        self.SideColum_4.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_4.setObjectName("SideColum_4")
        self.SideColum_5 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_5.setGeometry(QtCore.QRect(420, 240, 451, 16))
        self.SideColum_5.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_5.setObjectName("SideColum_5")
        self.SideColum_6 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_6.setGeometry(QtCore.QRect(420, 90, 451, 16))
        self.SideColum_6.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_6.setObjectName("SideColum_6")
        self.SideColum_7 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_7.setGeometry(QtCore.QRect(0, 0, 20, 741))
        self.SideColum_7.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_7.setObjectName("SideColum_7")
        self.extButton = QtWidgets.QPushButton(self.centralwidget)
        self.extButton.setGeometry(QtCore.QRect(30, 720, 41, 20))
        self.extButton.setStyleSheet("background-color: rgba(237, 255, 229, 242);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.extButton.setObjectName("extButton")
        # self.extButton.clicked.connect(self.exitUI)

        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.LoginFrame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        # LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.LoginFrame)
        self.statusbar.setObjectName("statusbar")
        # LoginWindow.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.LoginFrame.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label_3.setText(_translate("LoginWindow", "WELCOME"))
        self.startButton.setText(_translate("LoginWindow", "ENTER"))
        self.label.setText(_translate("LoginWindow", "LOGIN: "))
        self.label_2.setText(_translate("LoginWindow", "NAME:"))
        self.extButton.setText(_translate("LoginWindow", "EXIT"))


        self.label_3.adjustSize()
        self.label.adjustSize()

    def txtstate(self):
        text_input = self.lineEdit.text()
        text_file = open("ClinicianName.txt", "w")
        text_file.write("%s" % text_input)
        text_file.close()


###############################################################################################################

class Ui_PatientHistoryWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_PatientHistoryWindow, self).__init__(parent)
        # self.scroll = QScrollArea()   

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.SideColum = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum.setGeometry(QtCore.QRect(0, 0, 201, 741))
        self.SideColum.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum.setObjectName("SideColum")
        self.overviewSide = QtWidgets.QPushButton(self.centralwidget)
        self.overviewSide.setGeometry(QtCore.QRect(0, 90, 201, 41))
        self.overviewSide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        self.overviewSide.setObjectName("overviewSide")
        self.historySide = QtWidgets.QPushButton(self.centralwidget)
        self.historySide.setGeometry(QtCore.QRect(0, 130, 201, 41))
        self.historySide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        self.historySide.setObjectName("historySide")
        self.patientSetup = QtWidgets.QPushButton(self.centralwidget)
        self.patientSetup.setGeometry(QtCore.QRect(0, 170, 201, 41))
        self.patientSetup.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        self.patientSetup.setObjectName("patientSetup")
        self.Logout = QtWidgets.QPushButton(self.centralwidget)
        self.Logout.setGeometry(QtCore.QRect(0, 680, 201, 41))
        self.Logout.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";\n"
                "border-color: rgb(34, 34, 34);")
        self.Logout.setObjectName("Logout")
        self.changePatient = QtWidgets.QPushButton(self.centralwidget)
        self.changePatient.setGeometry(QtCore.QRect(0, 630, 201, 41))
        self.changePatient.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
                ";")
        self.changePatient.setObjectName("changePatient")
        self.pastSesholder = QtWidgets.QFrame(self.centralwidget)
        self.pastSesholder.setGeometry(QtCore.QRect(550, 70, 431, 61))
        self.pastSesholder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pastSesholder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pastSesholder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pastSesholder.setObjectName("pastSesholder")
        self.pastSesTitle = QtWidgets.QLabel(self.pastSesholder)
        self.pastSesTitle.setGeometry(QtCore.QRect(125, 00, 181, 41))
        self.pastSesTitle.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color: #7f7f7f")
        self.pastSesTitle.setObjectName("pastSesTitle")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 20, 171, 31))
        self.label_5.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color:#323232")
        self.label_5.setObjectName("label_5")
        self.WelcomeFrame_4 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_4.setGeometry(QtCore.QRect(210, 0, 1061, 51))
        self.WelcomeFrame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_4.setObjectName("WelcomeFrame_4")
        self.label_10 = QtWidgets.QLabel(self.WelcomeFrame_4)
        self.label_10.setGeometry(QtCore.QRect(820, 20, 231, 31))
        self.label_10.setStyleSheet("font: 18pt \".AppleSystemUIFont\"; \n"
                "background-color: rgb(255, 255, 255);\n"
                "color: #7f7f7f")
        self.label_10.setObjectName("label_10")
        self.WelcomeFrame_5 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_5.setGeometry(QtCore.QRect(0, 0, 201, 91))
        self.WelcomeFrame_5.setStyleSheet("background-color: rgba(106, 108, 108, 157); color: white;\n"
                "")
        self.WelcomeFrame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_5.setObjectName("WelcomeFrame_5")
        self.label_13 = QtWidgets.QLabel(self.WelcomeFrame_5)
        self.label_13.setGeometry(QtCore.QRect(70, 20, 51, 31))
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.WelcomeFrame_5)
        self.label_14.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.label_14.setStyleSheet("font: 13pt \".AppleSystemUIFont\";")
        self.label_14.setObjectName("label_14")

        self.PastSessions = QtWidgets.QFrame(self.centralwidget)
        self.PastSessions.setGeometry(QtCore.QRect(450, 150, 621, 581))
        self.PastSessions.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PastSessions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PastSessions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PastSessions.setObjectName("PastSessions")

        self.SideColum.raise_()
        self.overviewSide.raise_()
        self.historySide.raise_()
        self.patientSetup.raise_()
        self.Logout.raise_()
        self.changePatient.raise_()
        self.pastSesholder.raise_()
        self.WelcomeFrame_4.raise_()
        self.label_5.raise_()
        self.WelcomeFrame_5.raise_()
        self.PastSessions.raise_()

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        self.overviewSide.setText(self._translate("MainWindow", "Home"))
        self.historySide.setText(self._translate("MainWindow", "History"))
        self.patientSetup.setText(self._translate("MainWindow", "Exercise Setup"))
        self.Logout.setText(self._translate("MainWindow", "Logout"))
        self.changePatient.setText(self._translate("MainWindow", "Change Patient"))
        self.pastSesTitle.setText(self._translate("MainWindow", "Past Sessions"))
        self.label_5.setText(self._translate("MainWindow", "Session no. "))
        self.label_10.setText(self._translate("MainWindow", "Paitent: Jone Swith"))
        clinicianName = loadClinicianName()
        self.label_14.setText(self._translate("OverViewWindow", clinicianName ))
        self.label_13.setText(self._translate("MainWindow", "Clinician"))

        self.pastSesTitle.adjustSize()


###############################################################################################################
class UIinitPatientSetUp(QDialog):
    
    def __init__(self,listInfo,parent=None):
        super().__init__(parent)

        self.listInfo = listInfo

        Dialog = QtWidgets.QDialog(self)
        Dialog.setObjectName("Dialog")
        self.resize(450, 487)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")  

        Dialog.setStyleSheet("background-color: rgb(255,252,241)\n")

        self.layout = QVBoxLayout()

        self.MuscleDemo = QtWidgets.QFrame(self.centralwidget)
        self.MuscleDemo.setGeometry(QtCore.QRect(20, 30, 411, 320))
        self.MuscleDemo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MuscleDemo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MuscleDemo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MuscleDemo.setObjectName("MuscleDemo")

        self.findmuscleLabl = QtWidgets.QLabel(self.MuscleDemo)
        self.findmuscleLabl.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.findmuscleLabl.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "color: rgb(37,39,51)")
        self.findmuscleLabl.setObjectName("findmuscleLabl")

        self.examplemusclelabel = QtWidgets.QLabel(self.MuscleDemo)
        if (listInfo == 1):
                muscle = 'wrist'
                pixmap = QPixmap('icons/wrist1.jpg')
                self.examplemusclelabel.setPixmap(pixmap)
                self.examplemusclelabel.resize(pixmap.width()*1.8, pixmap.height()*1.8)
                self.examplemusclelabel.move(30,-20)
        elif (listInfo == 2):
                muscle = 'finger'
                pixmap = QPixmap('icons/finger1.jpg')
                self.examplemusclelabel.setPixmap(pixmap)
                # self.examplemusclelabel.resize(pixmap.width()*1.5, pixmap.height()*1.8)
                self.examplemusclelabel.move(40,50)                
        else:
                muscle = 'shoulder'
                pixmap = QPixmap('icons/shoulder1.jpg')
                self.examplemusclelabel.setPixmap(pixmap)
                self.examplemusclelabel.resize(pixmap.width()*1.8, pixmap.height()*1.8)
                self.examplemusclelabel.move(40,-120)


        self.exampleLabel = QtWidgets.QLabel(self.MuscleDemo)
        self.exampleLabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.exampleLabel.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "color: rgb(37,39,51)")
        self.exampleLabel.setObjectName("exampleLabel")


        self.RigthSide = QtWidgets.QColumnView(self.centralwidget)
        self.RigthSide.setGeometry(QtCore.QRect(430, 0, 20, 441))
        self.RigthSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.RigthSide.setObjectName("RigthSide")

   
        self.findmuscleLabl.raise_()
        self.leftSide = QtWidgets.QColumnView(self.centralwidget)
        self.leftSide.setGeometry(QtCore.QRect(0, 0, 20, 441))
        self.leftSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.leftSide.setObjectName("leftSide")
        
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(330, 420, 101, 20))
        self.nextButton.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")

        self.nextButton.setObjectName("nextButton")

        self.nextButton.clicked.connect(self.test_exit)


        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(20, 420, 101, 20))
        self.exitButton.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.test_exit)

        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")


        _translate = QtCore.QCoreApplication.translate
        # self.labelPatientsName.setText(_translate("Dialog", "Please Enter Patient\'s Name:"))

        # self.labelPatientUR.setText(_translate("Dialog", "Patient UR Number:"))
        
        self.findmuscleLabl.setText(_translate("Dialog", ("Find the {} muscle belly").format(muscle)))


        self.exampleLabel.setText(_translate("Dialog", "Example:"))
        self.exitButton.setText(_translate("Dialog", "Exit")) 
        self.nextButton.setText(_translate("Dialog", "Next")) 

        # self.labelPatientUR.adjustSize()
        # self.labelPatientsName.adjustSize()
        self.findmuscleLabl.adjustSize()
        self.exampleLabel.adjustSize()    

    def test_exit(self):
        print("close popup!")
        self.close()  
          

    def get_patient_name(self):
        text_input = self.patientSetup.text()
        print(text_input)
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        text_file = open("Patient Details/PatientName.txt", "w")
        text_file.write("%s" % text_input)
        # print(text_input)
        text_file.close()  

#     def get_patient_UR(self):
#         text_input = self.patientSetup.text()
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         text_file = open(dir_path + "\Patient Details\PatientName.txt", "a")
#         text_file.write("\n%s" % text_input)
#         # print(text_input)
#         text_file.close()  

###############################################################################################################
class UIinitMeasurePatientSetUp(QDialog):
    
    def __init__(self,listInfo,parent=None):
        super().__init__(parent)

        self.listInfo = listInfo

        setupWindow = QtWidgets.QWidget(self)
        setupWindow.setObjectName("MainWindow")
        setupWindow.resize(450, 487)
        setupWindow.setMaximumSize(QtCore.QSize(1280, 16777215))
        setupWindow.setStyleSheet("background-color: rgb(255,252,241)\n")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.MuscleDemo = QtWidgets.QFrame(self.centralwidget)
        self.MuscleDemo.setGeometry(QtCore.QRect(20, 0, 411, 301))
        self.MuscleDemo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MuscleDemo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MuscleDemo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MuscleDemo.setObjectName("MuscleDemo")
        self.findmuscleLabl = QtWidgets.QLabel(self.MuscleDemo)

        self.findmuscleLabl.setGeometry(QtCore.QRect(110, 10, 181, 21))
        self.findmuscleLabl.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "color: rgb(37,39,51)")
        self.findmuscleLabl.setObjectName("findmuscleLabl")
        self.exampleLabel = QtWidgets.QLabel(self.MuscleDemo)
        self.exampleLabel.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.exampleLabel.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "color: rgb(37,39,51)")

        self.examplemusclelabel = QtWidgets.QLabel(self.MuscleDemo)


        self.exampleLabel.setObjectName("exampleLabel")
        self.findmuscleLabl_2 = QtWidgets.QLabel(self.MuscleDemo)
        self.findmuscleLabl_2.setGeometry(QtCore.QRect(5, 70, 371, 21))
        self.findmuscleLabl_2.setStyleSheet("font: 12pt \".AppleSystemUIFont\";\n"
                "color: rgb(37,39,51)")
                
        self.findmuscleLabl_2.setObjectName("findmuscleLabl_2")
        self.RigthSide = QtWidgets.QColumnView(self.centralwidget)
        self.RigthSide.setGeometry(QtCore.QRect(430, 0, 20, 441))
        self.RigthSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.RigthSide.setObjectName("RigthSide")
        self.leftSide = QtWidgets.QColumnView(self.centralwidget)
        self.leftSide.setGeometry(QtCore.QRect(0, 0, 20, 441))
        self.leftSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.leftSide.setObjectName("leftSide")

        self.doneButton = QtWidgets.QPushButton(self.centralwidget)
        self.doneButton.setGeometry(QtCore.QRect(330, 420, 101, 20))
        self.doneButton.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.doneButton.setObjectName("doneButton")

        self.doneButton.clicked.connect(self.test_done)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 420, 101, 20))
        self.backButton.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.backButton.setObjectName("backButton")

        self.backButton.clicked.connect(self.test_back)

        self.patientsnameFrame = QtWidgets.QFrame(self.centralwidget)
        self.patientsnameFrame.setGeometry(QtCore.QRect(90, 320, 271, 81))
        self.patientsnameFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.patientsnameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientsnameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patientsnameFrame.setObjectName("patientsnameFrame")
        self.labelPatientsName = QtWidgets.QLabel(self.patientsnameFrame)
        self.labelPatientsName.setGeometry(QtCore.QRect(15, 10, 191, 31))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.PatientsNameEnter = QtWidgets.QLineEdit(self.patientsnameFrame)
        self.PatientsNameEnter.setGeometry(QtCore.QRect(30, 40, 211, 21))
        self.PatientsNameEnter.setStyleSheet("background-color: rgb(255,252,241);\n"
                "color: rgb(115, 116, 116);\n"
                "selection-color: rgb(207, 212, 212);\n"
                "border-color: rgb(156, 160, 159);\n"
                "border-bottom-color: rgb(159, 163, 163);")
        self.examplemusclelabel.raise_()
        _translate = QtCore.QCoreApplication.translate
        self.findmuscleLabl.setText(_translate("MainWindow", "Place EMG on muscle belly"))
        self.exampleLabel.setText(_translate("MainWindow", "Example:"))

        if (listInfo == 1):
                pixmap = QPixmap('icons/measWrist.png')
                self.examplemusclelabel.setPixmap(pixmap)
                self.examplemusclelabel.resize(pixmap.width()*1.8, pixmap.height()*1.8)
                self.findmuscleLabl_2.setText(_translate("MainWindow", "Find Measurement from forearm crease to EMG Placement"))
                self.examplemusclelabel.move(70,100)
        elif (listInfo == 2):
                pixmap = QPixmap('icons/measFinger.png')
                self.examplemusclelabel.setPixmap(pixmap)
                self.findmuscleLabl_2.setText(_translate("MainWindow", "Find Measurement from forearm to EMG Placement"))
                self.examplemusclelabel.move(70,130)                
        else:
                pixmap = QPixmap('icons/measShoulder.png')
                self.examplemusclelabel.setPixmap(pixmap)
                self.findmuscleLabl_2.setText(_translate("MainWindow", "Find Measurement from armpit crease to EMG Placement"))
                self.examplemusclelabel.move(90,130)  


        self.doneButton.setText(_translate("MainWindow", "Next"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "ENTER MEASUREMENT (cm)"))

        self.findmuscleLabl.setAlignment(Qt.AlignCenter)
        self.findmuscleLabl_2.setAlignment(Qt.AlignCenter)

        self.findmuscleLabl.adjustSize()
        self.findmuscleLabl_2.adjustSize()
        self.exampleLabel.adjustSize()
        self.labelPatientsName.adjustSize()

    def test_done(self):
        print("Next to EMG data!")
        text_input = self.PatientsNameEnter.text()
        text_file = open("meas.txt", "w")
        text_file.write("%s" % text_input)
        text_file.close()
        self.close()  

    def test_back(self):
        print("back to name page!")
        self.close()       
###############################################################################################################

class Ui_SampleEMG(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(450, 493)
        self.setMaximumSize(QtCore.QSize(1280, 16777215))
        self.setStyleSheet("background-color: rgb(255,252,241)\n"
                "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.MuscleDemo = QtWidgets.QFrame(self.centralwidget)
        self.MuscleDemo.setGeometry(QtCore.QRect(20, 0, 411, 341))
        self.MuscleDemo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MuscleDemo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MuscleDemo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MuscleDemo.setObjectName("MuscleDemo")

##########################################################################################

        self.lyt = QtWidgets.QVBoxLayout()
        self.MuscleDemo.setLayout(self.lyt)
        # self.setCentralWidget(self.MuscleDemo)

        # 2. Place the matplotlib figure
        self.myFig = MyFigureCanvas(x_len=20000, y_range=[0., 0.02], interval=20)
        self.lyt.addWidget(self.myFig)

##########################################################################################

        self.exampleLabel = QtWidgets.QLabel(self.MuscleDemo)
        self.exampleLabel.setGeometry(QtCore.QRect(155, 21, 81, 21))
        self.exampleLabel.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "color: rgb(37,39,51)")
        self.exampleLabel.setObjectName("exampleLabel")
        self.RigthSide = QtWidgets.QColumnView(self.centralwidget)
        self.RigthSide.setGeometry(QtCore.QRect(430, 0, 20, 441))
        self.RigthSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.RigthSide.setObjectName("RigthSide")
        self.leftSide = QtWidgets.QColumnView(self.centralwidget)
        self.leftSide.setGeometry(QtCore.QRect(0, 0, 20, 441))
        self.leftSide.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.leftSide.setObjectName("leftSide")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(330, 420, 101, 20))
        self.nextButton.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.nextButton.setObjectName("nextButton")
        self.backBB = QtWidgets.QPushButton(self.centralwidget)
        self.backBB.setGeometry(QtCore.QRect(20, 420, 101, 20))
        self.backBB.setStyleSheet("background-color: rgb(255,252,241);border-color: rgb(34, 34, 34);\n"
                "color: rgb(37,39,51);\n"
                "border-top-color: rgb(85, 86, 86);\n"
                "selection-background-color: rgb(197, 201, 201);\n"
                "")
        self.backBB.setObjectName("backBB")
        self.patientsnameFrame = QtWidgets.QFrame(self.centralwidget)
        self.patientsnameFrame.setGeometry(QtCore.QRect(90, 350, 271, 61))
        self.patientsnameFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.patientsnameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientsnameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patientsnameFrame.setObjectName("patientsnameFrame")
        self.labelPatientsName = QtWidgets.QLabel(self.patientsnameFrame)
        self.labelPatientsName.setGeometry(QtCore.QRect(50, 10, 151, 31))
        self.labelPatientsName.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(37,39,51);")
        self.labelPatientsName.setObjectName("labelPatientsName")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 24))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.nextButton.clicked.connect(self.test_done)
        self.backBB.clicked.connect(self.test_back)

        _translate = QtCore.QCoreApplication.translate
        self.exampleLabel.setText(_translate("MainWindow", "EMG DATA:"))
        self.nextButton.setText(_translate("MainWindow", "Done"))
        self.backBB.setText(_translate("MainWindow", "Back"))
        self.labelPatientsName.setText(_translate("MainWindow", "Sample of EMG signal"))

        self.exampleLabel.adjustSize()
        self.labelPatientsName.adjustSize()

    def test_done(self):
        print("FINISHED!")
        self.close()  

    def test_back(self):
        print("back to measurement page!")
        self.close()  



class MyFigureCanvas(FigureCanvas, anim.FuncAnimation):
    '''
    This is the FigureCanvas in which the live plot is drawn.

    '''
    def __init__(self, x_len:int, y_range:List, interval:int) -> None:
        '''
        :param x_len:       The nr of data points shown in one plot.
        :param y_range:     Range on y-axis.
        :param interval:    Get a new datapoint every .. milliseconds.

        '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        # Range settings
        self._x_len_ = x_len
        self._y_range_ = y_range

        # Store two lists _x_ and _y_
        x = list(range(0, x_len))
        y = [0] * x_len
        self.temp = False
        self.temp2 = True
        # Store a figure and ax
        self._ax_  = self.figure.subplots()
        self._ax_.set_ylim(ymin=self._y_range_[0], ymax=self._y_range_[1])
        self._line_, = self._ax_.plot(x, y)
        # self.delsys = DelsysSensors(self)
        self.delsysWorker = SensorGUI()
        self.delsysWorker.startEMGThread()
        print("USE THIS ")

        # Call superclass constructors
        anim.FuncAnimation.__init__(self, self.figure, self._update_canvas_, fargs=(y,), interval=interval, blit=True)
        return

    def _update_canvas_(self, i, y) -> None:
        '''
        This function gets called regularly by the timer.

        '''
        # if self.delsysWorker.getRunning() == False:
                # sensor is not running
                # return self._line_

        emgArr = self.delsysWorker.getEMG()
        if len(emgArr) < self._x_len_:
                # at the start, pad emgArr with zeros
                y = [0] * (self._x_len_ + 1) 
                emgArr.extend(y) #emgArr will now be longer than necessary, but we will truncate it later

        if len(emgArr) > self._x_len_:
                # if self.temp == False:
                #         print("updating")
                #         self.temp == True
                # # y.append(emgArr[len(emgArr) - 1])        
                # y = y[-self._x_len_:]                        # Truncate list _y_
                try:
                        self._line_.set_ydata(emgArr[0:self._x_len_]) #new
                        self._y_range = [min(emgArr), max(emgArr)]
                        self._ax_.set_ylim(ymin=min(emgArr), ymax=max(emgArr))
                except:
                        print("we got an error")
        # else:

                
        return self._line_,


# # Data source
# # ------------
# n = np.linspace(0, 499, 500)
# d = 50 + 25 * (np.sin(n / 8.3)) + 10 * (np.sin(n / 7.5)) - 5 * (np.sin(n / 1.5))
# i = 0

# def get_next_datapoint():
#     global i
#     i += 1
#     if i > 499:
#         i = 0
#     return d[i]

###############################################################################################################

# class Worker(QObject):
#         def __init__(self):
#                 # self._sensors = sensors
#                 self.running = pyqtSignal()
#                 self.data = pyqtSignal(array)
#                 self.finished = pyqtSignal()
        
#         def setupConnection(self):
#                 self.sensors = DelsysSensors()
        
#         def startEMG(self):
#                 self.sensors.streamEMGData()
        
#         def stopEMG(self):
#                 self.sensors.stopReading() #TODO: implement this
        
#         def getSensorData(self):
#                 self.data.emit(self.sensors.emg_data)

                
                

