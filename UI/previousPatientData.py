import sys
import re
import os


def getNumSessions(ID):
    #get list of all files in inital directory
    list_of_files = os.listdir('./Patient Details/{}/'.format(ID))
    return len(list_of_files)

def getSetupMeasurement(sessionNum,ID):
    #row 5 if counting from 1
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[5]
    return(''.join(char for char in line if char.isdigit()))

def getPreviousWrist(sessionNum,ID):
    #row 8 if counting from 1
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[8]
    return(''.join(char for char in line if char.isdigit()))

    
def getPreviousShoulder(sessionNum,ID):
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[10]
    return(''.join(char for char in line if char.isdigit()))    

def getPreviousFinger(sessionNum,ID):
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[8]
    return(''.join(char for char in line if char.isdigit()))   

def getPatientID(name):
    name_list = name.split() 

    initials = ""

    for split_name in name_list:  # go through each name
        initials += split_name[0].upper()  # append the initial    

    return initials

# We assume the patient name is split with a space 
def checkPatientDetails(name):
    
    patientID = getPatientID(name)
    return(checkReturningPatient(patientID)) # return 1 if is reoccuring
                                             # return 0 if new

#trys to open a file with the users ID
# IF: can open --> previous patient must exist
# ELSE: must be a new patient 
def checkReturningPatient(initials):
    file_path = ("Patient Details/{}/{}1.txt".format(initials,initials))

    if not os.path.exists(file_path):
        return 0
    else: 
        return 1


# returns a string that can be used as a label for the patient history
def displayPatientHistory(PatientID,sessionNum, exported):

    #we are assuming that the we haven't exported the current data
    if (exported == None):
        print('nothing to view')
        return 0
    else:
        if (sessionNum > 1):
            sessionNum = (sessionNum - 1)
 
    # numLines = 11*sessionNum
    contents = []

    if (sessionNum == 1):
        text_file = open('./Patient Details/{}/{}{}.txt'.format(PatientID,PatientID,sessionNum), "r+")
        content = text_file.readlines()
        line = content[:10]
        contents = " ".join(line)
        return(contents)    
        # print(contents) 
    else:
        for session in range(1, sessionNum):
            text_file = open('./Patient Details/{}/{}{}.txt'.format(PatientID,PatientID,sessionNum), "r+")
            content = text_file.readlines()
            line = content[:10]      
            contents = " ".join(line)  
            print(contents)
            return(contents)   
            
