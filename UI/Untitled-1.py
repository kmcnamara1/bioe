
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OverviewWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("background-color: rgb(255,252,241)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SideColum_2 = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum_2.setGeometry(QtCore.QRect(1261, 0, 20, 741))
        self.SideColum_2.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum_2.setObjectName("SideColum_2")
        self.WelcomeFrame = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame.setGeometry(QtCore.QRect(400, 100, 491, 151))
        self.WelcomeFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WelcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame.setObjectName("WelcomeFrame")
        self.label_3 = QtWidgets.QLabel(self.WelcomeFrame)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 231, 111))
        self.label_3.setStyleSheet("font: 48pt \".AppleSystemUIFont\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(37,39,51);")
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
        self.startButton.clicked.connect(self.txtstate)
        
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
	       
###############################################################################################################
     
        self.label = QtWidgets.QLabel(self.LoginFrame)
        self.label.setGeometry(QtCore.QRect(190, 10, 71, 21))
        self.label.setStyleSheet("font: 18pt \".AppleSystemUIFont\";\n"
"color: rgb(37,39,51)")
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
        self.extButton.clicked.connect(self.exitUI)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi_1(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##################################################################################
    def exitUI(self):
        sys.exit(app.exec_())

    def txtstate(self):
        text_input = self.lineEdit.text()
        print(text_input)
##################################################################################
    def retranslateUi_1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "WELCOME"))
        self.startButton.setText(_translate("MainWindow", "ENTER"))
        self.label.setText(_translate("MainWindow", "LOGIN: "))
        self.label_2.setText(_translate("MainWindow", "NAME:"))
        self.extButton.setText(_translate("MainWindow", "EXIT"))

class Ui_OverviewWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("background-color: rgb(255,252,241)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(890, 170, 141, 71))
        self.startButton.setStyleSheet("background-color: rgb(111, 207, 151);border-color: rgb(34, 34, 34);")
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(1050, 170, 141, 71))
        self.stopButton.setStyleSheet("background-color: rgb(235,87,87)")
        self.stopButton.setObjectName("stopButton")
        self.changeExerciseButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeExerciseButton.setGeometry(QtCore.QRect(890, 280, 141, 71))
        self.changeExerciseButton.setStyleSheet("background-color: rgb(242, 201, 76)")
        self.changeExerciseButton.setObjectName("changeExerciseButton")
        self.ExportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportDataButton.setGeometry(QtCore.QRect(1050, 280, 141, 71))
        self.ExportDataButton.setStyleSheet("background-color: rgb(242,153,74)")
        self.ExportDataButton.setObjectName("ExportDataButton")
        self.SideColum = QtWidgets.QColumnView(self.centralwidget)
        self.SideColum.setGeometry(QtCore.QRect(10, 0, 201, 741))
        self.SideColum.setStyleSheet("background-color: rgb(78, 78, 78)")
        self.SideColum.setObjectName("SideColum")
        self.overviewSide = QtWidgets.QPushButton(self.centralwidget)
        self.overviewSide.setGeometry(QtCore.QRect(10, 90, 201, 41))
        self.overviewSide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
";")
        self.overviewSide.setObjectName("overviewSide")
        self.historySide = QtWidgets.QPushButton(self.centralwidget)
        self.historySide.setGeometry(QtCore.QRect(10, 130, 201, 41))
        self.historySide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
";")
        self.historySide.setObjectName("historySide")
        self.goalSide = QtWidgets.QPushButton(self.centralwidget)
        self.goalSide.setGeometry(QtCore.QRect(10, 170, 201, 41))
        self.goalSide.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
";")
        self.goalSide.setObjectName("goalSide")
        self.patientSetup = QtWidgets.QPushButton(self.centralwidget)
        self.patientSetup.setGeometry(QtCore.QRect(10, 210, 201, 41))
        self.patientSetup.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
";")
        self.patientSetup.setObjectName("patientSetup")
        self.Logout = QtWidgets.QPushButton(self.centralwidget)
        self.Logout.setGeometry(QtCore.QRect(10, 680, 201, 41))
        self.Logout.setStyleSheet("background-color: rgb(78,78,78); color: white\n"
";\n"
"border-color: rgb(34, 34, 34);")
        self.Logout.setObjectName("Logout")
        self.changePatient = QtWidgets.QPushButton(self.centralwidget)
        self.changePatient.setGeometry(QtCore.QRect(10, 630, 201, 41))
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
        self.label_3.setGeometry(QtCore.QRect(170, 10, 101, 41))
        self.label_3.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
