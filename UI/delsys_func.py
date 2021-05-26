#####################################
## Code from Sami Keabab, UQ student ##
#####################################

import socket
import struct
from tkinter import messagebox
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import numpy as np
import time


#############################################################
# Local functions (should not access outside this file)
# Global functions (accessible by GUI) are at the end of the file
#############################################################

class DelsysSensors(QObject):
    runningSig = pyqtSignal(bool)
    dataSig = pyqtSignal(float)
    def __init__(self, master, parent=None):
        # super(DelsysSensors, self).__init__(parent)
        QObject.__init__(self,parent)
        print('delsyssensor class')
        self.master = master
        self.EMG_DATA_PORT_LENGTH = 16
        self.EMG_SEG_LEN = self.EMG_DATA_PORT_LENGTH * 4

        self.maxContract = 0
        self.timeouts = 0
        #add signals
        # self.runningSig = pyqtSignal()
        # self.dataSig = pyqtSignal(np.array)
        # self.finishedSig = pyqtSignal()

        self.streamOn = False


        self.initTrignoConnection()
        print('inited')
        self.getSensorsActive()
        print('^^sensors')
        self.initTriggers()
        # self.sendSTART()
        # print("sentStart")
        # self.streamEMGData()
        # print('not reached?')

    def initTrignoConnection(self):
            #initiate command port
            host = socket.gethostname()
            # create command socket and consume the servers initial response
            try:
                self.trigno_cmd_port = socket.create_connection((host,50040),10)
                print(self.trigno_cmd_port.recv(1024).decode('ascii'))
                self.trigno_imu_data_port = socket.create_connection((host, 50044),0.5)
                self.trigno_emg_data_port = socket.create_connection((host, 50043),0.5)

                
            except:
                messagebox.showerror("TCP Error","Could not establish connection with Trigno base.\nMake sure \"Trigno Control Utility\" is open and run the program again.")
                self.master.destroy()
                exit()





    def send_delsys_cmd(self,cmd):
            self.trigno_cmd_port.send(bytes("{}{}".format(cmd,'\r\n\r\n'),encoding = 'ascii'))
            resp = self.trigno_cmd_port.recv(1040)
            print(resp.decode('ascii'))
            return(resp.decode('ascii'))

    def read_EMG(self,t0,trgd): 
            try:
                packet = self.trigno_emg_data_port.recv(self.EMG_SEG_LEN)
                if not trgd:
                    trgd = True
            except socket.timeout:
                print('timeout\n\n')
                return(np.array([None]))
            
            data = np.asarray(struct.unpack('<'+'f'*self.EMG_DATA_PORT_LENGTH, packet))
            t = time.time() - t0
            data = np.append(data,t)
            return(data)


    def streamEMGData(self):
        self.emg_data = np.array([],ndmin = 2)
        self._data = []
        t0 = time.time()
        triggered = False
        samples = 0
        self.runningSig.emit(True)
        print("delsys runningsig True")
        
        # check which sensors to look at
        sensorsActiveIndex = [i for i,x in enumerate(self.sensor_active_list) if x]
        sensorIndex = sensorsActiveIndex[0] #we only care about the first sensor available


        while self.streamOn == True:
            # if samples > 100 and samples < 105:
                # stop after 100 samples
                # self.sendSTOP
                # print("delsys emmited false")
                # self.runningSig.emit(False)

            # Try and get the next frame
            frame = self.read_EMG(t0, triggered)
            if frame[0] == None:
                self.timeouts += 1
                if self.timeouts > 100:
                    # we've had 100 timeouts in a row, this is a problem
                    print("100 consecutive timeouts, let's return an error")
                    return -1
                continue

            if samples > 15000 and samples < 15005:
                print(frame)
                print("sensorIndex: {}".format(sensorIndex))

            # We received data, extract the right emg value for our sensor
            emgValue = frame[sensorIndex]

            #check if data was received ie trig start pressed
            if emgValue != None:
                triggered = True
                self.emg_data = np.append(self.emg_data,frame)
                self._data.append(emgValue)#this is what we'll use
                samples = samples + 1
                # if samples > 20000:
                #     emgFile = open("emgDatatest.txt", 'w')
                #     for row in self._data:
                #         np.savetxt(emgFile,row)

                # if abs(emgValue) > 0:
                    # print("emgValue is {}".format(emgValue))
                self.dataSig.emit(emgValue) ### THIS IS WHAT WE CARE ABOUT



            # if no data received and trig start was pressed ie trig stop was pressed
            elif triggered:
                
                break

            self.emg_data = self.emg_data.reshape(int(len(self.emg_data)/(self.EMG_DATA_PORT_LENGTH+1)),(self.EMG_DATA_PORT_LENGTH+1))
            # print(self.emg_data)
            if samples > 0 and abs(frame[0:16]).max() > self.maxContract:
                self.maxContract = abs(frame[0:16]).max()
                print("MAX CONTRACTION VALUE {}".format(self.maxContract) )





    
    def getEMGData(self):
        self.emg_data = np.array([],ndmin = 2)
        t0 = time.time()
        triggered = False
        samples = 0
        # if samples > 100:
            # stop after 100 samples
            # self.sendSTOP

        # Try and get the next frame
        frame = self.read_EMG(t0, triggered)
        #check if data was received ie trig start pressed
        if frame[0] != None:
            triggered = True
            self.emg_data = np.append(self.emg_data,frame)
            samples = samples + 1

        # if no data received and trig start was pressed ie trig stop was pressed
        elif triggered: 
            return # TODO: Return a value that can be distinguished as an error (triggered thus no values returned) 

        self.emg_data = self.emg_data.reshape(int(len(self.emg_data)/(self.EMG_DATA_PORT_LENGTH+1)),(self.EMG_DATA_PORT_LENGTH+1))
        # print(self.emg_data)
        maxContract = 0
        if samples > 0 and abs(frame[0:16]).max() > maxContract:
            maxContract = abs(frame[0:16]).max()
            # print("MAX CONTRACTION VALUE {}".format(self.maxContract) )

        print(maxContract)
        return maxContract


    def getSensorsActive(self):
            # A function to check which sensor are active
            # used to determine which sensor checkbox and data to display
            self.sensor_active_list = []
            for s in range(16):
                cmd = "SENSOR {} ACTIVE?".format(s+1)
                resp = self.send_delsys_cmd(cmd)
                if "YES" in resp:
                    self.sensor_active_list.append(True)
                else:
                    self.sensor_active_list.append(False)
            print(self.sensor_active_list)  

    ### Delsys Commands
    def initTriggers(self):
        self.send_delsys_cmd("TRIGGER START OFF")
        self.send_delsys_cmd("TRIGGER STOP OFF")

    def sendSTART(self):
        # checks if trigger is activated, sends start
        self.send_delsys_cmd("TRIGGER?")
        self.send_delsys_cmd("START")
        
    def sendSTOP(self):
        cmd =  "STOP"
        self.send_delsys_cmd(cmd)   
    
    def sendQUIT(self):
        self.send_delsys_cmd("QUIT")   

    # Commands received from GUI thread
    def receiveStart(self):
        self.sendSTART()
        if self.streamOn == True:
            print("already running")
            # don't do anything else
        else:
            self.streamOn = True
            self.streamEMGData()

    def receiveStop(self):
        self.sendSTOP()
        self.streamOn = False
    
    def receiveQuit(self):
        self.sendSTOP()
        self.sendQUIT()
        # TODO: figure out how to handle quitting properly
        

        


