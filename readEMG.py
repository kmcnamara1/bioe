#########
# Code to read raw EMG data and save it to a file
########

import sys
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from delsys_func import *
from tkinter import *
from tkinter import messagebox
# from UI.mainFile import *


class Main():
    def __init__(self,master):
        
        print('hello?')
        print("hELLO??")
        
        

        # self.sensors = DelsysSensors(self)
        # self.startThread()
        # self.sensors.streamEMGData()
        # while True:
            # self.sensors.getEMGData()
        # self.master = master
        # self.maxContract = 0
        
        # initTrignoConnection(self)


        # getSensorsActive(self)

        # streamEMGData(self)


class LilWidget(QMainWindow):
    def startThread(self):
        self.sensors = DelsysSensors(self)
        self.qThread = QThread(self)
        self.sensors.runningSig.connect(self.printRunning)
        self.sensors.moveToThread(self.qThread)
        self.qThread.started.connect(self.sensors.streamEMGData)
        self.qThread.start()
    
    def printRunning(self, val):
        print(val)

        
def guiCallback(self, value):
    print(value)

# def main():
#     print("main")
#     sensors = DelsysSensors()
#     while(True):
#         #sleep
#         # Not Reached
#          continue



        

# def Main():
#     initTrignoConnection()
    
#     getSensorsActive()

#     streamEMGData


if __name__ == "__main__":
    # print("readEMG.py\n")
    # root = Tk()
    # app = Main(root)
    # root.mainloop()


    app = QApplication(sys.argv)
    w = LilWidget()
    w.show()
    w.startThread()

    sys.exit(app.exec_())
    
    # main()




# ###############
# frame is a 1x17 array. First 16 elements represent EMG channels, 17th is the sample no
# only one of the first 16 elements will be useful (as only one channel at a time)




