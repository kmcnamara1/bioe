#########
# Code to read raw EMG data and save it to a file
########

from delsys_func import *
from tkinter import *
from tkinter import messagebox

class Main():
    def __init__(self,master):
        
        
        self.master = master
        self.maxContract = 0
        
        initTrignoConnection(self)


        self.getSensorsActive()

        self.streamEMGData()

        
        


        

# def Main():
#     initTrignoConnection()
    
#     getSensorsActive()

#     streamEMGData


if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()








