import sys
import re
import os

WRIST_LINE = 8
FINGER_LINE = 9 
SHOULDER_LINE = 10

def getNumSessions(ID):
    #get list of all files in inital directory
    list_of_files = os.listdir('Patient Details/{}/'.format(ID))
    return len(list_of_files)

def getSetupMeasurement(sessionNum,ID,ur):
    #row 5 if counting from 1
    text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,sessionNum), "r+")
    content = text_file.readlines()
    values = []
    for i in range(5,8):
        line = content[i]  
        line = ''.join(char for char in line if char.isdigit()) 
        print(line)
        val = "".join(re.findall('\d*\.?\d+',line))
        values.append("{}".format(val))     
    return(values)

    # return(''.join(char for char in line if char.isdigit()))


def getPreviousWrist(sessionNum,ID,ur):
    #row 8 if counting from 1

    if (sessionNum ==1):
        text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,sessionNum), "r+")
        content = text_file.readlines()
        line = content[WRIST_LINE]
        return(''.join(char for char in line if char.isdigit()))
    else:
        values = []
        for session in range(1,sessionNum+1):
            print(session)
            text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,session), "r+")
            content = text_file.readlines()
            line = content[WRIST_LINE]   
            line = "".join(line)
            val = "".join(re.findall('\d*\.?\d+',line))

            text_file.close()

            values.append("{}".format(val))

        return(values)    


    
def getPreviousShoulder(sessionNum,ID,ur):

    if (sessionNum ==1):
        text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,sessionNum), "r+")
        content = text_file.readlines()
        line = content[SHOULDER_LINE]
        return(''.join(char for char in line if char.isdigit()))
    else:
        values = []
        for session in range(1,sessionNum+1):
            text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,session), "r+")
            content = text_file.readlines()
            line = content[SHOULDER_LINE]   
            line = "".join(line)
            val = "".join(re.findall('\d*\.?\d+',line))

            # val = ''.join(char for char in line if char.isdigit())
            text_file.close()

            values.append("{}".format(val))
    
        return(values)   


def getPreviousFinger(sessionNum,ID,ur):

    if (sessionNum ==1):
        text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,sessionNum), "r+")
        content = text_file.readlines()
        line = content[FINGER_LINE]
        return(''.join(char for char in line if char.isdigit()))
    else:
        values = []
        for session in range(1,sessionNum+1):
            text_file = open('Patient Details/{}/{}{}.txt'.format((ID+ur),ID,session), "r+")
            content = text_file.readlines()
            line = content[FINGER_LINE]   
            line = "".join(line)
            val = "".join(re.findall('\d*\.?\d+',line))

            # val = ''.join(char for char in line if char.isdigit())
            text_file.close()

            values.append("{}".format(val))
   
        return(values)  

def getPatientID(name):
    name_list = name.split() 

    initials = ""

    for split_name in name_list:  # go through each name
        initials += split_name[0].upper()  # append the initial    

    return initials

# We assume the patient name is split with a space 
def checkPatientDetails(name,ur):
    
    patientID = getPatientID(name)
    
    return(checkReturningPatient((patientID+ur),patientID)) # return 1 if is reoccuring
                                             # return 0 if new

#trys to open a file with the users ID
# IF: can open --> previous patient must exist
# ELSE: must be a new patient 
def checkReturningPatient(urInits, initials):
    file_path = ("Patient Details/{}/{}1.txt".format(urInits,initials))

    if not os.path.exists(file_path):
        return 0
    else: 
        return 1


# returns a string that can be used as a label for the patient history
def displayPatientHistory(PatientID,ur,sessionNum, exported):

    #we are assuming that the we haven't exported the current data
    if (exported == None):
        print('nothing to view')
        return 0
    else:
        if (sessionNum > 1):
            sessionNum = (sessionNum - 1)
 
    # numLines = 11*sessionNum
    contents = ""

    if (sessionNum == 1):
        text_file = open('Patient Details/{}/{}{}.txt'.format((PatientID+ur),PatientID,sessionNum), "r+")
        content = text_file.readlines()
        line = content[:11]
        contents = " ".join(line)
        return(contents)    

    else:
        for session in range(1,sessionNum+1):
            print(session)
            text_file = open('Patient Details/{}/{}{}.txt'.format((PatientID+ur),PatientID,session), "r+")
            content = text_file.readlines()
            line = content[:11]   
            line = "".join(line)
            line = (line + "-----------------------------------------------------------------------------------------\n")

            text_file.close()
            contents += line
            print(contents)

            # contents = contents.join("\n") 

        # print(contents)   
        return(contents)   

            
