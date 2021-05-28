
########################################################################################################################################
# This file:
# - has all of the functions for getting delsys functions
# 
# Team 4
# Date Modified: 27/05/2021
# Author: Joshua Rolls
## Some code adapted from Sami Keabab, UQ student ##
########################################################################################################################################



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
    '''
    This is the class in which direct interaction with the sensor is handled.
    Attributes and methods in this class should only be handled within the EMG thread

    '''
    runningSig = pyqtSignal(bool) # signal to show if measurements are being taken
    dataSig = pyqtSignal(float) # signal to send EMG data between threads
    def __init__(self, master, parent=None):
        '''
        :param master - parent class
        
        '''
        QObject.__init__(self,parent)
        print('delsyssensor class')
        self.master = master
        self.EMG_DATA_PORT_LENGTH = 16
        self.EMG_SEG_LEN = self.EMG_DATA_PORT_LENGTH * 4

        self.maxContract = 0
        self.timeouts = 0
        
        
        self.streamOn = False


        self.initTrignoConnection()
        print('inited')
        self.getSensorsActive()
        print('^^sensors')
        self.initTriggers()
        
        

    def initTrignoConnection(self):
            '''
            Initiates TCP connection with Trigno Control Program
            :requires Delsys Sensor Control Box needs to be connected
                        and Trigno Control Utility open before use

            '''
            #initiate command port
            host = socket.gethostname()
            # create command socket and consume the servers initial response
            try:
                self.trigno_cmd_port = socket.create_connection((host,50040),10)
                print(self.trigno_cmd_port.recv(1024).decode('ascii'))
                self.trigno_imu_data_port = socket.create_connection((host, 50044),0.5)
                self.trigno_emg_data_port = socket.create_connection((host, 50043),0.5)
                # set connection to master if not already
                self.send_delsys_cmd("MASTER")
                
            except:
                messagebox.showerror("TCP Error","Could not establish connection with Trigno base.\nMake sure \"Trigno Control Utility\" is open and run the program again.")
                exit()



    def send_delsys_cmd(self,cmd):
        '''
        Sends commands to Delsys sensors via TCP and waits for response
        Inputs: cmd: the command to send to sensors (string)
        Returns: the response received from the sensor

        '''
        self.trigno_cmd_port.send(bytes("{}{}".format(cmd,'\r\n\r\n'),encoding = 'ascii'))
        resp = self.trigno_cmd_port.recv(1040)
        print(resp.decode('ascii'))
        return(resp.decode('ascii'))

    def read_EMG(self,t0,trgd): 
        '''
        Reads one frame of EMG data
        Inputs: t0: the start time
                trgd: indicates whether data has started being received or not
        Returns: Array of length (self.EMG_SEG_LEN + 1), where the first self.EMG_SEG_LEN
                    values represent measurements from each sensor, and the last value
                    represents sample time

        '''
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
        '''
        Receives data from sensors and emits it to self.dataSig
        Currently only handles one sensor maximum

        '''
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
            
            # Try and get the next frame
            frame = self.read_EMG(t0, triggered)
            if frame[0] == None:
                self.timeouts += 1
                if self.timeouts > 100:
                    # we've had 100 timeouts in a row, this is a problem
                    print("100 consecutive timeouts - stopping streaming")
                    return -1
                continue

            # We received data, extract the right emg value for our sensor            
            emgValue = frame[sensorIndex]

            #check if data was received ie trig start pressed
            if emgValue != None:
                triggered = True
                self.emg_data = np.append(self.emg_data,frame)
                self._data.append(emgValue)
                samples = samples + 1
                
                
                if samples % 2:
                    self.dataSig.emit(emgValue) #Emit signal to GUI



            # if no data received and trig start was pressed ie trig stop was pressed
            elif triggered:
                
                break

            self.emg_data = self.emg_data.reshape(int(len(self.emg_data)/(self.EMG_DATA_PORT_LENGTH+1)),(self.EMG_DATA_PORT_LENGTH+1))


    
    def getEMGData(self):
        '''
        OBSOLETE: gets one EMG frame and returns the maximum value (which will be the value from our sensor)
        Returns: one EMG value

        '''
        self.emg_data = np.array([],ndmin = 2)
        t0 = time.time()
        triggered = False
        samples = 0
        
        # Try and get the next frame
        frame = self.read_EMG(t0, triggered)
        #check if data was received ie trig start pressed
        if frame[0] != None:
            triggered = True
            self.emg_data = np.append(self.emg_data,frame)
            samples = samples + 1

        # if no data received and trig start was pressed ie trig stop was pressed
        elif triggered: 
            return None

        self.emg_data = self.emg_data.reshape(int(len(self.emg_data)/(self.EMG_DATA_PORT_LENGTH+1)),(self.EMG_DATA_PORT_LENGTH+1))

        maxContract = 0
        if samples > 0 and abs(frame[0:16]).max() > maxContract:
            maxContract = abs(frame[0:16]).max()

        print(maxContract)
        return maxContract


    def getSensorsActive(self):
        '''
        A function to check which sensors are active
        Sensor status is stored in self.sensor_active_list

        '''
        self.sensor_active_list = []
        for s in range(16):
            cmd = "SENSOR {} ACTIVE?".format(s+1)
            resp = self.send_delsys_cmd(cmd)
            if "YES" in resp:
                self.sensor_active_list.append(True)
            else:
                self.sensor_active_list.append(False)
        print(self.sensor_active_list)  



    """Delsys Commands"""
    def initTriggers(self):
        '''
        Initiates Delsys triggers to off

        '''
        self.send_delsys_cmd("TRIGGER START OFF")
        self.send_delsys_cmd("TRIGGER STOP OFF")

    def sendSTART(self):
        '''
        Sends a START command to the delsys sensors

        '''
        # checks if trigger is activated, sends start
        self.send_delsys_cmd("TRIGGER?")
        self.send_delsys_cmd("START")
        
    def sendSTOP(self):
        '''
        Sends a STOP command to the delsys sensors
        
        '''
        cmd =  "STOP"
        self.send_delsys_cmd(cmd)   
    
    def sendQUIT(self):
        '''
        Sends a QUIT command to the delsys sensors
        
        '''
        self.send_delsys_cmd("QUIT")   

    

    """Commands received from GUI thread"""
    def receiveStart(self):
        '''
        Responds to a start signal received from GUI thread

        '''
        self.sendSTART()
        if self.streamOn == True:
            print("already running")
            # don't do anything else
        else:
            self.streamOn = True
            self.streamEMGData()

    def receiveStop(self):
        '''
        Responds to a start signal received from GUI thread

        '''
        self.sendSTOP()
        self.streamOn = False
    
    def receiveQuit(self):
        '''
        Responds to a quit signal received from GUI thread

        '''
        self.sendSTOP()
        self.sendQUIT()
        print("quitting")
        self.trigno_emg_data_port.close()
        self.trigno_cmd_port.close()
        self.trigno_imu_data_port.close()
        
        


