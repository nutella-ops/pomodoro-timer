#!/usr/bin/python3
import time, os

sysTime = time.ctime().split()
day = sysTime[2]
month = sysTime[1]
dayLow = (month + day).lower()
fileName = dayLow +".txt"
dayMonth = month + " " + day
logHeader = dayMonth
os.system("echo " + logHeader + " >> /tmp/" + fileName)

def dayCheck():
    if (sysTime[2] == day):
        os.system("echo " + logPom + " >> /tmp/" + fileName)
    else:
        os.system("echo " + logHeader + " >> /tmp/" + fileName)
        os.system("echo " + logPom + " >> /tmp/" + fileName)

pom = 0
# try:
while(1):
    userInput = input("[" + str(pom) + "] minutes: ")
    minutes = float(userInput)

    startTime = sysTime[3][0:5]
    time.sleep(minutes * 60)
    stopTime = sysTime[3][0:5]
    os.system("ffplay -nodisp -autoexit $(find ~ -name 'g.wav' 2>/dev/null) 2>/dev/null")
    logPom = startTime + ", " + stopTime
    print(logHeader + ", " + logPom)
    dayCheck()
    pom += 1
# except KeyboardInterrupt:
#    response = input("Save your data?: ") 
#     if (response.lower()[0] == y):
#         os.system("mkdir ~/Documents/poms")
#         os.system("mv /tmp/" + month.lower() + "*.txt ~/Documents/poms"