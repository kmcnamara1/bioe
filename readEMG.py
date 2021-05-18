#########
# Code to read raw EMG data and save it to a file
########

from delsys_func import *
from tkinter import *
from tkinter import messagebox
from UI.mainFile import *


class Main():
    def __init__(self,master):
        
        print('hello?')
        print("hELLO??")
        self.sensors = DelsysSensors(self)
        while True:
            self.sensors.getEMGData()
        # self.master = master
        # self.maxContract = 0
        
        # initTrignoConnection(self)


        # getSensorsActive(self)

        # streamEMGData(self)

        
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
    w = MainWindow()

    sys.exit(app.exec_())
    
    # main()




# ###############
# frame is a 1x17 array. First 16 elements represent EMG channels, 17th is the sample no
# only one of the first 16 elements will be useful (as only one channel at a time)