################################################################
# The following classes are accessible to the GUI. Nothing above 
# this line should be accessed by GUI thread, 
# otherwise we'll have problems
################################################################


class SensorGUI(QObject):
    '''
    A class to handle interactions between the GUI and the EMG threads
    '''
    def __init__(self, parent=None):
        '''
        Initialises the QObject, and clears variables

        '''
        QObject.__init__(self,parent)
        self.isRunning = False
        self.max = None
        self.emgLatest = []
        self.counter = 0

    def startEMGThread(self):
        '''
        Starts the EMG thread. Should be called directly from GUI.

        '''

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

        
    
    """ Setting functions - slots for signals from delsys thread """
    def setRunning(self, val):
        '''
        Sets the isRunning variable
        Input: bool (True for running, False for not)
        '''
        self.isRunning = val

    def setMax(self):
        '''
        Sets the maximum contraction value by taking the maximum absolute value of the EMG array

        '''
        self.max = max(list(map(abs, self.emgLatest)))

    def setEMG(self, val):
        '''
        Sets the EMG array. Called inside the GUI thread whenever dataSig has been emitted from the EMG thread
        Trims the array to only keep the most recent 20-25k values

        Inputs: raw EMG value (integer)

        '''
        self.emgLatest.append(val)
        self.counter += 1
        if len(self.emgLatest) > 25000:
            # every 50 samples, we delete 50 samples
            # this way the array doesn't get too big
            # might play around with this number though
            if self.counter < 202:
                print("truncating")
            
            self.emgLatest = self.emgLatest[50:]
            # array thus varies in length between 20k and 25k values
        
        self.setMax() # replace this with some sophistry later

    def clearEMG(self):
        '''
        Clears the EMG array stored by the GUI thread
        (eg when starting a measurement or clicking redo)

        '''
        self.emgLatest = []


    '''Getting functions - called from GUI directly'''
    def getRunning(self):
        '''
        Returns state of the EMG sensors (True if Running, False if not)

        '''
        return self.isRunning

    def getEMG(self):
        '''
        Returns the current EMG array

        '''
        return self.emgLatest

    def getMax(self):
        '''
        Returns the MVC

        '''
        return self.max
    



class CommandsGUI(QObject):
    '''
    Handles commands sent from the GUI thread to the EMG thread

    '''
    guiStart = pyqtSignal()
    guiStop = pyqtSignal()
    guiQuit = pyqtSignal()
    def __init__(self, parent=None):
        '''
        Input: parent SensorGUI object

        '''
        QObject.__init__(self,parent)
        self.master = parent

    def guiSendStart(self):
        '''
        Sends a start command from the gui to the emg thread

        '''
        self.master.clearEMG()

        # don't need to do anything else since emg is running by default

        print("sending start from gui to emg")

    def guiSendStop(self):
        '''
        Sends a stop command from the gui to the emg thread

        '''
        self.guiStop.emit()


    def guiSendQuit(self):
        '''
        Sends a Quit command from the gui to the emg thread

        '''
        self.guiQuit.emit()



        




if "__name__"=="__main__":
    print("delsys_func.py\n")
    sensor = DelsysSensors()
    print("exiting")