# def emgThread(callbackFunction):
#     delsys = DelsysSensors()
#     delsys.runningSig.connect(callbackFunction)
#     delsys.streamEMGData()


################################################################
# The following classes are accessible to the GUI. Nothing above 
# this line should be accessed by GUI thread, 
# otherwise we'll have problems
################################################################


class SensorGUI(QObject):
    
    def __init__(self, parent=None):
        QObject.__init__(self,parent)
        self.isRunning = False
        self.max = None
        self.emgLatest = []
        self.counter = 0

    def startEMGThread(self):
        # should be called by GUI itself

        self.sensors = DelsysSensors(self)
        self.qThread = QThread(self)

        # init signals coming from EMG to GUI
        self.sensors.runningSig.connect(self.setRunning)
        self.sensors.dataSig.connect(self.setEMG)

        # init signals going from GUI to EMG
        self.commands = CommandsGUI(self)
        self.commands.guiStart.connect(self.sensors.receiveStart)
        self.commands.guiStop.connect(self.sensors.receiveStop)
        self.commands.guiQuit.connect(self.sensors.receiveQuit)

        self.sensors.moveToThread(self.qThread)
        self.qThread.started.connect(self.sensors.receiveStart)
        print("starting EMG thread") 
        self.qThread.start()

        
    
    ### Setting functions - slots for signals from delsys thread ###
    def setRunning(self, val):
        self.isRunning = val

    def setMax(self):
        # self.max = max(self.emgLatest)
        self.max = 1

    def setEMG(self, val):
        self.emgLatest.append(val)
        self.counter += 1
        if len(self.emgLatest) > 25000:
            # every 50 samples, we delete 50 samples
            # this way the array doesn't get too big
            # might play around with this number though
            if self.counter < 202:
                print("truncating")
            self.emgLatest = self.emgLatest[50:]
            # array thus varies in length between 200 and 250
        
        self.setMax() # replace this with some sophistry later

    def clearEMG(self):
        # clears stored EMG array (eg when starting a measurement)
        self.emgLatest = []

    ### Getting functions - called from GUI directly #####
    def getRunning(self):
        return self.isRunning

    def getEMG(self):
        return self.emgLatest

    def getMax(self):
        return self.max
    



class CommandsGUI(QObject):
    guiStart = pyqtSignal()
    guiStop = pyqtSignal()
    guiQuit = pyqtSignal()
    def __init__(self, parent=None):
        QObject.__init__(self,parent)
        self.master = parent

    def guiSendStart(self):
        self.master.clearEMG()
        # self.guiStart.emit()
        print("sending start from gui to emg")
    def guiSendStop(self):
        self.guiStop.emit()
    def guiSendQuit(self):
        # when do we call this?
        self.guiQuit.emit()



        




if "__name__"=="__main__":
    print("delsys_func.py\n")
    sensor = DelsysSensors()
    print("exiting")
