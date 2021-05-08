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
    line = content[4]
    return(''.join(char for char in line if char.isdigit()))

def getPreviousWrist(sessionNum,ID):
    #row 8 if counting from 1
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[7]
    return(''.join(char for char in line if char.isdigit()))

    
def getPreviousShoulder(sessionNum,ID):
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[9]
    return(''.join(char for char in line if char.isdigit()))    

def getPreviousFinger(sessionNum,ID):
    text_file = open('./Patient Details/{}/{}{}.txt'.format(ID,ID,sessionNum), "r+")
    content = text_file.readlines()
    line = content[8]
    return(''.join(char for char in line if char.isdigit()))   
