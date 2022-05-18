#!/usr/bin/python3
import time, os, math, playsound

## CONSTANTS & VARIABLES ##
# system time and date when the program is started
initTime = time.ctime().split()

# day and month when the program started
initDay = initTime[2]
initMonth = initTime[1]

# create a file name that is month and day, lowercase, with no spaces
fileName = (initDay + initMonth).lower() +".txt"

# the month and day column label in the log file
logHeader = time.ctime().split()[1] + " " + time.ctime().split()[2]

# set and create the directory
filePath =  os.environ['HOME'] + "/Documents/poms" + "/" + fileName

## FUNCTIONS ##
# check if a pom log for the day the program was started already exists
def writeLine(what, where):
    where.write(what + "\n")

def checkExisting():
    # ask for username, for security/privacy due to posting on github
    # if file exists, do nothing, if not, write a date column label to the log file
    if not os.path.exists(filePath):
        logFile = open(filePath, "a")
        writeLine(logHeader, logFile)
        logFile.close()


# check if the day has changed since the program was started
def dayCheck():
    dayNow = time.ctime().split()[2]
    logFile = open(filePath, "a")
    if (dayNow == initDay):
        writeLine(logPom, logFile)
    else:
        writeLine(logHeader, logFile)
        writeLine(logPom, logFile)
        initDay = dayNow
    logFile.close()


## MAIN PROGRAM ##
checkExisting()
# set the pomodoro counter to 0
pom = 0

# start an infinite loop
while(1):
    #prompt user for the pomodoro length and convert the user input from a string to a floating-point number
    userInput = input("[" + str(pom) + "] minutes: ")
    minutes = float(userInput)

    # save the start time to a variable
    # wait for the user-specified amount of time
    # save the end time to a variable
    startTime = time.ctime().split()[3][0:5]

    ## begin code written by my friend ##
    remaining = minutes * 60
    while remaining > 0:
        time.sleep(1)
        print(str(math.floor(remaining / 60)) + "m " + str(int(remaining % 60))+ "s     ", end="")
        remaining -= 1
        print("\r", end="")
    ## end code written by my friend ##

    stopTime = time.ctime().split()[3][0:5]
    
    # play da sound
    playsound.playsound('res/g.wav')
    
    # format the start and stop times with a comma and save to a variable
    logPom = startTime + ", " + stopTime

    # print(logHeader + ", " + logPom)
    dayCheck()
    pom += 1
