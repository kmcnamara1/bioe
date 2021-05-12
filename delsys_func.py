###############################
## Code from Sami, UQ student##
###############################

import socket
import struct
from tkinter import messagebox

# self.EMG_DATA_PORT_LENGTH = 16
# self.EMG_SEG_LEN = self.EMG_DATA_PORT_LENGTH * 4

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
         
            return(np.array([None]))
        
        data = np.asarray(struct.unpack('<'+'f'*self.EMG_DATA_PORT_LENGTH, packet))
        t = time.time() - t0
        data = np.append(data,t)
        return(data)


def streamEMGData(self):
        self.emg_data = np.array([],ndmin = 2)
        t0 = time.time()
        triggered = False
        while True:
            # Try and get the next frame
            frame = self.read_EMG(t0, triggered)
            #check if data was received ie trig start pressed
            if frame[0] != None:
                triggered = True
                self.emg_data = np.append(self.emg_data,frame)

            # if no data received and trig start was pressed ie trig stop was pressed
            elif triggered:
                
                break

            self.emg_data = self.emg_data.reshape(int(len(self.emg_data)/(self.EMG_DATA_PORT_LENGTH+1)),(self.EMG_DATA_PORT_LENGTH+1))
            print(self.emg_data)
            if max(self.emg_data) > self.maxContract:
                self.maxContract = self.emg_data
                print("MAX CONTRACTION VALUE %0000d", self.maxContract )


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