"background-color: rgb(255, 255, 255);\n"
"color: #7f7f7f")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.WelcomeFrame)
        self.label_4.setGeometry(QtCore.QRect(140, 40, 171, 41))
        self.label_4.setStyleSheet("font: 24pt \".AppleSystemUIFont\"; \n"
"background-color: rgb(255, 255, 255);\n"
"color:#323232")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 10, 171, 31))
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
        self.label_6.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.label_6.setStyleSheet("font: 14pt \".AppleSystemUIFont\"; \n"
"background-color: rgb(255, 255, 255);\n"
"color: #7f7f7f")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.WelcomeFrame_2)
        self.label_7.setGeometry(QtCore.QRect(50, 40, 101, 41))
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
        self.label_8.setGeometry(QtCore.QRect(90, 10, 31, 31))
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
        self.label_10.setGeometry(QtCore.QRect(820, 10, 231, 31))
        self.label_10.setStyleSheet("font: 18pt \".AppleSystemUIFont\"; \n"
"background-color: rgb(255, 255, 255);\n"
"color: #7f7f7f")
        self.label_10.setObjectName("label_10")
        self.WelcomeFrame_5 = QtWidgets.QFrame(self.centralwidget)
        self.WelcomeFrame_5.setGeometry(QtCore.QRect(10, 0, 201, 91))
        self.WelcomeFrame_5.setStyleSheet("background-color: rgba(106, 108, 108, 157); color: white;\n"
"")
        self.WelcomeFrame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WelcomeFrame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeFrame_5.setObjectName("WelcomeFrame_5")
        self.label_13 = QtWidgets.QLabel(self.WelcomeFrame_5)
        self.label_13.setGeometry(QtCore.QRect(70, 10, 51, 31))
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.WelcomeFrame_5)
        self.label_14.setGeometry(QtCore.QRect(60, 40, 71, 31))
        self.label_14.setStyleSheet("font: 13pt \".AppleSystemUIFont\";")
        self.label_14.setObjectName("label_14")
        self.startButton.raise_()
        self.stopButton.raise_()
        self.changeExerciseButton.raise_()
        self.ExportDataButton.raise_()
        self.SideColum.raise_()
        self.overviewSide.raise_()
        self.historySide.raise_()
        self.goalSide.raise_()
        self.patientSetup.raise_()
        self.Logout.raise_()
        self.changePatient.raise_()
        self.WelcomeFrame.raise_()
        self.WelcomeFrame_2.raise_()
        self.WelcomeFrame_3.raise_()
        self.WelcomeFrame_4.raise_()
        self.label_5.raise_()
        self.WelcomeFrame_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi_2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi_2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.changeExerciseButton.setText(_translate("MainWindow", "Change Exercise"))
        self.ExportDataButton.setText(_translate("MainWindow", "Export Data"))
        self.overviewSide.setText(_translate("MainWindow", "Overview"))
        self.historySide.setText(_translate("MainWindow", "History"))
        self.goalSide.setText(_translate("MainWindow", "Goal"))
        self.patientSetup.setText(_translate("MainWindow", "Patient Setup"))
        self.Logout.setText(_translate("MainWindow", "Logout"))
        self.changePatient.setText(_translate("MainWindow", "Change Patient"))
        self.label_3.setText(_translate("MainWindow", "ACTIVITY"))
        self.label_4.setText(_translate("MainWindow", "Wrist Extension"))
        self.label_5.setText(_translate("MainWindow", "Session no. "))
        self.label_6.setText(_translate("MainWindow", "MVC"))
        self.label_7.setText(_translate("MainWindow", "---.--mV"))
        self.label_8.setText(_translate("MainWindow", "REP"))
        self.label_9.setText(_translate("MainWindow", "-/3"))
        self.label_10.setText(_translate("MainWindow", "Paitent: Jone Swith"))
        self.label_13.setText(_translate("MainWindow", "Clinician"))
        self.label_14.setText(_translate("MainWindow", "Pippa Pepo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OverviewWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
